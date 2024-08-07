# patients/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Appointment, Consultation, Message, Doctor, Availability, HealthData, Prescription, Feedback, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Patient
        fields = ['username', 'password', 'name', 'age', 'contact_details']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(username=user_data['username'], password=validated_data.pop('password'))
        patient = Patient.objects.create(user=user, **validated_data)
        return patient

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'

class HealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthData
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
