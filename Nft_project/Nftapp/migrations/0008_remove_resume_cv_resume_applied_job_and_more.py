# Generated by Django 5.0 on 2024-01-30 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Nftapp", "0007_resume_cv"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resume",
            name="cv",
        ),
        migrations.AddField(
            model_name="resume",
            name="applied_job",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="Nftapp.job"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="resume",
            name="other_language",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="resume",
            name="upload_cv",
            field=models.FileField(default=1, upload_to="cv_uploads/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="resume",
            name="education",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="resume",
            name="full_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="resume",
            name="languages",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Applicant",
        ),
    ]
