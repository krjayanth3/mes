from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import (
    Department, FacultyMember, Announcement, GalleryImage, Committee,
    Topper, ContactInquiry, CampusFacility, QuickDownload, LeadershipProfile,
    AnnouncementCategory, GalleryCategory
)
from .forms import (
    ContactForm, DepartmentForm, AnnouncementForm, GalleryForm,
    FacultyForm, TopperForm, QuickDownloadForm, LeadershipForm
)

def home_view(request):
    announcements = Announcement.objects.filter(is_important=True)[:6]
    departments = Department.objects.all()
    toppers = Topper.objects.all()[:6]
    gallery_preview = GalleryImage.objects.all()[:8]
    facilities = CampusFacility.objects.all()
    quick_downloads = QuickDownload.objects.filter(is_active=True).order_by('order', '-created_at')[:8]
    founder_profile = LeadershipProfile.objects.filter(role_type='FOUNDER', is_active=True).first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your message has been sent to MES Polytechnic administration.")
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'announcements': announcements,
        'departments': departments,
        'toppers': toppers,
        'gallery_preview': gallery_preview,
        'facilities': facilities,
        'quick_downloads': quick_downloads,
        'founder_profile': founder_profile,
        'contact_form': form,
    }
    return render(request, 'website/home.html', context)

def about_view(request):
    committees = Committee.objects.all()
    founder_profile = LeadershipProfile.objects.filter(role_type='FOUNDER', is_active=True).first()
    principal_profile = LeadershipProfile.objects.filter(role_type='PRINCIPAL', is_active=True).first()
    
    context = {
        'committees': committees,
        'founder_profile': founder_profile,
        'principal_profile': principal_profile,
    }
    return render(request, 'website/about.html', context)

def departments_view(request):
    departments = Department.objects.all()
    return render(request, 'website/departments.html', {'departments': departments})

def department_detail_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    other_departments = Department.objects.exclude(id=department.id)
    dept_toppers = department.toppers.all()
    faculty_list = department.faculty_members.all()
    
    # Process lab facilities into list
    labs_list = []
    if department.lab_facilities:
        labs_list = [lab.strip() for lab in department.lab_facilities.split('\n') if lab.strip()]

    context = {
        'department': department,
        'other_departments': other_departments,
        'dept_toppers': dept_toppers,
        'faculty_list': faculty_list,
        'labs_list': labs_list,
    }
    return render(request, 'website/department_detail.html', context)

def faculty_view(request):
    departments = Department.objects.all().prefetch_related('faculty_members')
    selected_dept = request.GET.get('dept', '')
    
    if selected_dept:
        departments = departments.filter(code=selected_dept)
        
    context = {
        'departments': departments,
        'selected_dept': selected_dept,
    }
    return render(request, 'website/faculty.html', context)

def notices_view(request):
    category = request.GET.get('category', '')
    query = request.GET.get('q', '')

    notices = Announcement.objects.all()

    if category:
        notices = notices.filter(category=category)
    if query:
        notices = notices.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {
        'notices': notices,
        'categories': AnnouncementCategory.choices,
        'selected_category': category,
        'search_query': query,
    }
    return render(request, 'website/notices.html', context)

def gallery_view(request):
    category = request.GET.get('category', '')
    images = GalleryImage.objects.all()

    if category:
        images = images.filter(category=category)

    context = {
        'images': images,
        'categories': GalleryCategory.choices,
        'selected_category': category,
    }
    return render(request, 'website/gallery.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully! Our office will get back to you shortly.")
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors in the form below.")
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})

def staff_login_view(request):
    if request.user.is_authenticated:
        return redirect('staff_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('staff_dashboard')
        else:
            messages.error(request, "Invalid staff credentials or unauthorized access.")

    return render(request, 'website/login.html')

def staff_logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out safely.")
    return redirect('home')

@login_required
def staff_dashboard_view(request):
    department_form = DepartmentForm()
    announcement_form = AnnouncementForm()
    gallery_form = GalleryForm()
    faculty_form = FacultyForm()
    topper_form = TopperForm()
    download_form = QuickDownloadForm()
    leadership_form = LeadershipForm()

    if request.method == 'POST':
        if 'submit_department' in request.POST:
            department_form = DepartmentForm(request.POST, request.FILES)
            if department_form.is_valid():
                department_form.save()
                messages.success(request, "New Department program added successfully!")
                return redirect('staff_dashboard')
        elif 'submit_announcement' in request.POST:
            announcement_form = AnnouncementForm(request.POST, request.FILES)
            if announcement_form.is_valid():
                announcement_form.save()
                messages.success(request, "New announcement posted successfully!")
                return redirect('staff_dashboard')
        elif 'submit_gallery' in request.POST:
            gallery_form = GalleryForm(request.POST, request.FILES)
            if gallery_form.is_valid():
                gallery_form.save()
                messages.success(request, "New gallery image uploaded successfully!")
                return redirect('staff_dashboard')
        elif 'submit_faculty' in request.POST:
            faculty_form = FacultyForm(request.POST, request.FILES)
            if faculty_form.is_valid():
                faculty_form.save()
                messages.success(request, "New faculty member added successfully!")
                return redirect('staff_dashboard')
        elif 'submit_topper' in request.POST:
            topper_form = TopperForm(request.POST, request.FILES)
            if topper_form.is_valid():
                topper_form.save()
                messages.success(request, "Academic Achiever / Topper added successfully!")
                return redirect('staff_dashboard')
        elif 'submit_download' in request.POST:
            download_form = QuickDownloadForm(request.POST, request.FILES)
            if download_form.is_valid():
                download_form.save()
                messages.success(request, "Quick Download document/link added successfully!")
                return redirect('staff_dashboard')
        elif 'submit_leadership' in request.POST:
            leadership_form = LeadershipForm(request.POST, request.FILES)
            if leadership_form.is_valid():
                leadership_form.save()
                messages.success(request, "Founder / Leadership Profile updated successfully!")
                return redirect('staff_dashboard')

    departments = Department.objects.all()
    announcements = Announcement.objects.all()[:15]
    gallery_images = GalleryImage.objects.all()[:15]
    faculty_members = FacultyMember.objects.all()
    toppers = Topper.objects.all()
    quick_downloads = QuickDownload.objects.all()
    leadership_profiles = LeadershipProfile.objects.all()
    inquiries = ContactInquiry.objects.all()[:20]

    context = {
        'department_form': department_form,
        'announcement_form': announcement_form,
        'gallery_form': gallery_form,
        'faculty_form': faculty_form,
        'topper_form': topper_form,
        'download_form': download_form,
        'leadership_form': leadership_form,
        'departments': departments,
        'announcements': announcements,
        'gallery_images': gallery_images,
        'faculty_members': faculty_members,
        'toppers': toppers,
        'quick_downloads': quick_downloads,
        'leadership_profiles': leadership_profiles,
        'inquiries': inquiries,
    }
    return render(request, 'website/staff_dashboard.html', context)

# --- EDIT VIEWS ---

@login_required
def edit_department_view(request, pk):
    item = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Department '{item.name}' ({item.code}) updated successfully!")
            return redirect('staff_dashboard')
    else:
        form = DepartmentForm(instance=item)
    return render(request, 'website/edit_item.html', {
        'form': form,
        'title': f"Edit Department: {item.name} ({item.code})",
        'item_type': 'Department Program & Intake',
        'current_image': item.image.url if item.image else None,
        'back_url': 'staff_dashboard'
    })

@login_required
def edit_announcement_view(request, pk):
    item = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Announcement '{item.title}' updated successfully!")
            return redirect('staff_dashboard')
    else:
        form = AnnouncementForm(instance=item)
    return render(request, 'website/edit_item.html', {
        'form': form,
        'title': f"Edit Announcement: {item.title}",
        'item_type': 'Announcement',
        'back_url': 'staff_dashboard'
    })

@login_required
def edit_gallery_view(request, pk):
    item = get_object_or_404(GalleryImage, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Gallery Image '{item.title}' updated successfully!")
            return redirect('staff_dashboard')
    else:
        form = GalleryForm(instance=item)
    return render(request, 'website/edit_item.html', {
        'form': form,
        'title': f"Edit Gallery Image: {item.title}",
        'item_type': 'Gallery Image',
        'current_image': item.image.url if item.image else None,
        'back_url': 'staff_dashboard'
    })

@login_required
def edit_faculty_view(request, pk):
    item = get_object_or_404(FacultyMember, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Faculty profile '{item.name}' updated successfully!")
            return redirect('staff_dashboard')
    else:
        form = FacultyForm(instance=item)
    return render(request, 'website/edit_item.html', {
        'form': form,
        'title': f"Edit Faculty Member: {item.name}",
        'item_type': 'Faculty Member',
        'current_image': item.photo.url if item.photo else None,
        'back_url': 'staff_dashboard'
    })

@login_required
def edit_topper_view(request, pk):
    item = get_object_or_404(Topper, pk=pk)
    if request.method == 'POST':
        form = TopperForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Academic Achiever '{item.student_name}' updated successfully!")
            return redirect('staff_dashboard')
    else:
        form = TopperForm(instance=item)
    return render(request, 'website/edit_item.html', {
        'form': form,
        'title': f"Edit Academic Achiever: {item.student_name}",
        'item_type': 'Academic Achiever / Topper',
        'current_image': item.photo.url if item.photo else None,
        'back_url': 'staff_dashboard'
    })

@login_required
def edit_quick_download_view(request, pk):
    item = get_object_or_404(QuickDownload, pk=pk)
    if request.method == 'POST':
        form = QuickDownloadForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Quick Download '{item.title}' updated successfully!")
            return redirect('staff_dashboard')
    else:
        form = QuickDownloadForm(instance=item)
    return render(request, 'website/edit_item.html', {
        'form': form,
        'title': f"Edit Quick Download: {item.title}",
        'item_type': 'Quick Download Document',
        'current_file': item.file.url if item.file else None,
        'back_url': 'staff_dashboard'
    })

@login_required
def edit_leadership_view(request, pk):
    item = get_object_or_404(LeadershipProfile, pk=pk)
    if request.method == 'POST':
        form = LeadershipForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Leadership Profile '{item.name}' updated successfully!")
            return redirect('staff_dashboard')
    else:
        form = LeadershipForm(instance=item)
    return render(request, 'website/edit_item.html', {
        'form': form,
        'title': f"Edit Leadership Profile: {item.name}",
        'item_type': 'Leadership & Founder Profile',
        'current_image': item.photo.url if item.photo else None,
        'back_url': 'staff_dashboard'
    })

# --- DELETE VIEWS ---

@login_required
def delete_department_view(request, pk):
    item = get_object_or_404(Department, pk=pk)
    name = item.name
    item.delete()
    messages.success(request, f"Department '{name}' deleted successfully.")
    return redirect('staff_dashboard')

@login_required
def delete_announcement_view(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    announcement.delete()
    messages.success(request, "Announcement deleted successfully.")
    return redirect('staff_dashboard')

@login_required
def delete_gallery_view(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    image.delete()
    messages.success(request, "Gallery image deleted successfully.")
    return redirect('staff_dashboard')

@login_required
def delete_faculty_view(request, pk):
    faculty = get_object_or_404(FacultyMember, pk=pk)
    faculty.delete()
    messages.success(request, "Faculty member deleted successfully.")
    return redirect('staff_dashboard')

@login_required
def delete_topper_view(request, pk):
    topper = get_object_or_404(Topper, pk=pk)
    topper.delete()
    messages.success(request, "Academic Achiever / Topper deleted successfully.")
    return redirect('staff_dashboard')

@login_required
def delete_quick_download_view(request, pk):
    item = get_object_or_404(QuickDownload, pk=pk)
    item.delete()
    messages.success(request, "Quick Download item deleted successfully.")
    return redirect('staff_dashboard')

@login_required
def delete_leadership_view(request, pk):
    item = get_object_or_404(LeadershipProfile, pk=pk)
    item.delete()
    messages.success(request, "Leadership Profile deleted successfully.")
    return redirect('staff_dashboard')
