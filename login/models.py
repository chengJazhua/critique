from django.db import models

# Create your models here.

class Evidence(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()

class Report(models.Model):
    userID = models.CharField(max_length = 200)
    className = models.CharField(max_length = 200)
    professorName = models.CharField(max_length = 200)
    studentName = models.CharField(max_length = 200)
    rating = models.CharField(max_length = 200)
    workType = models.CharField(max_length = 200)
    fileLink = models.CharField(max_length = 500)