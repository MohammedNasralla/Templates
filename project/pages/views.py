from django.shortcuts import render
from datetime import datetime

def index(request):
    print("View index called")
    context = {
        'first_name': 'mohammed',
        'last_name': 'nasralla',
        'student_id': 120212446,
        'address': 'gaza',
        'email': '',
        'mobile_number': '+972598698040',
        'date_of_birth': datetime(2003, 11, 28),
    }
    return render(request, 'pages/index.html', context)



