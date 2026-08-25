import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mes_polytechnic.settings')
django.setup()

from django.test import Client
from website.models import Announcement, GalleryImage, FacultyMember, Topper, QuickDownload, Department

client = Client()

# Authenticate client
client.login(username='admin', password='admin123')

dept = Department.objects.first()
ann = Announcement.objects.first()
gal = GalleryImage.objects.first()
fac = FacultyMember.objects.first()
top = Topper.objects.first()
dl = QuickDownload.objects.first()

routes = [
    '/',
    '/about/',
    '/departments/',
    '/departments/cse/',
    '/departments/ce/',
    '/departments/sh/',
    '/faculty/',
    '/notices/',
    '/gallery/',
    '/contact/',
    '/staff-dashboard/',
    f'/staff-dashboard/department/edit/{dept.id}/',
    f'/staff-dashboard/announcement/edit/{ann.id}/',
    f'/staff-dashboard/gallery/edit/{gal.id}/',
    f'/staff-dashboard/faculty/edit/{fac.id}/',
    f'/staff-dashboard/topper/edit/{top.id}/',
    f'/staff-dashboard/download/edit/{dl.id}/',
]

print("--- Testing MES Polytechnic Administration Routes ---")
all_passed = True
for url in routes:
    response = client.get(url)
    if response.status_code == 200:
        print(f"[OK 200] {url}")
    else:
        print(f"[FAIL {response.status_code}] {url}")
        all_passed = False

if all_passed:
    print("\nALL ADMINISTRATION & CONTENT ROUTES TESTED SUCCESSFULLY WITH HTTP 200 OK!")
else:
    print("\nSOME ROUTES FAILED!")
