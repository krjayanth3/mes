from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    icon_class = models.CharField(max_length=50, default='fa-laptop-code', help_text="FontAwesome icon class e.g. fa-laptop-code, fa-cogs, fa-bolt, fa-drafting-compass, fa-microchip")
    short_description = models.TextField()
    description = models.TextField()
    intake = models.PositiveIntegerField(default=60)
    duration = models.CharField(max_length=50, default="3 Years (6 Semesters)")
    hod_name = models.CharField(max_length=100, blank=True)
    hod_qualification = models.CharField(max_length=100, blank=True)
    hod_message = models.TextField(blank=True)
    lab_facilities = models.TextField(help_text="Bullet points or newline separated list of labs", blank=True)
    image = models.ImageField(upload_to='departments/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.code)
        
        # Auto-assign icon class based on branch code
        code_upper = self.code.upper() if self.code else ''
        if 'CS' in code_upper:
            self.icon_class = 'fa-laptop-code'
        elif 'EC' in code_upper:
            self.icon_class = 'fa-microchip'
        elif 'ME' in code_upper:
            self.icon_class = 'fa-cogs'
        elif 'CE' in code_upper or 'CIVIL' in code_upper:
            self.icon_class = 'fa-trowel-bricks'
        elif 'EE' in code_upper:
            self.icon_class = 'fa-bolt'
        elif 'SH' in code_upper or 'SCIENCE' in code_upper:
            self.icon_class = 'fa-atom'
        elif not self.icon_class:
            self.icon_class = 'fa-graduation-cap'
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.code})"

class FacultyMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, help_text="e.g. Head of Department, Senior Lecturer, Selection Grade Lecturer")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculty_members')
    qualification = models.CharField(max_length=150, help_text="e.g. M.Tech, B.E., Ph.D.")
    experience = models.CharField(max_length=50, blank=True, help_text="e.g. 10+ Years")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='faculty/', blank=True, null=True)
    is_hod = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.designation} ({self.department.code})"

class AnnouncementCategory(models.TextChoices):
    ACADEMIC = 'ACADEMIC', 'Academic'
    EXAM = 'EXAM', 'Examination'
    CIRCULAR = 'CIRCULAR', 'Official Circular'
    ADMISSION = 'ADMISSION', 'Admissions'
    EVENT = 'EVENT', 'News & Event'
    GENERAL = 'GENERAL', 'General Notice'

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=AnnouncementCategory.choices, default=AnnouncementCategory.GENERAL)
    content = models.TextField(blank=True)
    document = models.FileField(upload_to='announcements/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_important = models.BooleanField(default=False)
    is_ticker = models.BooleanField(default=True, help_text="Show in running notification ticker")
    publish_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date', '-created_at']

    def __str__(self):
        return f"[{self.category}] {self.title}"

class GalleryCategory(models.TextChoices):
    CAMPUS = 'CAMPUS', 'Campus Infrastructure'
    LABS = 'LABS', 'Laboratories & Workshops'
    EVENTS = 'EVENTS', 'Events & Celebrations'
    SPORTS = 'SPORTS', 'Sports & Cultural'
    ACADEMICS = 'ACADEMICS', 'Academic Activities'

class GalleryImage(models.Model):
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=GalleryCategory.choices, default=GalleryCategory.CAMPUS)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title

class Committee(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    pdf_file = models.FileField(upload_to='committees/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Topper(models.Model):
    student_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='toppers')
    semester = models.CharField(max_length=50, help_text="e.g. 1st Sem, 3rd Sem, 5th Sem")
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.CharField(max_length=50, default="2024-2025")
    photo = models.ImageField(upload_to='toppers/', blank=True, null=True)

    class Meta:
        ordering = ['-percentage']

    def __str__(self):
        return f"{self.student_name} ({self.department.code}) - {self.percentage}%"

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d')})"

class CampusFacility(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default="fa-building")
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)

    def __str__(self):
        return self.title

class QuickDownload(models.Model):
    title = models.CharField(max_length=200, help_text="Document title, e.g. Grievance Redressal Committee Report")
    category = models.CharField(max_length=100, default="AICTE & DTE Document", help_text="Category badge or brief tag")
    file = models.FileField(upload_to='downloads/', blank=True, null=True, help_text="Upload PDF or document file")
    external_link = models.URLField(blank=True, null=True, help_text="Or enter an external link if no file is uploaded")
    order = models.PositiveIntegerField(default=0, help_text="Display priority order")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

class LeadershipRole(models.TextChoices):
    FOUNDER = 'FOUNDER', 'Founder / Poojyasri Desk'
    PRINCIPAL = 'PRINCIPAL', 'Principal Desk'
    PRESIDENT = 'PRESIDENT', 'President / Management Desk'
    SECRETARY = 'SECRETARY', 'Secretary Desk'

class LeadershipProfile(models.Model):
    role_type = models.CharField(max_length=20, choices=LeadershipRole.choices, default=LeadershipRole.FOUNDER, unique=True)
    honorific = models.CharField(max_length=50, default="Poojyasri", blank=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, help_text="e.g. Ex. M.L.C | Founder, Madhugiri Education Society (R)")
    message = models.TextField(help_text="Vision quote or message to students")
    photo = models.ImageField(upload_to='leadership/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'role_type']

    def __str__(self):
        return f"{self.get_role_type_display()} - {self.name}"
