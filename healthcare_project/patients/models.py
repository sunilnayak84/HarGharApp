from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_details = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    doctor_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')
    notification_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.name} - {self.date} at {self.time} with {self.doctor_name}"

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    doctor_name = models.CharField(max_length=100)
    consultation_type = models.CharField(max_length=50, choices=[('Video', 'Video'), ('Audio', 'Audio')])
    notes = models.TextField(default='No notes')

    def __str__(self):
        return f"Consultation with {self.doctor_name} on {self.date}"

class Feedback(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.patient.name} - Rating: {self.rating}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor.name} - {self.date} at {self.time} - {'Available' if self.is_available else 'Unavailable'}"

class HealthData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50, choices=[('Blood Pressure', 'Blood Pressure'), ('Glucose Level', 'Glucose Level')])
    value = models.CharField(max_length=100)
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.data_type} - {self.value} at {self.date_recorded}"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medication = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    date_prescribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.medication} prescribed by {self.doctor.name} on {self.date_prescribed}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
