# serializers.py
from rest_framework import serializers
from .models import *


class DoctorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_data
        fields = '__all__'


class AppointmentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointmnet_data
        fields = '__all__'


class InsurancePlanDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance_plan_data
        fields = '__all__'
