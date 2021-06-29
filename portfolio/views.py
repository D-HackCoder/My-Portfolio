from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'index.html')

def Contact(request):
    return render(request,'Contact.html')

def Projects(request):
    return render(request,'Projects.html')

def Skills(request):
    return render(request,'Skills.html')

def Education(request):
    return render(request,'Education.html')

