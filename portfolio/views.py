from django.shortcuts import render , redirect , HttpResponse

# Create your views here.
def home():
    return render(request , 'home.html')
