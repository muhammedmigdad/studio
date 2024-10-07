from django.urls import path
from manager import views

app_name = "manager"

urlpatterns = [
    
    path("enquiry/", views.enquiry, name="enquiry"),
    path("login/", views.login, name="login"),
    

]