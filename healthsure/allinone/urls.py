from django.contrib import admin
from django.urls import path
from lin_lout import views
from django.urls.conf import include
from allinone import views


from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

app_name = 'allinone'

urlpatterns = [
    
    #api call for the just presentation
    # path('doctor_details/', views.doctor_details, name='doctor_details'),
    # path('appointmnet_details/', views.appointmnet_details, name='appointmnet_details'),
    # path('Insurance_Plans_details/', views.Insurance_Plans_details, name='Insurance_Plans_details'),
    path('doctor-details/', views.doctor_details, name='doctor-details'),
    path('appointment-details/', views.appointmnet_details, name='appointment-details'),
    path('insurance-plans-details/', views.insurance_plans_details, name='insurance-plans-details'),

    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]