# Generated by Django 5.0 on 2024-01-23 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nftapp', '0008_remove_resume_cv_resume_upload_cv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='other_language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
