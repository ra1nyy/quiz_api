from rest_framework import serializers, status
from question.models import Question
from quiz.models import Quiz
from question.serializers import QuestionSerializer
from study_program.models import StudyProgram
from study_progress.models import StudyProgress
from core.handlers import ResponseException


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

    def to_representation(self, instance):
        response = super(QuizSerializer, self).to_representation(instance)
        stage = StudyProgram.objects.filter(quiz=instance).first()
        study_progress = StudyProgress.objects.filter(user=self.context['request'].user, stage=stage)
        if study_progress.exists() and study_progress.first().is_current_stage \
                and study_progress.first().is_lecture_studied:
            questions_to_response = []
            for question_id in response['questions']:
                question = Question.objects.get(id=question_id)
                questions_to_response.append(QuestionSerializer(question).data)
            response['questions'] = questions_to_response
            return response
        else:
            raise ResponseException('You do not have access to the quiz of this stage!',
                                    status_code=status.HTTP_400_BAD_REQUEST)


class QuizSaveResultsSerializer(serializers.ModelSerializer):
    answers_dict = serializers.DictField(required=True)

    class Meta:
        model = Quiz
        fields = ['answers_dict']

    def save_quiz_results(self):
        answers_dict = self.validated_data.get('answers_dict')
        stage = StudyProgram.objects.filter(quiz=self.instance).first()
        study_progress = StudyProgress.objects.filter(user=self.context['request'].user,
                                                      stage=stage).first()

        right_answers = 0
        for question_id in answers_dict:
            question = Question.objects.get(id=question_id)
            if question.type == 'text':
                if isinstance(answers_dict[question_id], str):
                    if question.text_answer and question.text_answer.lower() == answers_dict[question_id].lower():
                        right_answers += 1
                else:
                    raise ResponseException('Answer have incorrect type!',
                                            status_code=status.HTTP_400_BAD_REQUEST)
            elif question.type in ['one_answer', 'many_answers']:
                if isinstance(answers_dict[question_id], list):
                    # TODO: переделать логику, тк не учитываются частично верные ответы
                    if question.right_answers and question.right_answers.sort() == answers_dict[question_id].sort():
                        right_answers += 1
                else:
                    raise ResponseException('Answer have incorrect type!',
                                            status_code=status.HTTP_400_BAD_REQUEST)
        percent_of_quiz_progress = round((right_answers / self.instance.questions.count()) * 100)
        study_progress.percent_of_quiz_progress = percent_of_quiz_progress
        study_progress.save(update_fields=['percent_of_quiz_progress'])
