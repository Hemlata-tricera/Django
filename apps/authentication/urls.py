from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from .views import *  # Import views from the authentication app

urlpatterns = [
    path('home/', home, name="recipes"),      # Home page
    path("admin/", admin.site.urls),          # Admin interface
    path('login/', login_page, name='login_page'),    # Login page
    path('logout/', logout_page, name='logout_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
]
