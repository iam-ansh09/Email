from unicodedata import name
from django.shortcuts import render,HttpResponse
from datetime import datetime
from Event.models import Email
# Create your views here.
def index(request):
    dictV={}
    if request.method== "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        toMail = request.POST.get('toMail')
        fromMail = request.POST.get('fromMail')
        mail = Email(name=name, roll=roll, phone=phone, email=email, date=datetime.today(),toMail=toMail,fromMail=fromMail)
        mail.save()
        dictV['status'] = 'success'
        dictV['message'] = 'Your Submission Was Recorder'
    return render(request, 'index.html',dictV)