from django.urls import path
from .views import RegisterPatientView, PatientProfileView, AppointmentBookingView, AppointmentDetailView, ConsultationCreateView, ConsultationDetailView, MessageCreateView, MessageListView, DoctorCreateView, DoctorDetailView, AvailabilityCreateView, AvailabilityDetailView, HealthDataCreateView, HealthDataListView, PrescriptionCreateView, PrescriptionDetailView, FeedbackCreateView, FeedbackListView, PatientDashboardView, DoctorDashboardView, ReportsView, CustomRegisterView, NotificationListView, MarkNotificationAsReadView

urlpatterns = [
    path('register/', RegisterPatientView.as_view(), name='register_patient'),
    path('profile/<int:pk>/', PatientProfileView.as_view(), name='patient_profile'),
    path('appointments/book/', AppointmentBookingView.as_view(), name='book_appointment'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('consultations/', ConsultationCreateView.as_view(), name='create_consultation'),
    path('consultations/<int:pk>/', ConsultationDetailView.as_view(), name='consultation_detail'),
    path('messages/', MessageCreateView.as_view(), name='create_message'),
    path('messages/list/', MessageListView.as_view(), name='list_messages'),
    path('doctors/', DoctorCreateView.as_view(), name='create_doctor'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('availability/', AvailabilityCreateView.as_view(), name='create_availability'),
    path('availability/<int:pk>/', AvailabilityDetailView.as_view(), name='availability_detail'),
    path('healthdata/', HealthDataCreateView.as_view(), name='create_healthdata'),
    path('healthdata/list/', HealthDataListView.as_view(), name='list_healthdata'),
    path('prescriptions/', PrescriptionCreateView.as_view(), name='create_prescription'),
    path('prescriptions/<int:pk>/', PrescriptionDetailView.as_view(), name='prescription_detail'),
    path('feedback/', FeedbackCreateView.as_view(), name='create_feedback'),
    path('feedback/list/', FeedbackListView.as_view(), name='list_feedback'),
    path('dashboard/patient/', PatientDashboardView.as_view(), name='patient_dashboard'),
    path('dashboard/doctor/', DoctorDashboardView.as_view(), name='doctor_dashboard'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('auth/register/', CustomRegisterView.as_view(), name='custom_register'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/mark-as-read/<int:pk>/', MarkNotificationAsReadView.as_view(), name='mark_notification_as_read'),
]
