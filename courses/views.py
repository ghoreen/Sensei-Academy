from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Sensei Academy 🎓</h1><p>Learn to draw anime.</p>")