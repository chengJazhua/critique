from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView



app_name = "login"
urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html")),
    path('logout/', LogoutView.as_view()),
    path('userlanding/<str:username>/', views.user_landing_view),
    path('adminlanding/<str:username>/',views.admin_landing_view),
]