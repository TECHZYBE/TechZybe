from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        msgs=request.POST["message"]
        Contact_details.objects.create(name=name,email=email,subject=subject,message=msgs).save()
        messages.success(request, "Your message has been sent")
        
        return JsonResponse({"status":"OK"})