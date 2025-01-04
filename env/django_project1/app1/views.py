from django.shortcuts import render,redirect,HttpResponse
from . models import Signup_data

def home(req):
    if req.method=="GET":
        return render(req,'index.html')
    else:
        name1=req.POST.get('nm')
        email1=req.POST.get('em')
        password1=req.POST.get('pw')
        ob=Signup_data(name=name1,email=email1,password=password1)
        ob.save()
        return HttpResponse("save")
    
def index(req):
    return render(req,'about.html',{})

def contact(req):
    return render(req, 'contact.html', {})

def head(req):
    return render(req,'head.html',{})
   