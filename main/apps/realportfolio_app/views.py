from django.shortcuts import render

# Create your views here.

def index(request):
    print "Home"
    return render(request, 'realportfolio_app/index.html')

def projects(request):
    print "Projects"
    return render(request, 'realportfolio_app/project.html')

def aboutme(request):
    print "About Me"
    return render(request, 'realportfolio_app/about.html')

def testimonials(request):
    print "Testimonials"
    return render(request, 'realportfolio_app/testimonials.html')