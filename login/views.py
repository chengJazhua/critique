from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
# Create your views here.

@receiver(user_logged_in)
def redirect_after_google_login(sender, request, user, **kwargs):
    print(f"Signal received from {sender}")
    # Check if the user is in the "site admin" group
    if user.groups.filter(name='site admin').exists():
        print(f"I am an admin")
        # Redirect to the admin landing page
        return redirect('adminlanding/')
    else:
        print(f"I am a user")
        # Redirect to the user landing page
        return redirect('userlanding/')

def home(request):
    return render(request, "login/home.html") #issue here

def logout_view(request):
    logout(request)
    return redirect("/")

def user_landing_view(request):
    ## retrieve user's name through database lookup
    name = "name"
    return render(
        request, 
        "user_landing_page.html", 
    )

def admin_landing_view(request):
    return render(
        request, 
        "admin_landing_page.html",
    )