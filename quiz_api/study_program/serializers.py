from rest_framework import serializers

from study_program.models import StudyProgram


class StudyProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudyProgram
        fields = '__all__'
