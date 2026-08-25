import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mes_polytechnic.settings')
django.setup()

from website.models import LeadershipProfile, LeadershipRole

def run():
    print("--- Seeding Leadership & Founder Profiles ---")
    
    os.makedirs('media/leadership', exist_ok=True)
    source_img = os.path.join('resources', 'college.jpg')

    # Founder Profile
    founder, created = LeadershipProfile.objects.get_or_create(
        role_type=LeadershipRole.FOUNDER,
        defaults={
            'honorific': 'Poojyasri',
            'name': 'Sri T.V. Venkataswamy',
            'title': 'Ex. M.L.C | Founder, Madhugiri Education Society (R)',
            'message': 'Technical education is the bedrock of rural and regional development. M.E.S. Polytechnic was envisioned to deliver top-quality diploma engineering education to empower youth with practical skills and ethical values.',
            'order': 1,
            'is_active': True
        }
    )
    if os.path.exists(source_img):
        target_name = "founder_tvv.jpg"
        target_path = os.path.join('media', 'leadership', target_name)
        shutil.copy(source_img, target_path)
        founder.photo = f"leadership/{target_name}"
        founder.save()
        print(f"Updated Founder photo: {founder.photo}")

    # Principal Profile
    principal, created = LeadershipProfile.objects.get_or_create(
        role_type=LeadershipRole.PRINCIPAL,
        defaults={
            'honorific': 'Prof.',
            'name': 'Principal, M.E.S. Polytechnic',
            'title': 'M.E.S. Polytechnic, Madhugiri &bull; Code: 347',
            'message': 'At M.E.S. Polytechnic, we emphasize practical learning, skill workshops, disciplined academic rigor, and active industry participation so that every diploma graduate steps out with confidence and high competence.',
            'order': 2,
            'is_active': True
        }
    )
    if os.path.exists(source_img):
        target_name = "principal_desk.jpg"
        target_path = os.path.join('media', 'leadership', target_name)
        shutil.copy(source_img, target_path)
        principal.photo = f"leadership/{target_name}"
        principal.save()
        print(f"Updated Principal photo: {principal.photo}")

    print("--- Leadership Seeding Completed! ---")

if __name__ == '__main__':
    run()
