from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def registerview(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    template_name = "AuthApp/register.html"
    context = {"form":form}
    return render(request,template_name, context)

def loginview (request):
    if request.method == "POST":
        u = request.POST["un"]
        p = request.POST["pw"]
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect("show-phone")

        else:
            messages.error(request, 'Invalid Credentials')
    template_name = "AuthApp/login.html"
    context ={}
    return render(request, template_name, context)

def logoutview(request):
    logout(request)
    return redirect("login")