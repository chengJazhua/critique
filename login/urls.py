from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import include, re_path


app_name = "login"
urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path('logout/', LogoutView.as_view()),
    path('userlanding/', views.user_reports),
    path('adminlanding/',views.admin_landing_view),
    path('report/', views.report),
    path('publicreports/', views.public_reports),
    path('viewreports/', views.admin_view_reports),
    path('adminreportview/', views.review_reports),
    path('adminreportview/<int:pk>/', views.admin_specific_report_view, name='admin_specific_report_view'),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.report_delete, name='report_delete'),
    path('sent/',views.email),
    path('new_reports/',views.new_reports),
    path('in_progress_reports/',views.in_progress_reports),
    path('resolved_reports/',views.resolved_reports),

]
