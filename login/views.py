from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from login.models import Report
#from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.

@receiver(user_logged_in)
def redirect_after_google_login(sender, request, user, **kwargs):
    print(f"Signal received from {sender}")
    
    #return redirect('adminlanding/')
    if user.groups.filter(name='site admin').exists():
        print(f"I am an admin")
        return redirect('adminlanding/')
    else:
        print(f"I am a user")
        return redirect('userlanding/')


def home(request):
    return render(request, "login/home.html") #issue here

def logout_view(request):
    logout(request)
    return redirect("/")

def admin_view_reports(request):
    return render(request, "admin_view_reports.html")

def user_reports(request):
    return render(request, "user_reports.html")


def user_landing_view(request):
    ## retrieve user's name through database lookup
    print(f"requested user landing view")
    name = "name"
    return render(
        request, 
        "user_landing_page.html", 
    )


def admin_landing_view(request):
    print(f"requested admin landing view")
    return render(
        request, 
        "admin_landing_page.html",
    )

def report(request):
    if request.method == 'POST':
        '''image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
            if image_type == 'private':
                upload = UploadPrivate(file=image_file)
            else:
                upload = Upload(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'upload.html', {
            'image_url': image_url
        })'''
        userID = request.POST['userID']
        className = request.POST['className']
        professorName = request.POST['professorName']
        studentName = request.POST['studentName']
        rating = request.POST.get('rating')
        workType = request.POST.getlist('workType')
        fileLink = "temp"
        Report.objects.create(userID = userID, className = className, professorName = professorName, studentName = studentName, rating = rating, workType = workType, fileLink = fileLink)
        # TODO: upload file and error checking (make sure all inputs are valid)
        return render(
            request,
            "report_page.html"
            )
