from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PhoneModelForm
from .models import PhoneModel
# Create your views here.
def first_view(request):
    templates="layout.html"
    context={}
    return render(request, templates, context)

def addPhone(request):
    form = PhoneModelForm()
    if request.method == "POST":
        form = PhoneModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show-phone")
            return HttpResponse("Phone Added")
    templates_name ="PhoneHub/Form.html"
    context = {"form":form}
    return render(request, templates_name, context)

def updatePhone(request,i):
    phone_object = PhoneModel.objects.get(id=i)
    form = PhoneModelForm(instance=phone_object)
    if request.method == "POST":
        form = PhoneModelForm(request.POST,instance=phone_object)
        if form.is_valid():
            form.save()
            return redirect("show-phone")
            return HttpResponse("Phone Update")
    templates_name ="PhoneHub/Form.html"
    context = {"form":form}
    return render(request, templates_name, context)

def deletePhone(request,i):
    Phone_object = PhoneModel.objects.get(id=i)
    Phone_object.delete()
    return redirect("show-phone")
    return HttpResponse("Phone Delete")

def showPhone(request):
    Phone_object_qs = PhoneModel.objects.all()
    templates_name ="PhoneHub/show.html"
    context = {"Phone_object_qs":Phone_object_qs}
    return render(request, templates_name, context)
