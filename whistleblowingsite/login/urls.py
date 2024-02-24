from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path('logout/', LogoutView.as_view()),
    path('userlanding/<str:username>/', views.user_landing_view),
]