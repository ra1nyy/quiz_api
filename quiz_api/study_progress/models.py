import uuid
from django.db import models
from django.contrib.auth.models import User
from study_program.models import StudyProgram
from django.core.validators import MinValueValidator, MaxValueValidator


class StudyProgress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='study_progress', on_delete=models.CASCADE)
    stage = models.ForeignKey(StudyProgram, related_name='study_progress', on_delete=models.CASCADE)
    is_current_stage = models.BooleanField(default=False)
    percent_of_quiz_progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                                   default=0)
    is_lecture_studied = models.BooleanField(default=False)
