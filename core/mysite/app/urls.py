from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [

  path('', views.index, name="index"),
  path("finished/", views.toplay, name="toplay"),
  path("error/", views.error, name="error")
]