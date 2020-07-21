from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def cv(request):
    return render(request, 'portfolio/cv.html')


def hire_me(request):
    return render(request, 'portfolio/hire-me.html')
