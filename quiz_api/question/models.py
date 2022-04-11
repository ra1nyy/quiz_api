import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField


def default_answer_option():
    return {1: 'answer 1'}


class Question(models.Model):
    TYPES = (
        ('text', 'text'),
        ('one_answer', 'one_answer'),
        ('many_answers', 'many_answers'),
        ('comparison', 'comparison')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(default='text', choices=TYPES, max_length=60)
    question = models.CharField(default=None, max_length=500)                     # 'What is love ?
    text_answer = models.CharField(default=None, max_length=100, null=True)       # if type == 'text'
    answer_options = models.JSONField(default=default_answer_option, null=True)   # else {1: "shit", 2: "perfect"}
    right_answers = ArrayField(models.IntegerField(default=0), null=True, blank=True)   # [1,]
