# from django.shortcuts import render
#
# # Create your views here.
# from django.shortcuts import render, redirect
# from urllib import request
# from django.contrib.auth.models import User
# from django.db import connection
# import json
# from django.http import JsonResponse
# from allinone.models import *
#
#
# def doctor_details(request):
#
#     data = Doctor_data.objects.get_queryset()
#     print(data)
#
#     return JsonResponse(data)
#
# def appointmnet_details(request):
#     pass
# def Insurance_Plans_details(request):
#     pass
# views.py
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *



def doctor_details(request):
    data = Doctor_data.objects.all()
    serializer = DoctorDataSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)



def appointmnet_details(request):
    data = Appointmnet_data.objects.all()
    serializer = AppointmentDataSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)



def insurance_plans_details(request):
    data = Insurance_plan_data.objects.all()
    serializer = InsurancePlanDataSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)
