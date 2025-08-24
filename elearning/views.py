from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def course_list(request):
    return render(request, 'pages/course_list.html')

def course_detail(request, course_id):
    return render(request, 'pages/course_detail.html', {'course_id': course_id})

def c_login(request):
    return render(request, 'pages/login.html')
def c_register(request):
    return render(request, 'pages/register.html')
