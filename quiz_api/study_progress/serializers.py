from rest_framework import serializers
from study_progress.models import StudyProgress
from core.handlers import ResponseException


class StudyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyProgress
        fields = '__all__'


class StudyProgressSendResultsSerializer(serializers.ModelSerializer):
    text_answer = serializers.CharField(required=False)
    answer_list = serializers.ListField(required=False)

    class Meta:
        model = StudyProgress
        fields = ['text_answer', 'answer_list']

    def update(self, instance, validated_data):
        text_answer = self.validated_data.get('text_answer')
        answer_list = self.validated_data.get('answer_list')
        print(self.instance)
        if self.instance.type == 'text':
            if not text_answer:
                pass

        elif self.instance.type in ['one_answer', 'many_answer']:
            if not answer_list:
                pass
            print('type another')