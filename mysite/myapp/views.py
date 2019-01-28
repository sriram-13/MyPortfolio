from django.shortcuts import render_to_response
from .models import Experience, Responsibility
import datetime

# Create your views here.

def recommendations(request):
    return render_to_response('recommendations.html')

def experience(request):
    current_date = datetime.datetime.now()
    qset = Experience.objects.all().order_by('-to_date')
    return render_to_response('experience.html', {'qset': qset})
#Add a attribute to Experience model named current_role of type BooleanField from which decision to whether update to_date or not with current date will be made.
