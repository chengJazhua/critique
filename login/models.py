from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Evidence(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.uploaded_at <= now

class Report(models.Model):
    class Statuses(models.TextChoices):
        NEW = "NEW", _("New")
        INPROGRESS = "INP", _("In Progress")
        RESOLVED = "RES", _("Resolved")
    userID = models.CharField(max_length = 200)
    className = models.CharField(max_length = 200)
    professorName = models.CharField(max_length = 200)
    studentName = models.CharField(max_length = 200)
    rating = models.CharField(max_length = 200)
    workType = models.CharField(max_length = 200)
    fileLink = models.CharField(max_length = 500)
    status = models.CharField(max_length = 3, choices=Statuses, default=Statuses.NEW)
    feedback = models.TextField(max_length = 500)