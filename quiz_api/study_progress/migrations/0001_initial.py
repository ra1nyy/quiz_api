# Generated by Django 4.0.3 on 2022-04-11 14:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study_program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyProgress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_current_stage', models.BooleanField(default=False)),
                ('percent_of_quiz_progress', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_lecture_studied', models.BooleanField(default=False)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_progress', to='study_program.studyprogram')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_progress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
