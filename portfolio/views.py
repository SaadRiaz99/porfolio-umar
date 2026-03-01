from django.shortcuts import render , redirect , HttpResponse
from .models import Contact_message

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            Contact_message.objects.create(name=name, email=email, message=message)
            return render(request, 'home.html', {'success': True})
            
    return render(request , 'home.html')
