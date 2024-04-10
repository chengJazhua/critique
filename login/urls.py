from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView



app_name = "login"
urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path('logout/', LogoutView.as_view()),
    path('userlanding/', views.user_reports),
    path('adminlanding/',views.admin_landing_view),
    path('report/', views.report),
    path('viewreports/', views.user_reports),
    path('viewreports/', views.admin_view_reports),
    path('adminreportview/', views.review_reports),
    path('adminreportview/<int:pk>/', views.admin_specific_report_view, name='admin_specific_report_view'),
    path('sent/',views.email)
]
