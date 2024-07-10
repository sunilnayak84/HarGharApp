# Generated by Django 5.0.7 on 2024-07-10 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0005_doctor_availability"),
    ]

    operations = [
        migrations.CreateModel(
            name="HealthData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data_type",
                    models.CharField(
                        choices=[
                            ("Blood Pressure", "Blood Pressure"),
                            ("Glucose Level", "Glucose Level"),
                        ],
                        max_length=50,
                    ),
                ),
                ("value", models.CharField(max_length=100)),
                ("date_recorded", models.DateTimeField(auto_now_add=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.patient",
                    ),
                ),
            ],
        ),
    ]
