from django import forms
from .models import (
    ContactInquiry, Announcement, GalleryImage, Department,
    Topper, FacultyMember, QuickDownload, LeadershipProfile
)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 focus:border-red-600 focus:ring-2 focus:ring-red-100 transition outline-none', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 focus:border-red-600 focus:ring-2 focus:ring-red-100 transition outline-none', 'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 focus:border-red-600 focus:ring-2 focus:ring-red-100 transition outline-none', 'placeholder': '10-Digit Mobile Number'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 focus:border-red-600 focus:ring-2 focus:ring-red-100 transition outline-none', 'placeholder': 'Subject of Inquiry'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-lg border border-slate-300 focus:border-red-600 focus:ring-2 focus:ring-red-100 transition outline-none h-32 resize-none', 'placeholder': 'Write your message or feedback here...'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name', 'code', 'intake', 'duration', 'hod_name',
            'hod_qualification', 'hod_message', 'short_description',
            'description', 'lab_facilities', 'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. Computer Science & Engineering'}),
            'code': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. CSE'}),
            'intake': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': '60'}),
            'duration': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': '3 Years (6 Semesters)'}),
            'hod_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'HOD Full Name'}),
            'hod_qualification': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. M.Tech / B.E.'}),
            'hod_message': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg h-24 focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'HOD message to students...'}),
            'short_description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg h-20 focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'Brief 1-2 sentence program summary...'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg h-32 focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'Detailed curriculum and scope description...'}),
            'lab_facilities': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg h-28 focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'One lab per line, e.g.:\nData Structures Lab\nWeb Development Lab\nPython & AI Lab'}),
        }

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'category', 'content', 'document', 'link', 'is_important', 'is_ticker', 'publish_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'category': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'content': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg h-24 focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'link': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'publish_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'category', 'image', 'caption']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'category': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'caption': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
        }

class FacultyForm(forms.ModelForm):
    class Meta:
        model = FacultyMember
        fields = ['name', 'designation', 'department', 'qualification', 'experience', 'email', 'phone', 'photo', 'is_hod', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'designation': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. Senior Lecturer'}),
            'department': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'qualification': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. M.Tech in CS'}),
            'experience': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. 10 Years'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'order': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
        }

class TopperForm(forms.ModelForm):
    class Meta:
        model = Topper
        fields = ['student_name', 'department', 'semester', 'percentage', 'year', 'photo']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'Student Full Name'}),
            'department': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'semester': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. 1st Semester'}),
            'percentage': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. 90.33', 'step': '0.01'}),
            'year': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. 2024-2025'}),
        }

class QuickDownloadForm(forms.ModelForm):
    class Meta:
        model = QuickDownload
        fields = ['title', 'category', 'file', 'external_link', 'order', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. Academic Calendar 2025-26'}),
            'category': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. AICTE / DTE Document'}),
            'external_link': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'https://...'}),
            'order': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
        }

class LeadershipForm(forms.ModelForm):
    class Meta:
        model = LeadershipProfile
        fields = ['role_type', 'honorific', 'name', 'title', 'message', 'photo', 'is_active']
        widgets = {
            'role_type': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500'}),
            'honorific': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. Poojyasri / Dr.'}),
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'Full Name'}),
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'e.g. Ex. M.L.C | Founder'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-slate-300 rounded-lg h-24 focus:outline-none focus:ring-2 focus:ring-red-500', 'placeholder': 'Founder vision or principal desk speech...'}),
        }
