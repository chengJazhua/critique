from django.test import TestCase, RequestFactory, Client
from .models import Report
import datetime
from django.utils import timezone
from .models import Evidence
from django.urls import reverse

# Create your tests here.
class EvidenceModelTests(TestCase):
    def test(self):
        self.assertIs(1, 1)
    def test_was_published_recently_with_future_upload_at(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_upload_at = Evidence(uploaded_at=time)
        self.assertIs(future_upload_at.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):

        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_upload_at = Evidence(uploaded_at=time)
        self.assertIs(old_upload_at.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_upload_at = Evidence(uploaded_at=time)
        self.assertIs(recent_upload_at.was_published_recently(), True)

class ReportModelTests(TestCase):
    def test_report(self):
        test_report = Report(
            userID = "test_user", 
            report = "student did this!", 
            className = "CS 3240", 
            professorName = "Sheriff", 
            studentName = "test_student", 
            rating = "Positive", 
            workType = "Assignment", 
            fileLink = "fakefilelink.com", 
            status = "Resolved",
            feedback = "report is resolved!",
            professor_email = "fakeprofessoremail@gmail.com",
            email_prof = False,
            private = True,
            reported = False,
            email_status = False,
        )
        self.assertEqual(test_report.userID, "test_user")
        self.assertEqual(test_report.report, "student did this!")
        self.assertEqual(test_report.className, "CS 3240")
        self.assertEqual(test_report.professorName, "Sheriff")
        self.assertEqual(test_report.rating, "Positive")
        self.assertEqual(test_report.workType, "Assignment")
        self.assertEqual(test_report.fileLink, "fakefilelink.com")
        self.assertEqual(test_report.status, "Resolved")
        self.assertEqual(test_report.feedback, "report is resolved!")
        self.assertEqual(test_report.professor_email, "fakeprofessoremail@gmail.com")
        self.assertEqual(test_report.email_prof, False)
        self.assertEqual(test_report.private, True)
        self.assertEqual(test_report.reported, False)
        self.assertEqual(test_report.email_status, False)
        
    def test_report_default_values(self):
        test_report = Report(
            userID = "test_user", 
            report = "student did this!", 
            className = "CS 3240", 
            professorName = "Sheriff", 
            studentName = "test_student", 
            rating = "Positive", 
            workType = "Assignment", 
            fileLink = "fakefilelink.com", 
            status = "Resolved",
            feedback = "report is resolved!",
            professor_email = "fakeprofessoremail@gmail.com",
        )
        self.assertEqual(test_report.userID, "test_user")
        self.assertEqual(test_report.report, "student did this!")
        self.assertEqual(test_report.className, "CS 3240")
        self.assertEqual(test_report.professorName, "Sheriff")
        self.assertEqual(test_report.rating, "Positive")
        self.assertEqual(test_report.workType, "Assignment")
        self.assertEqual(test_report.fileLink, "fakefilelink.com")
        self.assertEqual(test_report.status, "Resolved")
        self.assertEqual(test_report.feedback, "report is resolved!")
        self.assertEqual(test_report.professor_email, "fakeprofessoremail@gmail.com")
        self.assertEqual(test_report.email_prof, True)
        self.assertEqual(test_report.private, True)
        self.assertEqual(test_report.reported, False)
        self.assertEqual(test_report.email_status, False)
        
class ReportAttributeTests(TestCase):
    def test_report_attributes(self):
        test_report = Report(
            userID = "test_user", 
            report = "student did this!", 
            className = "CS 3240", 
            professorName = "Sheriff", 
            studentName = "test_student", 
            rating = "Positive", 
            workType = "Assignment", 
            fileLink = "fakefilelink.com", 
            status = "Resolved",
            feedback = "report is resolved!",
            professor_email = "fakeprofessoremail@gmail.com",
            email_prof = False,
            private = True,
            reported = False,
            email_status = False,
        )
        self.assertIsInstance(test_report.userID, str)
        self.assertIsInstance(test_report.report, str)
        self.assertIsInstance(test_report.className, str)
        self.assertIsInstance(test_report.professorName, str)
        self.assertIsInstance(test_report.rating, str)
        self.assertIsInstance(test_report.workType, str)
        self.assertIsInstance(test_report.fileLink, str)
        self.assertIsInstance(test_report.status, str)
        self.assertIsInstance(test_report.feedback, str)
        self.assertIsInstance(test_report.professor_email, str)
        self.assertIsInstance(test_report.email_prof, bool)
        self.assertIsInstance(test_report.private, bool)
        self.assertIsInstance(test_report.reported, bool)
        self.assertIsInstance(test_report.email_status, bool)
        
    def test_report_default_values_attributes(self):
        test_report = Report(
            userID = "test_user", 
            report = "student did this!", 
            className = "CS 3240", 
            professorName = "Sheriff", 
            studentName = "test_student", 
            rating = "Positive", 
            workType = "Assignment", 
            fileLink = "fakefilelink.com", 
            status = "Resolved",
            feedback = "report is resolved!",
            professor_email = "fakeprofessoremail@gmail.com",
        )
        self.assertIsInstance(test_report.userID, str)
        self.assertIsInstance(test_report.report, str)
        self.assertIsInstance(test_report.className, str)
        self.assertIsInstance(test_report.professorName, str)
        self.assertIsInstance(test_report.rating, str)
        self.assertIsInstance(test_report.workType, str)
        self.assertIsInstance(test_report.fileLink, str)
        self.assertIsInstance(test_report.status, str)
        self.assertIsInstance(test_report.feedback, str)
        self.assertIsInstance(test_report.professor_email, str)
        self.assertIsInstance(test_report.email_prof, bool)
        self.assertIsInstance(test_report.private, bool)
        self.assertIsInstance(test_report.reported, bool)
        self.assertIsInstance(test_report.email_status, bool)