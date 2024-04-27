from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from login.models import Report, Evidence
#from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
from .forms import ReportForm

from django.template.defaulttags import register

@register.filter(name='isjpg')
def split(value): 
 
    ext = value.split(".")[-1]
    return ext == '.jpg'

# Create your views here.
class DocumentCreateView(CreateView):
    model = Evidence
    fields = ['upload', ]
    success_url = '/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Evidence.objects.all()
        context['documents'] = documents
        return context

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
    return render(request, "login/home.html") 

def logout_view(request):
    logout(request)
    return redirect("/")

def admin_view_reports(request):
    return render(request, "admin_view_reports.html")

def public_reports(request):
    if request.method == "POST":
        search = request.POST.get('search')
        public_reports = Report.objects.filter(private=False)
        if search == "":
            return render(request, "public_reports.html", {"reports": public_reports})
        public_reports = public_reports.filter(Q(userID__icontains=search) | Q(className__icontains=search) | Q(professorName__icontains=search) | Q(studentName__icontains=search) | Q(professor_email__icontains=search))
        public_reports.filter(private=False)
        return render(request, "public_reports.html", {"reports": public_reports})
    
    public_reports = Report.objects.filter(private=False)
    return render(request, "public_reports.html", {"reports": public_reports})

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
        try:
            evidence = Evidence(upload=request.FILES['filename'])
            fileLink = evidence.upload.url
            evidence.save()
        except Exception as e:
            fileLink=""
            # return render(
            #     request,
            #     "report_page.html",
            #     {
            #         "error_message": "You are missing one or more fields",
            #     },
            #     )
        userID = request.POST['userID']
        className = request.POST['className']
        professorName = request.POST['professorName']
        studentName = request.POST['studentName']
        rating = request.POST.get('rating')
        workType = request.POST.get('workType')
        professor_email = request.POST['professor_email']
        email_prof = request.POST.get('email_prof')
        report = request.POST['report']
        privacy = request.POST.get('privacy')
        status = "New"
        feedback = ""
        
        print(privacy)
        
        if privacy == "public":
            privacy_boolean = False
        else:
            privacy_boolean = True
        
        if(email_prof == "email_prof"):
            email_prof_boolean = True
        else:
            email_prof_boolean = False
        
        if userID == "":
            userID = "Anonymous"
        
        if email_prof == None or report == "" or className == "" or professorName == "" or studentName == "" or rating == None or workType == None or status == "":
            print("not enough fields")
            return render(
                request,
                "report_page.html",
                {
                    "error_message": "You are missing one or more fields.",
                },
                )
        if email_prof_boolean:
            try:
                if professor_email.strip()=="":
                    raise ValidationError("Invalid email")
                validate_email(professor_email)
            except ValidationError as e:
                return render(
                    request,
                    "report_page.html",
                    {
                        "error_message": "You must enter a valid email.",
                    },
                    )
        print("creating object")
        Report.objects.create(userID = userID, report = report, className = className, professorName = professorName, studentName = studentName, rating = rating, workType = workType, fileLink = fileLink, status=status, feedback=feedback, email_prof = email_prof_boolean, professor_email = professor_email, private = privacy_boolean)
    return render(
                request,
                "report_page.html",
                {
                    "error_message": "",
                },
                )
            

@login_required
def user_reports(request):
    print(f"requested user view reports")
    name = "name"
    reports = Report.objects.filter(userID=request.user.email)
    return render(request, 'user_reports.html', {'reports': reports})

    
def review_reports(request):
    reports = Report.objects.all()
    return render(
        request,
        "review_reports.html",
        {'reports' : reports},
    )
    
def new_reports(request):
    new_reports = Report.objects.filter(status='New')
    return render(request, "new_reports.html", {"reports": new_reports})

def in_progress_reports(request):
    inprogress_reports = Report.objects.filter(status='In Progress')
    return render(request, "inprogress_reports.html", {"reports": inprogress_reports})

def resolved_reports(request):
    resolved_reports = Report.objects.filter(status='Resolved')
    return render(request, "resolved_reports.html", {"reports": resolved_reports})   
    
def admin_specific_report_view(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if(report.status == "New"):
        report.status = "Seen"
        report.save()
    if request.method == 'POST':
        if request.POST.get('Resolve',False): #if resolve button is clicked
            feedback = request.POST.get('feedback')
            print(f"Feedback received: [{feedback}]")
            if feedback == "":
                return render(
                    request, 
                    'admin_specific_report_view.html', 
                    {
                        'report': report,
                        # to include in html page
                        'error_message': "You must submit feedback.",
                    },
                )
            report.feedback = feedback
            report.status = "Resolved"
            report.save()
        elif request.POST.get('Email',False): #if email button is clicked
            if report.email_prof:
                print(f"emailing")
                report.email_status=True
                report.save()
                msg='A student,' + report.studentName +', in your class,'+report.className+', has been reported for the following reasons:\n'+ report.report
                if report.fileLink!="":
                    msg+= "\nclick here to view additional evidence:\n" + report.fileLink +"\n"
                if report.userID=="Anonymous":
                    msg+="\n This was reported anonymously"
                else:
                    msg+="\n Please reach back out to the reporter at "+ report.userID + " if you have any other questions or concerns."
                email = EmailMessage('Reporting '+report.studentName+' for '+report.className,
                                    msg,
                                    to=[report.professor_email])
                email.send()
                return render(request, 'email_sent.html', {'message':"Email has been sent to professor!"})
            else:
                return render(request, 'email_sent.html', {'message':"This user has requested to not report to the professor."})

    return render(
        request, 
        'admin_specific_report_view.html', 
        {'report': report},
        )

def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)  

    if request.method == 'POST':         
        report.delete()                    
    return redirect('/userlanding/')            
    

def email(request):
    return render(request, "email_sent.html")

def edit_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    userID = report.userID
    if request.method == 'POST':
        try:
            evidence = Evidence(upload=request.FILES['filename'])
            fileLink = evidence.upload.url
            evidence.save()
        except Exception as e:
            fileLink=report.fileLink
        userID = request.POST['userID']
        className = request.POST['className']
        professorName = request.POST['professorName']
        studentName = request.POST['studentName']
        rating = request.POST.get('rating')
        workType = request.POST.get('workType')
        professor_email = request.POST['professor_email']
        email_prof = request.POST.get('email_prof')
        report_text = request.POST['report']
        privacy = request.POST.get('privacy')
        status = "New"
        feedback = ""
        
        print(privacy)
        
        if privacy == "public":
            privacy_boolean = False
        else:
            privacy_boolean = True
        
        if(email_prof == "email_prof"):
            email_prof_boolean = True
        else:
            email_prof_boolean = False
        
        if userID == "":
            userID = "Anonymous"
        
        if email_prof == None or report_text == "" or className == "" or professorName == "" or studentName == "" or rating == None or workType == None or status == "":
            print("not enough fields")
            return render(
                request,
                "edit_report.html",
                {
                    'report': report,
                    "error_message": "You are missing one or more fields.",
                },
                )
        if email_prof_boolean:
            try:
                if professor_email.strip()=="":
                    raise ValidationError("Invalid email")
                validate_email(professor_email)
            except ValidationError as e:
                return render(
                    request,
                    "edit_report.html",
                    {
                        "error_message": "You must enter a valid email.",
                        'report': report,
                    },
                    )
        print("creating object")
        report.userID = userID
        report.report = report_text
        report.className = className
        report.professorName = professorName
        report.studentName = studentName
        report.rating = rating
        report.workType = workType
        report.fileLink = fileLink
        report.status = status
        report.feedback = feedback
        report.email_prof = email_prof_boolean
        report.professor_email = professor_email
        report.private = privacy_boolean
        report.save()
        return redirect('/userlanding/')
        
    return render(
        request,
        "edit_report.html",
        {
            "error_message": "",
            'report': report,
        },
        )