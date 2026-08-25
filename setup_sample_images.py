import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mes_polytechnic.settings')
django.setup()

from website.models import Department, FacultyMember, GalleryImage, Topper

def run():
    print("--- Setting up sample media image files ---")

    # Base source image
    source_img = os.path.join('resources', 'college.jpg')
    logo_img = os.path.join('resources', 'college_logo.png')

    if not os.path.exists(source_img):
        print("Source image resources/college.jpg not found.")
        return

    # Directories
    os.makedirs('media/gallery', exist_ok=True)
    os.makedirs('media/faculty', exist_ok=True)
    os.makedirs('media/toppers', exist_ok=True)
    os.makedirs('media/departments', exist_ok=True)

    # 1. Update Gallery Images with real media files
    for idx, img_obj in enumerate(GalleryImage.objects.all()):
        target_name = f"gallery_{img_obj.id}.jpg"
        target_path = os.path.join('media', 'gallery', target_name)
        shutil.copy(source_img, target_path)
        img_obj.image = f"gallery/{target_name}"
        img_obj.save()
        print(f"Updated gallery image: {img_obj.title} -> media/gallery/{target_name}")

    # 2. Seed Faculty Members with pictures
    dept_cse = Department.objects.filter(code='CSE').first()
    dept_ece = Department.objects.filter(code='ECE').first()
    dept_me = Department.objects.filter(code='ME').first()
    dept_ce = Department.objects.filter(code='CE').first()
    dept_eee = Department.objects.filter(code='EEE').first()

    faculty_data = [
        # CSE
        {'name': 'Prof. Ramesh K. S.', 'designation': 'Head of Department & Professor', 'department': dept_cse, 'qualification': 'M.Tech in CS, Ph.D.', 'experience': '15+ Years', 'is_hod': True, 'order': 1},
        {'name': 'Sri Kumar Swamy V.', 'designation': 'Selection Grade Lecturer', 'department': dept_cse, 'qualification': 'M.Tech in Software Engg', 'experience': '12 Years', 'is_hod': False, 'order': 2},
        {'name': 'Smt. Divya M.', 'designation': 'Lecturer (Web & DBMS)', 'department': dept_cse, 'qualification': 'B.E. in CS', 'experience': '7 Years', 'is_hod': False, 'order': 3},
        
        # ECE
        {'name': 'Prof. Suresh Kumar V.', 'designation': 'Head of Department & Professor', 'department': dept_ece, 'qualification': 'M.Tech in Digital Electronics', 'experience': '16 Years', 'is_hod': True, 'order': 1},
        {'name': 'Sri Nagaraju B.', 'designation': 'Senior Lecturer (VLSI & IoT)', 'department': dept_ece, 'qualification': 'M.Tech in Electronics', 'experience': '10 Years', 'is_hod': False, 'order': 2},
        
        # ME
        {'name': 'Prof. Manjunath N.', 'designation': 'Head of Department & Professor', 'department': dept_me, 'qualification': 'M.Tech in Machine Design', 'experience': '18 Years', 'is_hod': True, 'order': 1},
        {'name': 'Sri Prakash G.', 'designation': 'Senior Workshop Superintendent', 'department': dept_me, 'qualification': 'B.E. in Mechanical', 'experience': '14 Years', 'is_hod': False, 'order': 2},
        
        # CE
        {'name': 'Prof. Shivashankar M.', 'designation': 'Head of Department & Professor', 'department': dept_ce, 'qualification': 'M.Tech in Structural Engineering', 'experience': '15 Years', 'is_hod': True, 'order': 1},
        {'name': 'Smt. Kavitha R.', 'designation': 'Lecturer (Surveying & CAD)', 'department': dept_ce, 'qualification': 'M.Tech in Transportation', 'experience': '8 Years', 'is_hod': False, 'order': 2},
        
        # EEE
        {'name': 'Prof. Ananda V.', 'designation': 'Head of Department & Professor', 'department': dept_eee, 'qualification': 'M.Tech in Power Systems', 'experience': '17 Years', 'is_hod': True, 'order': 1},
        {'name': 'Sri Harish Kumar', 'designation': 'Lecturer (Electrical Machines)', 'department': dept_eee, 'qualification': 'B.E. in Electrical', 'experience': '9 Years', 'is_hod': False, 'order': 2},
    ]

    for item in faculty_data:
        if item['department']:
            fac_obj, created = FacultyMember.objects.get_or_create(
                name=item['name'],
                department=item['department'],
                defaults=item
            )
            # Copy sample image for faculty photo
            target_name = f"faculty_{fac_obj.id}.jpg"
            target_path = os.path.join('media', 'faculty', target_name)
            shutil.copy(source_img, target_path)
            fac_obj.photo = f"faculty/{target_name}"
            fac_obj.save()
            print(f"Processed Faculty: {fac_obj.name} ({fac_obj.department.code})")

    # 3. Copy image for toppers
    for topper in Topper.objects.all():
        target_name = f"topper_{topper.id}.jpg"
        target_path = os.path.join('media', 'toppers', target_name)
        shutil.copy(source_img, target_path)
        topper.photo = f"toppers/{target_name}"
        topper.save()
        print(f"Updated topper photo: {topper.student_name}")

    print("--- Media image setup completed successfully! ---")

if __name__ == '__main__':
    run()
