from rest_framework import serializers
from study_progress.models import StudyProgress
from core.handlers import ResponseException


class StudyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgress
        fields = '__all__'
