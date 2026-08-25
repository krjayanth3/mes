from .models import Announcement

def college_info(request):
    try:
        ticker_announcements = Announcement.objects.filter(is_ticker=True).order_by('-created_at')[:5]
    except Exception:
        ticker_announcements = []

    return {
        'COLLEGE_NAME': 'M.E.S. POLYTECHNIC',
        'SOCIETY_NAME': 'MADHUGIRI EDUCATION SOCIETY (R)',
        'INSTITUTION_CODE': '347',
        'APPROVAL_INFO': 'Recognized by Govt. of Karnataka & Approved by AICTE, New Delhi',
        'COLLEGE_ADDRESS': 'G.B.N Road, Madhugiri, Tumkur District, Karnataka - 572132',
        'COLLEGE_PHONE': '08137-295534',
        'COLLEGE_MOBILES': ['9448892708', '9972009329', '9448747848'],
        'COLLEGE_EMAIL': 'principalmespolytechnic@gmail.com',
        'COLLEGE_EMAIL_ALT': 'stvvmes@gmail.com',
        'FOUNDER_NAME': 'Poojyasri Sri T.V. Venkataswamy',
        'FOUNDER_TITLE': 'Ex. M.L.C',
        'COLLEGE_LOGO': '/static/images/college_logo.png',
        'DEV_TEAM_LOGO': '/static/images/abcx-logo.png',
        'DEV_COMPANY_NAME': 'ABCX',
        'DEV_COMPANY_URL': 'https://abcx.co.in/',
        'DEV_COMPANY_LEGAL': 'AlphaBeastCodeX Private Limited',
        'ticker_announcements': ticker_announcements,
    }
