from django.shortcuts import render,redirect
from django.http import HttpResponse
from userapp.models import User,Restaurant,Category

def signup(request):
  if request.method=="POST":
    name = request.POST.get("a")
    email = request.POST.get("b")
    mobile = request.POST.get("c")
    password = request.POST.get("d")
    
    User.objects.create(
      name = name,
      email = email,
      mobile = mobile,
      password=password
    )
    return redirect("login_link")
  return render(request,"userapp/signup.html")


def login(request):
  if request.method=="POST":
    email = request.POST.get("a")
    password = request.POST.get("b")
    
    try:
      user = User.objects.get(email=email)
      if user.email==email and user.password==password:
        request.session["USERID"] = user.id
        request.session["EMAIL"] = user.email
        request.session["NAME"] = user.name
        return redirect("dashboard_link")
        return HttpResponse("Login success")
      else:
        return HttpResponse("Invalid Credentials")
    except User.DoesNotExist:
      return HttpResponse("First Register Account")
    except User.MultipleObjectsReturned:
      return HttpResponse("Multiple Data Found")
  return render(request,"userapp/login.html")

def dashboard(request):
  if "USERID" not in request.session:
    return redirect("login_link")

  restaurants=Restaurant.objects.filter(is_active=True)
  categories=Category.objects.all()

  context={
    "username":request.session.get("NAME"),
    "categories":categories,
    "restaurants":restaurants

  }
  return render(request,"userapp/dashboard.html",context)    

    
