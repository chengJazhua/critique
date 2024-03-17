from django.test import TestCase, RequestFactory
from .models import Report
import datetime
from django.utils import timezone
from .models import Evidence

# Create your tests here.
# class ReportModelTests(TestCase):
#     def setUp(self):
#         self.report = Report(userID = "user", className = "ASDE", professorName = "sherriff", 
#                              studentName="John Doe", rating = "Neutral", workType = "Group Project", 
#                              fileLink = "testfile.com")
#         self.factory = RequestFactory()

#     def test_user(self):
#         self.assertEqual(self.report.userID, "user")

#     def test_className(self):
#         self.assertEqual(self.report.className, "ASDE")

#     def test_professorName(self):
#         self.assertEqual(self.report.professorName, "sherriff")

#     def test_studentName(self):
#         self.assertEqual(self.report.studentName, "John Doe")

#     def test_rating(self):
#         self.assertEqual(self.report.rating, "Neutral")

#     def test_workType(self):
#         self.assertEqual(self.report.workType, "Group Project")

#     def test_fileLink(self):
#         self.assertEqual(self.report.fileLink, "testfile.com")

class EvidenceModelTests(TestCase):
    def test(self):
        self.assertIs(1, 1)
#     def test_was_published_recently_with_future_upload_at(self):
#         time = timezone.now() + datetime.timedelta(days=30)
#         future_upload_at = Evidence(uploaded_at=time)
#         self.assertIs(future_upload_at.was_published_recently(), False)

#     def test_was_published_recently_with_old_question(self):

#         time = timezone.now() - datetime.timedelta(days=1, seconds=1)
#         old_upload_at = Evidence(uploaded_at=time)
#         self.assertIs(old_upload_at.was_published_recently(), False)


#     def test_was_published_recently_with_recent_question(self):

#         time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
#         recent_upload_at = Evidence(uploaded_at=time)
#         self.assertIs(recent_upload_at.was_published_recently(), True)

