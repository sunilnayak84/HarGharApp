from django.contrib import admin
from django.urls import path, include
from patients.views import RegisterPatientView, CustomRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterPatientView.as_view(), name='register_patient'),
    path('auth/register/', CustomRegisterView.as_view(), name='custom_register'),
    path('patients/', include('patients.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
