from django.shortcuts import render


def home(request):
    courses_list = [
        'أساسيات الرسم',
         'تطوير مهاراتك في الرسم',
         'شروحات وامثله ',
        'اساتذه مختصين في مجال رسم الانمي اضافه الى ارشادات مهمه',
    ]

    context = {
        'title': 'أهلاً بك في أكاديمية سينسي!',
        'courses': courses_list,
    }
    return render(request, 'courses/home.html', context)


def about(request):
    return render(request, 'courses/about.html')