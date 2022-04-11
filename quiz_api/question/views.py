from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from question.models import Question
from question.serializers import QuestionSerializer
from core.permissions import IsAuthenticated


class QuestionRetrieveView(RetrieveModelMixin,
                           GenericAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
