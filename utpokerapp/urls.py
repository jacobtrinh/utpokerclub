from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('membership/', views.membership, name="membership"),
    path('contact/', views.contact, name="contact"),
    path('activities/', views.activities, name="activities")

]
