from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
   path("", views.index, name="index"),
   path("about/", views.about, name="about"),
   path("gellery/", views.gellery, name="gellery"),
   path("filims/", views.filims, name="filims"),
   path("portfolio/", views.portfolio, name="portfolio"),
   path("portfolio-detail/", views.portfolio_detail, name="portfolio-detail"),
   path("contact/", views.contact, name="contact"),
   path("enquiry/", views.enquiry, name="enquiry"),
   path("login/", views.login, name="login"),
   path("register/", views.register, name="register"),
   path("logout/", views.logout, name="logout"),
   

]