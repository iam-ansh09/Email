from unicodedata import name
from django.shortcuts import render,HttpResponse
from datetime import datetime
from Event.models import Email,Question
# Create your views here.
def index(request):
    dictV={}
    try:
        question = Question.objects.all()[0].statement
    except:
        question = 'You Will Get The Question Soon'
    dictV['question']=question

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