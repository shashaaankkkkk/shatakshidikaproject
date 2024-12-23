# Generated by Django 5.1.4 on 2024-12-23 16:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                ("age", models.IntegerField()),
                ("course", models.CharField(max_length=100)),
                (
                    "year_of_study",
                    models.CharField(
                        choices=[
                            ("1", "Year 1"),
                            ("2", "Year 2"),
                            ("3", "Year 3"),
                            ("4", "Year 4"),
                        ],
                        max_length=1,
                    ),
                ),
                ("marital_status", models.BooleanField()),
                ("issue", models.TextField()),
                ("reference", models.CharField(max_length=200)),
                ("contact", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]