from django.shortcuts import render
from django.http import request
from Bank import bank,data
"""
this is the function to do the mvc/mvt
"""

def home(request):
    print("thanks")
    return render(request,'elijah.html')


def add(request):
    email=request.GET.get("email")
    print(email)
    print("this is value of email")
    
    name="elijah"
    return render(request,'register.html',{'names':name})
def man(request):
    print("this is another function")
    return render(request, "main.html")