from django import forms
from login.models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields=['userID', 'report', 'className', 'professorName', 'studentName', 
                'rating','workType','fileLink','status','feedback', 'professor_email', 'email_prof', 'private', 'reported']