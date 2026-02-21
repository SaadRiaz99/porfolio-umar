from django.shortcuts import render , requests , redirect

# Create your views here.
def home():
    return render(requests , "home.html")

