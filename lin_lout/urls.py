from django.contrib import admin
from django.urls import path
from lin_lout import views
import  lin_lout.views as views
app_name = 'lin_lout'


urlpatterns = [
    path('', views.LOGIN_VIEW, name="login"),
]


