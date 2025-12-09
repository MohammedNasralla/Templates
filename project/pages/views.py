from django.shortcuts import render

def index(request):
    print("View index called")
    context = {
        'full_name': 'Mohammed Talal Nasralla',
        'student_id': '120212446',
        'address': 'Gaza',
        'email': 'mohammednasralla28@gmail.com',
        'mobile_number': '+972598698040'
    }
    return render(request, 'pages/index.html', context)



