import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mes_polytechnic.settings')
django.setup()

from website.models import QuickDownload

def run():
    print("--- Seeding Quick Downloads ---")
    
    os.makedirs('media/downloads', exist_ok=True)
    
    # Create sample PDF files if not present
    sample_pdf_text = "%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj 3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Resources<<>>>>endobj\nxref\n0 4\n0000000000 65535 f\n0000000009 00000 n\n0000000052 00000 n\n0000000101 00000 n\ntrailer<</Size 4/Root 1 0 R>>\nstartxref\n178\n%%EOF"
    
    downloads_data = [
        {
            'title': 'Grievance Redressal Committee Report',
            'category': 'AICTE Mandatory',
            'filename': 'grievance_redressal_committee.pdf',
            'order': 1,
            'is_active': True,
        },
        {
            'title': 'Anti-Ragging Guidelines & Affidavit',
            'category': 'Campus Safety',
            'filename': 'anti_ragging_guidelines.pdf',
            'order': 2,
            'is_active': True,
        },
        {
            'title': 'SC / ST Cell & Welfare Manual',
            'category': 'Student Welfare',
            'filename': 'sc_st_cell_manual.pdf',
            'order': 3,
            'is_active': True,
        },
        {
            'title': 'Academic Calendar of Diploma Programmes 2025-26',
            'category': 'DTE Karnataka',
            'filename': 'academic_calendar_2025_26.pdf',
            'order': 4,
            'is_active': True,
        },
        {
            'title': 'C25 Outcome-Based Diploma Curriculum Memo',
            'category': 'Curriculum GO',
            'filename': 'c25_curriculum_memo.pdf',
            'order': 5,
            'is_active': True,
        }
    ]

    for item in downloads_data:
        file_path = os.path.join('media', 'downloads', item['filename'])
        with open(file_path, 'w') as f:
            f.write(sample_pdf_text)
            
        obj, created = QuickDownload.objects.get_or_create(
            title=item['title'],
            defaults={
                'category': item['category'],
                'file': f"downloads/{item['filename']}",
                'order': item['order'],
                'is_active': item['is_active']
            }
        )
        if not created:
            obj.file = f"downloads/{item['filename']}"
            obj.category = item['category']
            obj.order = item['order']
            obj.save()
        print(f"Processed Quick Download: {obj.title} -> {obj.file}")

    print("--- Quick Downloads Seeding Completed! ---")

if __name__ == '__main__':
    run()
