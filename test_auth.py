import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mes_polytechnic.settings')
django.setup()

from django.test import Client

client = Client()

print("--- Testing Staff Login & Dashboard ---")
login_response = client.post('/login/', {'username': 'admin', 'password': 'admin123'})
print(f"Login POST status code: {login_response.status_code} (Should redirect to /staff-dashboard/)")

dashboard_response = client.get('/staff-dashboard/')
print(f"Dashboard GET status code: {dashboard_response.status_code} (Should be 200 OK)")

if dashboard_response.status_code == 200 and "Welcome, admin" in dashboard_response.content.decode('utf-8'):
    print("STAFF DASHBOARD AUTHENTICATION AND RENDERING TEST PASSED!")
else:
    print("STAFF DASHBOARD TEST FAILED!")
