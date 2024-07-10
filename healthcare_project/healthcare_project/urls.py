from django.contrib import admin
from django.urls import path, include
from patients.views import RegisterPatientView

urlpatterns = [
    path('patients/register/', RegisterPatientView.as_view(), name='register_patient'),
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
