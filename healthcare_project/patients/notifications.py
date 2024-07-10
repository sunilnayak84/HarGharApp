from django.core.mail import send_mail
from .models import Appointment, Notification

def send_appointment_notification(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    message = f"Reminder: Your appointment with Dr. {appointment.doctor_name} on {appointment.date} at {appointment.time}."
    Notification.objects.create(user=appointment.patient.user, message=message)



def send_appointment_notification(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    subject = f"Appointment Reminder: {appointment.date} at {appointment.time}"
    message = f"Dear {appointment.patient.name},\n\nThis is a reminder for your appointment with Dr. {appointment.doctor_name} on {appointment.date} at {appointment.time}.\n\nThank you."
    recipient_list = [appointment.patient.contact_details]
    send_mail(subject, message, 'noreply@healthcareapp.com', recipient_list)
    appointment.notification_sent = True
    appointment.save()
