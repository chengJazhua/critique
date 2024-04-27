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
    path('publicreports/newest', views.public_reports_newest),
    path('publicreports/votes', views.public_reports_votes),
    path('viewreports/', views.admin_view_reports),
    path('adminreportview/', views.review_reports),
    path('adminreportview/<int:pk>/', views.admin_specific_report_view, name='admin_specific_report_view'),
    path('publicreports/<int:pk>/', views.public_specific_report_view, name='public_specific_report_view'),
    re_path(r'^delete/admin/(?P<pk>[0-9]+)/$', views.report_delete_admin, name='report_delete_admin'),
    re_path(r'^delete/user/(?P<pk>[0-9]+)/$', views.report_delete, name='report_delete'),
    
    path('sent/',views.email),
    path('new_reports/',views.new_reports),
    path('in_progress_reports/',views.in_progress_reports),
    path('resolved_reports/',views.resolved_reports),
    path('admin_public_reports/',views.admin_public_reports),
    path('editreport/<int:pk>/',views.edit_report),
]
