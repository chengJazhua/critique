from django.test import TestCase, RequestFactory
from .models import Report

# Create your tests here.
class ReportModelTests(TestCase):
    def setUp(self):
        self.report = Report(userID = "user", className = "ASDE", professorName = "sherriff", 
                             studentName="John Doe", rating = "Neutral", workType = "Group Project", 
                             fileLink = "testfile.com")
        self.factory = RequestFactory()

    def test_user(self):
        self.assertEqual(self.report.userID, "user")

    def test_className(self):
        self.assertEqual(self.report.className, "ASDE")

    def test_professorName(self):
        self.assertEqual(self.report.professorName, "sherriff")

    def test_studentName(self):
        self.assertEqual(self.report.studentName, "John Doe")

    def test_rating(self):
        self.assertEqual(self.report.rating, "Neutral")

    def test_workType(self):
        self.assertEqual(self.report.workType, "Group Project")

    def test_fileLink(self):
        self.assertEqual(self.report.fileLink, "testfile.com")