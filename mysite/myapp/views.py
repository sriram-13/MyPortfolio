from django.shortcuts import render_to_response
from .models import Experience, Responsibility, Recommendations, Skillset, Skills, Home, HomeImage, Contact
import datetime

# Create your views here.

def home(request):
    qset = Home.objects.all()
    return render_to_response('home.html', {'qset': qset})

def skillset(request):
    qset = Skillset.objects.all()
    return render_to_response('skillset.html', {'qset': qset})

def recommendations(request):
    qset = Recommendations.objects.all()
    return render_to_response('recommendations.html', {'qset': qset})

def experience(request):
    current_date = datetime.datetime.now()
    qset = Experience.objects.all().order_by('-to_date')
    return render_to_response('experience.html', {'qset': qset})
#Add a attribute to Experience model named current_role of type BooleanField from which decision to whether update to_date or not with current date will be made.

def contact(request):
    qset = Contact.objects.all()
    return render_to_response('contact.html', {'qset': qset})