import uuid
from django.db import models
from quiz.models import Quiz
from lecture.models import Lecture


class StudyProgram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lecture = models.ForeignKey(Lecture, related_name='study_program', null=False, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='study_program', null=True, on_delete=models.SET_NULL)
    stage = models.IntegerField(default=0)
