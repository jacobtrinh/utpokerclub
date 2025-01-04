from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, 'utpokerapp/dashboard.html')

def membership(request):
    return render(request, 'utpokerapp/membership.html')

def activities(request):
    hosts = Host.objects.all()
    homegames = Home_Game.objects.all().order_by('-id')[:6]
    return render(request, 'utpokerapp/activities.html', {'hosts': hosts, 'homegames': homegames})

def contact(request):
    if request.method == "POST":
        contact =Contact()

        firstname=request.POST.get('firstname')
        if firstname.strip() == "":
            firstname = "None"

        lastname = request.POST.get('lastname')
        if lastname.strip() == "":
            lastname = "None"

        email= request.POST.get('email')
        subject = request.POST.get('subject')

        if firstname.strip() != "None" and lastname.strip() != "None" and subject != "":
            contact.firstname=firstname
            contact.lastname=lastname
            contact.email=email
            contact.subject=subject
            contact.save()
            return render(request, 'utpokerapp/dashboard.html')


    return render(request, 'utpokerapp/contact.html')


