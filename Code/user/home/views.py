from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from home.models import Contact


# Create your views here.
def home(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,"home.html")

def loginuser(request):
    if request.method=="POST":
         username=request.POST.get("username")
         password=request.POST.get("password")
         print(username,password)

         user = authenticate(username=username, password=password)

         if user is not None:
             # A backend authenticated the credentials
             login(request,user)
             return redirect("/")
    
         else:
             # A backend authenticated the credentials
            return render(request,"login.html")

    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        mail=request.POST.get("mail")
        age=request.POST.get("age")
        desc=request.POST.get("desc")
        contact=Contact(name=name, mail=mail, age=age, desc=desc)
        contact.save()
        messages.success(request, "Profile details updated.")
    return render(request,"contact.html")
