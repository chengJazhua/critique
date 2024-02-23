from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, "login/home.html") #issue here

def logout_view(request):
    logout(request)
    return redirect("/")