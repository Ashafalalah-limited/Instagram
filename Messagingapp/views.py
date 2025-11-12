from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact.html')
    
def help(request):
    return render(request,'help.html')    