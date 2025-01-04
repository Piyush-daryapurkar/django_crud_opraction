from django.urls import path
from . import views
urlpatterns=[
    path("",views.head),
    path("about/",views.index),
    path("contact/", views.contact)
]