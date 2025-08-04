from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home/', views.account_home, name='account-home'),
    path('logged-out/', views.logged_out, name='logged-out'),
]
