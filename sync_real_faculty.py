import os
import shutil
import urllib.parse
import requests
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mes_polytechnic.settings')
django.setup()

from website.models import (
    Department, FacultyMember, LeadershipProfile, LeadershipRole
)

BASE_URL = 'https://www.mespolytechnic.in/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def download_file(relative_url, dest_dir, filename=None):
    os.makedirs(dest_dir, exist_ok=True)
    if not filename:
        filename = os.path.basename(relative_url)
    
    encoded_url = urllib.parse.urljoin(BASE_URL, urllib.parse.quote(relative_url, safe='/'))
    dest_path = os.path.join(dest_dir, filename)
    try:
        r = requests.get(encoded_url, headers=HEADERS, timeout=8)
        if r.status_code == 200:
            with open(dest_path, 'wb') as f:
                f.write(r.content)
            print(f"[DOWNLOAD OK] {relative_url} -> {dest_path} ({len(r.content)} bytes)")
            return dest_path
        else:
            print(f"[DOWNLOAD FAIL {r.status_code}] {encoded_url}")
    except Exception as e:
        print(f"[DOWNLOAD ERROR] {encoded_url}: {e}")
    return None

def sync_faculty():
    print("==================================================")
    print("  PARSING & SYNCING EXACT FACULTY FROM FACULTY.HTML")
    print("==================================================")

    # 1. Ensure Science & Humanities Department exists
    sh_dept, _ = Department.objects.get_or_create(
        code='SH',
        defaults={
            'name': 'Science & Humanities (General)',
            'short_description': 'Foundational education in Applied Physics, Applied Chemistry, Mathematics, and Communication Skills for 1st-year engineering students.',
            'description': 'The Science & Humanities department lays the foundational mathematical and scientific principles necessary for engineering analysis. The department is staffed with highly experienced lecturers in Physics, Chemistry, Mathematics, and English.',
            'intake': 60,
            'duration': '1st Year Foundation',
            'hod_name': 'G V PUTTAMALLAIAH',
            'hod_qualification': 'M.Sc',
            'hod_message': 'Strong fundamentals in applied sciences and communication empower students to excel in core engineering domains.',
            'icon_class': 'fa-atom',
            'image': 'gallery/gallery_003.jpg'
        }
    )

    # 2. Update HOD names for all existing departments
    dept_map = {
        'CE': ('Civil Engineering', 'JANARDHAN K N', 'B.E.'),
        'ECE': ('Electronics & Communication Engg', 'MADHU MOHAN P', 'DIP / POST DIP'),
        'ME': ('Mechanical Engineering', 'ERANNA K N', 'B.E.'),
        'CSE': ('Computer Science & Engineering', 'MANJUNATH E', 'B.E.'),
        'EEE': ('Electrical & Electronics Engg', 'KRISHNAPPA', 'DIP / POST DIP'),
        'SH': ('Science & Humanities', 'G V PUTTAMALLAIAH', 'M.Sc'),
    }

    for code, (name, hod_name, hod_qual) in dept_map.items():
        d = Department.objects.filter(code=code).first()
        if d:
            d.hod_name = hod_name
            d.hod_qualification = hod_qual
            d.save()
            print(f"[DEPT UPDATED] {code} -> HOD: {hod_name} ({hod_qual})")

    # 3. Sync Principal Profile with real photo
    print("\n--- Syncing Principal (M L VENU) ---")
    os.makedirs('media/leadership', exist_ok=True)
    princ_photo = download_file('images/ml-venu.jpg', 'media/leadership', 'ml_venu.jpg')
    
    principal_obj, _ = LeadershipProfile.objects.get_or_create(
        role_type=LeadershipRole.PRINCIPAL,
        defaults={
            'honorific': 'Prof.',
            'name': 'M L VENU',
            'title': 'Principal, M.E.S. Polytechnic, Madhugiri (Code 347)',
            'message': 'At M.E.S. Polytechnic, we emphasize practical learning, skill workshops, disciplined academic rigor, and active industry participation so that every diploma graduate steps out with confidence and high competence.',
            'photo': 'leadership/ml_venu.jpg',
            'order': 2,
            'is_active': True
        }
    )
    principal_obj.name = 'M L VENU'
    principal_obj.honorific = 'Prof.'
    principal_obj.title = 'Principal, M.E.S. Polytechnic, Madhugiri (Code 347)'
    if princ_photo:
        principal_obj.photo = 'leadership/ml_venu.jpg'
    principal_obj.save()
    print(f"[PRINCIPAL UPDATED] {principal_obj.name} -> {principal_obj.photo}")

    # 4. Clean out old faculty records and populate EXACT list from official site
    print("\n--- Scraping Faculty Tables from faculty.html ---")
    FacultyMember.objects.all().delete()
    os.makedirs('media/faculty', exist_ok=True)

    faculty_dataset = [
        # Table 2: Civil Engineering
        {'dept': 'CE', 'name': 'JANARDHAN K N', 'desig': 'Head of Department', 'qual': 'B.E.', 'phone': '7026436191', 'photo_url': 'images/janardhan-kn.jpg', 'is_hod': True, 'order': 1},
        {'dept': 'CE', 'name': 'SINDHU M P', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9164942160', 'photo_url': 'photo/civil/sindhu.jpg', 'is_hod': False, 'order': 2},
        {'dept': 'CE', 'name': 'CHETHAN V', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '7849049815', 'photo_url': 'photo/civil/chethan.jpg', 'is_hod': False, 'order': 3},
        {'dept': 'CE', 'name': 'DIVYA A R', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9964282849', 'photo_url': 'photo/civil/divya.jpg', 'is_hod': False, 'order': 4},

        # Table 3: Electronics & Communication
        {'dept': 'ECE', 'name': 'MADHU MOHAN P', 'desig': 'Head of Department', 'qual': 'DIP / POST DIP', 'phone': '9916741832', 'photo_url': 'photo/ec/madhumohan.jpg', 'is_hod': True, 'order': 1},
        {'dept': 'ECE', 'name': 'RASHMI GH', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9449740593', 'photo_url': 'photo/ec/rashmi.jpg', 'is_hod': False, 'order': 2},
        {'dept': 'ECE', 'name': 'HASEENA TAJ', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9901056059', 'photo_url': 'images/haseena-taj.jpg', 'is_hod': False, 'order': 3},
        {'dept': 'ECE', 'name': 'PRADEEP KUMAR M P', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9964166785', 'photo_url': 'photo/ec/pradeep.jpg', 'is_hod': False, 'order': 4},
        {'dept': 'ECE', 'name': 'RIZWAN BASHA', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '8722332535', 'photo_url': 'photo/ec/rizwan.jpg', 'is_hod': False, 'order': 5},
        {'dept': 'ECE', 'name': 'Navyashree B K', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '7022271569', 'photo_url': 'photo/ec/Navyashree B K.jpeg', 'is_hod': False, 'order': 6},

        # Table 4: Mechanical Engineering
        {'dept': 'ME', 'name': 'ERANNA K N', 'desig': 'Head of Department', 'qual': 'B.E.', 'phone': '9448747848', 'photo_url': 'photo/me/eranna.jpg', 'is_hod': True, 'order': 1},
        {'dept': 'ME', 'name': 'VEDASHREE R', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '7406746542', 'photo_url': 'photo/me/vedha.jpg', 'is_hod': False, 'order': 2},
        {'dept': 'ME', 'name': 'VILAS KUMAR V', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9449266586', 'photo_url': 'photo/me/vilas.jpg', 'is_hod': False, 'order': 3},
        {'dept': 'ME', 'name': 'MANJUNATH K R', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9686274423', 'photo_url': 'photo/me/manjunath.jpg', 'is_hod': False, 'order': 4},
        {'dept': 'ME', 'name': 'IBRAHIM PASHA', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '8904466801', 'photo_url': 'images/ibrahim.jpg', 'is_hod': False, 'order': 5},

        # Table 5: Computer Science & Engineering
        {'dept': 'CSE', 'name': 'MANJUNATH E', 'desig': 'Head of Department', 'qual': 'B.E.', 'phone': '9538259757', 'photo_url': 'photo/cs/manjunathe.jpg', 'is_hod': True, 'order': 1},
        {'dept': 'CSE', 'name': 'SUMANA A R', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9901361362', 'photo_url': 'photo/cs/Sumana A R.jpeg', 'is_hod': False, 'order': 2},
        {'dept': 'CSE', 'name': 'Jyothi N R', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '8884155653', 'photo_url': 'photo/cs/Jyothi N R.jpeg', 'is_hod': False, 'order': 3},
        {'dept': 'CSE', 'name': 'RASHMI T V', 'desig': 'Lecturer', 'qual': 'M.TECH', 'phone': '8197581544', 'photo_url': 'photo/cs/rashmi.jpg', 'is_hod': False, 'order': 4},
        {'dept': 'CSE', 'name': 'NAVEEN KUMAR J', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '7829647685', 'photo_url': 'images/Naveen kumar J.jpeg', 'is_hod': False, 'order': 5},
        {'dept': 'CSE', 'name': 'SHWETHA M', 'desig': 'Instructor', 'qual': 'DIP / POST DIP', 'phone': '9663624460', 'photo_url': 'photo/cs/Shwetha.jpeg', 'is_hod': False, 'order': 6},
        {'dept': 'CSE', 'name': 'MAMATHA R', 'desig': 'Instructor', 'qual': 'SSLC', 'phone': '9845607890', 'photo_url': 'photo/cs/Mamatha.jpeg', 'is_hod': False, 'order': 7},

        # Table 6: Electrical & Electronics Engineering
        {'dept': 'EEE', 'name': 'KRISHNAPPA', 'desig': 'Head of Department', 'qual': 'DIP / POST DIP', 'phone': '9901164232', 'photo_url': 'photo/ee/krishnappa.jpg', 'is_hod': True, 'order': 1},
        {'dept': 'EEE', 'name': 'SATHISH KUMAR M R', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9900439287', 'photo_url': 'photo/ee/sathish.jpg', 'is_hod': False, 'order': 2},
        {'dept': 'EEE', 'name': 'RAVIKUMAR V S', 'desig': 'Lecturer', 'qual': 'M.E.', 'phone': '9482908927', 'photo_url': 'photo/ee/ravikumar.jpg', 'is_hod': False, 'order': 3},
        {'dept': 'EEE', 'name': 'NISCHALA G', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '9620866546', 'photo_url': 'photo/ee/nishchala.jpg', 'is_hod': False, 'order': 4},
        {'dept': 'EEE', 'name': 'Nandini K', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '8105011866', 'photo_url': 'photo/ee/Nandini K.jpeg', 'is_hod': False, 'order': 5},
        {'dept': 'EEE', 'name': 'Prathima K J', 'desig': 'Lecturer', 'qual': 'B.E.', 'phone': '7619468725', 'photo_url': 'photo/ee/Prathima.jpeg', 'is_hod': False, 'order': 6},
        {'dept': 'EEE', 'name': 'NAGESH BABU J', 'desig': 'Instructor', 'qual': 'ITI', 'phone': '8050838265', 'photo_url': 'photo/ee/nageshbabu.jpg', 'is_hod': False, 'order': 7},

        # Table 7: Science & Humanities
        {'dept': 'SH', 'name': 'G V PUTTAMALLAIAH', 'desig': 'Head of Department', 'qual': 'M.Sc', 'phone': '9060079200', 'photo_url': 'photo/science/gvp.jpg', 'is_hod': True, 'order': 1},
        {'dept': 'SH', 'name': 'NAGENDRA KUMAR D N', 'desig': 'Lecturer', 'qual': 'M.Phil', 'phone': '9986740811', 'photo_url': 'photo/science/nagendrakumar.jpg', 'is_hod': False, 'order': 2},
        {'dept': 'SH', 'name': 'MANJUNATHA B K', 'desig': 'Lecturer', 'qual': 'M.A.', 'phone': '9901080143', 'photo_url': 'photo/science/manjunath.jpg', 'is_hod': False, 'order': 3},
        {'dept': 'SH', 'name': 'CHANDANA R', 'desig': 'Lecturer', 'qual': 'M.Sc', 'phone': '8660293531', 'photo_url': 'photo/science/chandana.jpeg', 'is_hod': False, 'order': 4},
    ]

    for item in faculty_dataset:
        dept_obj = Department.objects.filter(code=item['dept']).first()
        if not dept_obj:
            print(f"[SKIP] Department {item['dept']} not found")
            continue

        raw_filename = os.path.basename(item['photo_url'])
        clean_filename = f"{item['dept'].lower()}_{raw_filename.replace(' ', '_').lower()}"
        downloaded_file = download_file(item['photo_url'], 'media/faculty', clean_filename)
        rel_photo_path = f"faculty/{clean_filename}" if downloaded_file else None

        FacultyMember.objects.create(
            name=item['name'],
            designation=item['desig'],
            department=dept_obj,
            qualification=item['qual'],
            experience='Faculty Member',
            phone=item['phone'],
            photo=rel_photo_path,
            is_hod=item['is_hod'],
            order=item['order']
        )
        print(f"[FACULTY CREATED] {item['name']} ({item['desig']}) -> {rel_photo_path}")

    print(f"\n==================================================")
    print(f"  SUCCESS! {FacultyMember.objects.count()} OFFICIAL FACULTY MEMBERS POPULATED! 🚀")
    print(f"==================================================")

if __name__ == '__main__':
    sync_faculty()
