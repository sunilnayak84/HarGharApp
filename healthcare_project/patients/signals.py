from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment

@receiver(post_save, sender=Appointment)
def send_appointment_notification(sender, instance, created, **kwargs):
    if created:
        # Logic to send notification for a new appointment
        print(f"Notification: Appointment created for {instance.patient.name} on {instance.date} at {instance.time}.")
    else:
        # Logic to send notification for an updated appointment
        print(f"Notification: Appointment updated for {instance.patient.name} on {instance.date} at {instance.time}.")
