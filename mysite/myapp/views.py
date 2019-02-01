from django.shortcuts import render_to_response
from .models import Experience, Responsibility, Recommendations, Skillset, Skills, Home, HomeImage, Contact, ProfilePic
import datetime

# Create your views here.

profilepic = str()
profilepic_qset = ProfilePic.objects.all()
for x in profilepic_qset:
    temp = str(x.img)
    str1, str2, profilepic = temp.split('/')

def home(request):
    qset = Home.objects.all()
    return render_to_response('home.html', {'qset': qset, 'profilepic': profilepic})

def skillset(request):
    qset = Skillset.objects.all()
    return render_to_response('skillset.html', {'qset': qset, 'profilepic': profilepic})

def recommendations(request):
    qset = Recommendations.objects.all()
    return render_to_response('recommendations.html', {'qset': qset, 'profilepic': profilepic})

def experience(request):
    current_date = datetime.date.today()
    qset = Experience.objects.all().order_by('-to_date')
    return render_to_response('experience.html', {'qset': qset, 'profilepic': profilepic, 'current_date': current_date})
#Add a attribute to Experience model named current_role of type BooleanField from which decision to whether update to_date or not with current date will be made.

def contact(request):
    str3 = str()
    qset = Contact.objects.all()
    for x in qset:
        temp = str(x.contact_img)
        str1, str2, str3 = temp.split('/')
        query = x
    return render_to_response('contact.html', {'query': query, 'str3': str3, 'profilepic': profilepic})