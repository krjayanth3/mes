from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('departments/', views.departments_view, name='departments'),
    path('departments/<slug:slug>/', views.department_detail_view, name='department_detail'),
    path('faculty/', views.faculty_view, name='faculty'),
    path('notices/', views.notices_view, name='notices'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.staff_login_view, name='login'),
    path('logout/', views.staff_logout_view, name='logout'),
    path('staff-dashboard/', views.staff_dashboard_view, name='staff_dashboard'),
    
    # Department Edit/Delete
    path('staff-dashboard/department/edit/<int:pk>/', views.edit_department_view, name='edit_department'),
    path('staff-dashboard/department/delete/<int:pk>/', views.delete_department_view, name='delete_department'),

    # Announcement Edit/Delete
    path('staff-dashboard/announcement/edit/<int:pk>/', views.edit_announcement_view, name='edit_announcement'),
    path('staff-dashboard/announcement/delete/<int:pk>/', views.delete_announcement_view, name='delete_announcement'),
    
    # Gallery Edit/Delete
    path('staff-dashboard/gallery/edit/<int:pk>/', views.edit_gallery_view, name='edit_gallery'),
    path('staff-dashboard/gallery/delete/<int:pk>/', views.delete_gallery_view, name='delete_gallery'),
    
    # Faculty Edit/Delete
    path('staff-dashboard/faculty/edit/<int:pk>/', views.edit_faculty_view, name='edit_faculty'),
    path('staff-dashboard/faculty/delete/<int:pk>/', views.delete_faculty_view, name='delete_faculty'),
    
    # Academic Achiever / Topper Edit/Delete
    path('staff-dashboard/topper/edit/<int:pk>/', views.edit_topper_view, name='edit_topper'),
    path('staff-dashboard/topper/delete/<int:pk>/', views.delete_topper_view, name='delete_topper'),

    # Quick Downloads Edit/Delete
    path('staff-dashboard/download/edit/<int:pk>/', views.edit_quick_download_view, name='edit_quick_download'),
    path('staff-dashboard/download/delete/<int:pk>/', views.delete_quick_download_view, name='delete_quick_download'),

    # Leadership / Founder Edit/Delete
    path('staff-dashboard/leadership/edit/<int:pk>/', views.edit_leadership_view, name='edit_leadership'),
    path('staff-dashboard/leadership/delete/<int:pk>/', views.delete_leadership_view, name='delete_leadership'),
]
