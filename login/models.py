from django.db import models

class Report(models.Model):
    userID = models.CharField(max_length = 200)
    className = models.CharField(max_length = 200)
    professorName = models.CharField(max_length = 200)
    studentName = models.CharField(max_length = 200)
    ratings = models.CharField(max_length = 200)
    workType = models.CharField(max_length = 200)
    fileLink = models.CharField(max_length = 500)