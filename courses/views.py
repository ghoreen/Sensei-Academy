from django.shortcuts import render


def home(request):
    courses_list = [
        'أساسيات Python',
        'تطوير الويب باستخدام Django',
        'قواعد البيانات SQLite & PostgreSQL',
        'بناء الـ APIs بـ Django REST Framework',
    ]

    context = {
        'title': 'أهلاً بك في أكاديمية سينسي!',
        'courses': courses_list,
    }
    return render(request, 'courses/home.html', context)


def about(request):
    return render(request, 'courses/about.html')