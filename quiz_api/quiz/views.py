from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from core.permissions import IsAuthenticated
from quiz.models import Quiz
from quiz.serializers import QuizSerializer, QuizSaveResultsSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class QuizRetrieveView(RetrieveModelMixin,
                       GenericAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(Quiz, pk=pk)
        self.serializer_class = QuizSaveResultsSerializer
        serializer = self.serializer_class(data=request.data, instance=instance,
                                           context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save_quiz_results()
        # response = serializer.to_representation(updated)
        response = QuizSerializer(instance, context={"request": request})
        return Response(response.data, status=status.HTTP_200_OK)

