from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Avg
from .models import Patient, Appointment, Consultation, Message, Doctor, Availability, HealthData, Prescription, Feedback, Notification
from .serializers import PatientSerializer, AppointmentSerializer, ConsultationSerializer, MessageSerializer, DoctorSerializer, AvailabilitySerializer, HealthDataSerializer, PrescriptionSerializer, FeedbackSerializer, NotificationSerializer
from .notifications import send_appointment_notification
from dj_rest_auth.registration.views import RegisterView
from django.contrib.auth.models import User
from django.shortcuts import render

def my_view(request):
    return render(request, 'my_template.html', context)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_patient(request):
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CustomRegisterView(RegisterView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by('-timestamp')

class RegisterPatientView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]

class PatientProfileView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentBookingView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        appointment = serializer.save()
        send_appointment_notification(appointment.id)

class AppointmentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_update(self, serializer):
        appointment = serializer.save()
        send_appointment_notification(appointment.id)

class ConsultationCreateView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class ConsultationDetailView(generics.RetrieveUpdateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AvailabilityCreateView(generics.CreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class AvailabilityDetailView(generics.RetrieveUpdateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class HealthDataCreateView(generics.CreateAPIView):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer

class HealthDataListView(generics.ListAPIView):
    queryset = HealthData.objects.all()
    serializer_class = HealthDataSerializer

class PrescriptionCreateView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class PrescriptionDetailView(generics.RetrieveUpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackListView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class PatientDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patient = request.user
        appointments = Appointment.objects.filter(patient=patient)
        consultations = Consultation.objects.filter(patient=patient)
        messages = Message.objects.filter(receiver=patient.name)
        feedback = Feedback.objects.filter(patient=patient)

        data = {
            "appointments": AppointmentSerializer(appointments, many=True).data,
            "consultations": ConsultationSerializer(consultations, many=True).data,
            "messages": MessageSerializer(messages, many=True).data,
            "feedback": FeedbackSerializer(feedback, many=True).data,
        }

        return Response(data)

class DoctorDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctor = request.user
        appointments = Appointment.objects.filter(doctor_name=doctor.name)
        consultations = Consultation.objects.filter(doctor_name=doctor.name)
        feedback = Feedback.objects.filter(appointment__doctor_name=doctor.name) | Feedback.objects.filter(consultation__doctor_name=doctor.name)

        data = {
            "appointments": AppointmentSerializer(appointments, many=True).data,
            "consultations": ConsultationSerializer(consultations, many=True).data,
            "feedback": FeedbackSerializer(feedback, many=True).data,
        }

        return Response(data)

class ReportsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Count of appointments per doctor
        appointments_per_doctor = Appointment.objects.values('doctor_name').annotate(count=Count('id'))

        # Average rating per doctor
        avg_rating_per_doctor = Feedback.objects.values('appointment__doctor_name').annotate(avg_rating=Avg('rating'))

        # Total number of patients
        total_patients = Patient.objects.count()

        # Total number of appointments
        total_appointments = Appointment.objects.count()

        # Total number of consultations
        total_consultations = Consultation.objects.count()

        data = {
            'appointments_per_doctor': appointments_per_doctor,
            'avg_rating_per_doctor': avg_rating_per_doctor,
            'total_patients': total_patients,
            'total_appointments': total_appointments,
            'total_consultations': total_consultations,
        }

        return Response(data)

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')

class MarkNotificationAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user, is_read=False)

    def perform_update(self, serializer):
        serializer.instance.is_read = True
        serializer.save()
