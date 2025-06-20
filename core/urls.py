from django.urls import path
from .views import upload_and_diagnose, showcase, register_view, login_view, logout_view, dashboard
from . import views

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Main application URLs
    path('dashboard/', dashboard, name='dashboard'),
    path('upload/', upload_and_diagnose, name='upload'),
    path('', showcase, name='showcase'),
] 