from rest_framework import serializers, status
from lecture.models import Lecture
from study_program.models import StudyProgram
from study_progress.models import StudyProgress
from django.contrib.auth.models import User
from core.handlers import ResponseException


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

    def to_representation(self, instance):
        response = super(LectureSerializer, self).to_representation(instance)
        stage = StudyProgram.objects.filter(lecture=instance).first()
        study_progress = StudyProgress.objects.filter(user=self.context['request'].user, stage=stage)
        if study_progress.exists() and study_progress.first().is_current_stage:
            return response
        else:
            raise ResponseException('You do not have access to the lecture of this stage!',
                                    status_code=status.HTTP_400_BAD_REQUEST)


class StartStudyingLectureSerializer(serializers.Serializer):
    lecture = serializers.PrimaryKeyRelatedField(queryset=Lecture.objects.all(), required=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    def start_study(self):
        lecture = self.validated_data['lecture']
        user = self.validated_data['user']
        stage = StudyProgram.objects.filter(lecture=lecture).first()

        if not StudyProgress.objects.filter(user=user).exists():
            study_progress = StudyProgress.objects.create(
                user=user,
                is_current_stage=True,
                stage=stage)
        else:
            StudyProgress.objects.all().update(is_current_stage=False)
            study_progress = StudyProgress.objects.filter(user=user, stage=stage).first()
            study_progress.is_current_stage = True
            study_progress.save(update_fields=['is_current_stage'])
        return study_progress


class FinishStudyingLectureSerializer(serializers.Serializer):
    lecture = serializers.PrimaryKeyRelatedField(queryset=Lecture.objects.all(), required=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)

    def finish_study(self):
        lecture = self.validated_data['lecture']
        user = self.validated_data['user']
        stage = StudyProgram.objects.filter(lecture=lecture).first()

        if not StudyProgress.objects.filter(user=user).exists():
            return False
        else:
            study_progress = StudyProgress.objects.filter(user=user, stage=stage).first()
            study_progress.is_lecture_studied = True
            study_progress.save(update_fields=['is_lecture_studied'])
        return study_progress
