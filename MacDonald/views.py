from django.shortcuts import render
from Template import *

# Create your views here.

def HomeView(request):
    return render(request,'home.html')


def AboutView(request):
    return render(request,'about.html')


def MenuView(request):
    return render(request,'menu.html')


def BookTableView(request):
    return render(request,'booktable.html')


def BookTableView1(request):
    return render(request,'booktable.html')