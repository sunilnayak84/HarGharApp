from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Patient, Appointment, Consultation

class PatientTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='TestPassword123')
        self.patient = Patient.objects.create(user=self.user, name='Test Patient', age=30, contact_details='test@example.com')
        self.client.login(username='testuser', password='TestPassword123')

    def test_register_patient(self):
        url = reverse('register_patient')
        data = {
            "name": "Test Patient 2",
            "age": 40,
            "contact_details": "test2@example.com"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patient_dashboard(self):
        url = reverse('patient_dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_appointment_booking(self):
        url = reverse('book_appointment')
        data = {
            "patient": self.patient.id,
            "date": "2024-07-15",
            "time": "10:00:00",
            "doctor_name": "Dr. John Doe"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_consultation_creation(self):
        url = reverse('create_consultation')
        data = {
            "patient": self.patient.id,
            "date": "2024-07-15",
            "time": "10:30:00",
            "doctor_name": "Dr. John Doe",
            "consultation_type": "Follow-up"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_reports(self):
        url = reverse('reports')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

