# Generated by Django 5.0 on 2024-01-30 11:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Nftapp", "0008_remove_resume_cv_resume_applied_job_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resume",
            name="languages",
        ),
        migrations.RemoveField(
            model_name="resume",
            name="other_language",
        ),
    ]
