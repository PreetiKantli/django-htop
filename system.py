from django.urls import path
from monitor import views

urlpatterns = [
    path('htop/', views.htop),
]
