import uuid
from django.db import models
from question.models import Question


class Quiz(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    questions = models.ManyToManyField(Question, related_name='quiz')
