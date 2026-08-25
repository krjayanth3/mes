import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mes_polytechnic.settings')
django.setup()

from django.contrib.auth.models import User
from website.models import (
    Department, Announcement, AnnouncementCategory,
    GalleryImage, GalleryCategory, Committee, Topper, CampusFacility
)

def run():
    print("--- Seeding MES Polytechnic Database ---")

    # 1. Admin User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@mespolytechnic.in', 'admin123')
        print("Created superuser 'admin' with password 'admin123'")
    else:
        print("Superuser 'admin' already exists.")

    # 2. Departments
    departments_data = [
        {
            'name': 'Computer Science & Engineering',
            'code': 'CSE',
            'icon_class': 'fa-laptop-code',
            'short_description': 'Empowering students with cutting-edge software development, AI, networking, and cloud computing skills.',
            'description': 'The Computer Science Engineering department at M.E.S. Polytechnic provides a robust foundation in software engineering, programming in C, Python, Java, web technologies, database management systems, hardware maintenance, and network security. Equipped with modern computer labs and high-speed internet connection, students receive extensive hands-on experience.',
            'intake': 60,
            'duration': '3 Years (6 Semesters)',
            'hod_name': 'Prof. Ramesh K. S.',
            'hod_qualification': 'M.Tech in Computer Science',
            'hod_message': 'Our mission is to nurture technical brilliance and problem-solving skill sets in students, turning them into competent software professionals and innovative technologists ready for modern industry requirements.',
            'lab_facilities': "Software Engineering & Web Technologies Lab\nDatabase Management Systems (DBMS) Lab\nData Structures & Python Programming Lab\nComputer Hardware & Networking Lab\nCloud Computing & Cyber Security Lab"
        },
        {
            'name': 'Electronics & Communication Engineering',
            'code': 'ECE',
            'icon_class': 'fa-microchip',
            'short_description': 'Pioneering training in microprocessors, embedded systems, telecommunication, and digital signal processing.',
            'description': 'The Department of Electronics and Communication Engineering prepares diploma engineers to design, innovate, and test electronic devices and communication networks. The curriculum covers analog and digital electronics, microcontroller programming, IoT applications, and signal processing.',
            'intake': 60,
            'duration': '3 Years (6 Semesters)',
            'hod_name': 'Prof. Suresh Kumar V.',
            'hod_qualification': 'M.Tech in Digital Electronics',
            'hod_message': 'Electronics powers modern technological breakthroughs. We focus on hands-on hardware prototyping and embedded software skills to equip our graduates for top electronics manufacturing and telecom companies.',
            'lab_facilities': "Analog Electronics & Circuitry Lab\nDigital Electronics & Microcontroller Lab\nEmbedded Systems & IoT Innovation Lab\nCommunication Engineering & Optical Fiber Lab\nVLSI & Printed Circuit Board (PCB) Lab"
        },
        {
            'name': 'Mechanical Engineering',
            'code': 'ME',
            'icon_class': 'fa-cogs',
            'short_description': 'Core engineering discipline focusing on manufacturing, thermal systems, CAD/CAM design, and robotics.',
            'description': 'The Mechanical Engineering department at M.E.S. Polytechnic is one of the foundational departments, boasting extensive workshop machinery, CNC centers, fluid power systems, and thermal engineering labs. Students gain mastery in engineering graphics, CAD modeling, machine maintenance, and modern manufacturing technology.',
            'intake': 60,
            'duration': '3 Years (6 Semesters)',
            'hod_name': 'Prof. Manjunath N.',
            'hod_qualification': 'M.Tech in Machine Design',
            'hod_message': 'Mechanical engineering remains the backbone of industrial growth. We instil practical craftsmanship, CAD design mastery, and analytical rigour in every student.',
            'lab_facilities': "Machine Shop & Fitting Workshop\nFoundry & Forging Practice Shop\nCAD/CAM & 3D Prototyping Lab\nThermal Engineering & Hydraulics Lab\nStrength of Materials & Testing Lab"
        },
        {
            'name': 'Civil Engineering',
            'code': 'CE',
            'icon_class': 'fa-drafting-compass',
            'short_description': 'Building tomorrow through structural design, surveying, environmental engineering, and construction management.',
            'description': 'Civil Engineering forms the foundation of modern infrastructure. At M.E.S. Polytechnic, students master land surveying using Total Station & GPS, structural drafting, concrete technology, soil mechanics, and highway engineering.',
            'intake': 60,
            'duration': '3 Years (6 Semesters)',
            'hod_name': 'Prof. Shivashankar M.',
            'hod_qualification': 'M.Tech in Structural Engineering',
            'hod_message': 'We train our students to build resilient, sustainable infrastructure that serves communities for generations. Fieldwork and Total Station surveying are key pillars of our program.',
            'lab_facilities': "Advanced Surveying & Total Station Lab\nMaterial Testing & Concrete Technology Lab\nGeotechnical & Soil Mechanics Lab\nAutoCAD Drafting & Building Design Lab\nEnvironmental Engineering & Quality Testing Lab"
        },
        {
            'name': 'Electrical & Electronics Engineering',
            'code': 'EEE',
            'icon_class': 'fa-bolt',
            'short_description': 'Powering the future with power systems, electric vehicles, renewable energy, and industrial automation.',
            'description': 'The EEE department provides rigorous instruction in electrical machinery, power generation and distribution, control systems, electric motor drives, solar renewable energy installations, and industrial automation PLC controls.',
            'intake': 60,
            'duration': '3 Years (6 Semesters)',
            'hod_name': 'Prof. Ananda V.',
            'hod_qualification': 'M.Tech in Power Systems',
            'hod_message': 'With the revolution in electric vehicles and green energy, electrical engineers are in high demand. We provide practical experience on electrical transformers, motor test-benches, and solar panels.',
            'lab_facilities': "AC/DC Electrical Machines Lab\nPower Electronics & PLC Control Lab\nElectrical Wiring & Installation Workshop\nRenewable Energy & Solar Testing Lab\nCircuit Theory & Measurements Lab"
        }
    ]

    dept_objs = {}
    for d in departments_data:
        obj, created = Department.objects.get_or_create(
            code=d['code'],
            defaults=d
        )
        dept_objs[d['code']] = obj
        if not created:
            for key, val in d.items():
                setattr(obj, key, val)
            obj.save()
        print(f"Processed Department: {obj.name}")

    # 3. Announcements
    announcements_list = [
        {
            'title': 'Diploma Semester Examination Fee Notification Nov-Dec 2025',
            'category': AnnouncementCategory.EXAM,
            'content': 'All regular and repeater diploma students are hereby informed to pay their November-December 2025 examination fees before the deadline. Online portal is open at DTE portal.',
            'is_important': True,
            'is_ticker': True,
            'link': 'https://dtek.karnataka.gov.in/'
        },
        {
            'title': 'Academic Calendar for Regular Diploma Programmes 2025-26',
            'category': AnnouncementCategory.ACADEMIC,
            'content': 'DTE Karnataka has released the official Academic Calendar for all regular diploma courses for the academic year 2025-26. Classes commence as per scheduled timeline.',
            'is_important': True,
            'is_ticker': True,
            'link': 'https://www.mespolytechnic.in/'
        },
        {
            'title': 'Implementation of C25 Diploma Curriculum - GO & Official Memo',
            'category': AnnouncementCategory.CIRCULAR,
            'content': 'Government Order and Official Memorandum regarding the new Outcome-Based C25 Diploma Curriculum introduced across technical polytechnics in Karnataka.',
            'is_important': True,
            'is_ticker': True,
        },
        {
            'title': 'Yuvanidhi Yojana Registration for Final Year Diploma Graduates',
            'category': AnnouncementCategory.ADMISSION,
            'content': 'Eligible passing-out diploma students can register for Yuvanidhi Scheme financial aid through Seva Sindhu portal. Check circular for required document checklist.',
            'is_important': False,
            'is_ticker': True,
        },
        {
            'title': 'Mandatory Creation of Student APAAR ID (Automated Permanent Academic Account Registry)',
            'category': AnnouncementCategory.CIRCULAR,
            'content': 'All registered students must create their APAAR ID linked with ABC (Academic Bank of Credits) portal. Contact HOD or department coordinators for assistance.',
            'is_important': True,
            'is_ticker': True,
        },
        {
            'title': 'Annual Campus Placement Drive 2025-26 Announcement',
            'category': AnnouncementCategory.EVENT,
            'content': 'Top engineering & industrial firms will conduct campus recruitment drives for final year Civil, Mechanical, ECE, CSE & EEE students. Pre-placement training begins next Monday.',
            'is_important': True,
            'is_ticker': False,
        }
    ]

    for ann in announcements_list:
        obj, created = Announcement.objects.get_or_create(
            title=ann['title'],
            defaults=ann
        )
        print(f"Processed Announcement: {ann['title']}")

    # 4. Committees
    committees_list = [
        {'name': 'Grievance Committee', 'code': 'GC', 'description': 'Responsible for student and institutional grievance handling and welfare.'},
        {'name': 'Grievance Redressal Committee', 'code': 'GRC', 'description': 'AICTE mandated committee to ensure transparent resolution of staff and student concerns.'},
        {'name': 'Anti-Ragging Committee', 'code': 'ARC', 'description': 'Enforces zero-tolerance anti-ragging policy across the campus and student hostels.'},
        {'name': 'SC / ST Committee & Cell', 'code': 'SCST', 'description': 'Promotes empowerment, scholarships, and academic support for SC/ST category students.'},
        {'name': 'Internal Compliance Committee', 'code': 'ICC', 'description': 'Provides safe and equal gender environment, preventing harassment.'},
        {'name': 'Internal Quality Assurance Cell', 'code': 'IQAC', 'description': 'Monitors and maintains high standards in technical pedagogy and campus infrastructure.'},
        {'name': 'Industry - Institution Interaction Cell', 'code': 'IIC', 'description': 'Facilitates industrial visits, expert guest lectures, internships, and campus placements.'},
    ]

    for c in committees_list:
        Committee.objects.get_or_create(name=c['name'], defaults=c)
        print(f"Processed Committee: {c['name']}")

    # 5. Toppers
    toppers_data = [
        {'student_name': 'Chandan D', 'dept_code': 'CSE', 'semester': '1st Semester', 'percentage': 90.33, 'year': '2024-2025'},
        {'student_name': 'Pavithra N', 'dept_code': 'ECE', 'semester': '1st Semester', 'percentage': 90.16, 'year': '2024-2025'},
        {'student_name': 'Rajashekhar', 'dept_code': 'ECE', 'semester': '1st Semester', 'percentage': 89.33, 'year': '2024-2025'},
        {'student_name': 'Kemparaju', 'dept_code': 'EEE', 'semester': '1st Semester', 'percentage': 88.83, 'year': '2024-2025'},
        {'student_name': 'Subramanyam T S', 'dept_code': 'ME', 'semester': '3rd Semester', 'percentage': 86.62, 'year': '2024-2025'},
        {'student_name': 'Brunda M', 'dept_code': 'CE', 'semester': '5th Semester', 'percentage': 85.25, 'year': '2024-2025'},
    ]

    for t in toppers_data:
        dept = dept_objs.get(t['dept_code'])
        if dept:
            Topper.objects.get_or_create(
                student_name=t['student_name'],
                department=dept,
                semester=t['semester'],
                defaults={'percentage': t['percentage'], 'year': t['year']}
            )
            print(f"Processed Topper: {t['student_name']}")

    # 6. Campus Facilities
    facilities_data = [
        {
            'title': 'Hi-Tech Computer Laboratories',
            'description': 'Equipped with high-performance desktop computers, optical fiber internet leased line, software development IDEs, and network simulators.',
            'icon_class': 'fa-desktop'
        },
        {
            'title': 'Heavy Mechanical & Civil Workshops',
            'description': 'Includes CNC lathes, milling machines, universal testing machines (UTM), total stations, and fluid hydraulics test benches.',
            'icon_class': 'fa-gears'
        },
        {
            'title': 'Central Library & Learning Resource Center',
            'description': 'Features over 15,000 reference volumes, technical journals, e-books access, and quiet reading zones for students.',
            'icon_class': 'fa-book-open'
        },
        {
            'title': 'Advanced Electronics & IoT Lab',
            'description': 'Equipped with digital storage oscilloscopes, microprocessor kits, sensor modules, and soldering stations.',
            'icon_class': 'fa-microchip'
        },
        {
            'title': 'Auditorium & Conference Hall',
            'description': '300+ seating capacity air-conditioned hall for technical symposiums, guest lectures, cultural festivals, and seminars.',
            'icon_class': 'fa-users'
        },
        {
            'title': 'Sports Complex & Playground',
            'description': 'Spacious athletic track, cricket field, volleyball court, shuttle badminton courts, and indoor games facilities.',
            'icon_class': 'fa-trophy'
        }
    ]

    for f in facilities_data:
        CampusFacility.objects.get_or_create(title=f['title'], defaults=f)
        print(f"Processed Facility: {f['title']}")

    # 7. Sample Gallery Entries
    gallery_items = [
        {'title': 'MES Polytechnic Main Administrative Block', 'category': GalleryCategory.CAMPUS, 'caption': 'Front view of the institution campus located at Madhugiri.'},
        {'title': 'Advanced Computer Science Engineering Lab', 'category': GalleryCategory.LABS, 'caption': 'Students working on programming and database management modules.'},
        {'title': 'Mechanical Engineering Machine Shop', 'category': GalleryCategory.LABS, 'caption': 'Hands-on practical machining session on lathe and milling tools.'},
        {'title': 'Civil Engineering Surveying Fieldwork', 'category': GalleryCategory.ACADEMICS, 'caption': 'Students performing land surveying using Total Station equipment.'},
        {'title': 'Electronics Hardware Prototyping Session', 'category': GalleryCategory.LABS, 'caption': 'Breadboard testing and microcontroller programming practice.'},
        {'title': 'Annual Sports Day Celebration', 'category': GalleryCategory.SPORTS, 'caption': 'Student athletics and inter-department sports tournament.'},
        {'title': 'Technical Project Exhibition & Expo', 'category': GalleryCategory.EVENTS, 'caption': 'Final year diploma student working projects showcase.'},
        {'title': 'Industrial Visit & Site Inspection', 'category': GalleryCategory.ACADEMICS, 'caption': 'Faculty guided student field trip to major power and manufacturing plant.'},
    ]

    for g in gallery_items:
        GalleryImage.objects.get_or_create(title=g['title'], defaults=g)
        print(f"Processed Gallery Item: {g['title']}")

    print("--- Seeding Completed Successfully! ---")

if __name__ == '__main__':
    run()
