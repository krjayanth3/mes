from django.contrib import admin
from .models import (
    Department, FacultyMember, Announcement, GalleryImage, Committee,
    Topper, ContactInquiry, CampusFacility, QuickDownload, LeadershipProfile
)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'intake', 'duration', 'hod_name')
    prepopulated_fields = {'slug': ('code',)}
    search_fields = ('name', 'code', 'hod_name')

@admin.register(FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department', 'qualification', 'is_hod', 'order')
    list_filter = ('department', 'is_hod')
    search_fields = ('name', 'designation', 'qualification')
    list_editable = ('is_hod', 'order')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_important', 'is_ticker', 'publish_date')
    list_filter = ('category', 'is_important', 'is_ticker', 'publish_date')
    search_fields = ('title', 'content')
    list_editable = ('is_important', 'is_ticker')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category',)
    search_fields = ('title', 'caption')

@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'external_link')
    search_fields = ('name', 'description')

@admin.register(Topper)
class TopperAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'department', 'semester', 'percentage', 'year')
    list_filter = ('department', 'year')
    search_fields = ('student_name',)

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at', 'is_resolved')
    list_filter = ('is_resolved', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_resolved',)

@admin.register(CampusFacility)
class CampusFacilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_class')

@admin.register(QuickDownload)
class QuickDownloadAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file', 'external_link', 'order', 'is_active', 'created_at')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'category')

@admin.register(LeadershipProfile)
class LeadershipProfileAdmin(admin.ModelAdmin):
    list_display = ('role_type', 'name', 'honorific', 'title', 'is_active')
    list_filter = ('role_type', 'is_active')
    search_fields = ('name', 'title', 'message')
    list_editable = ('is_active',)
