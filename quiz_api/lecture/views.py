from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin

from lecture.models import Lecture
from lecture.serializers import (LectureSerializer, StartStudyingLectureSerializer,
                                 FinishStudyingLectureSerializer)
from core.permissions import IsAuthenticated
from rest_framework.response import Response
from core.handlers import ResponseException


class LectureRetrieveView(RetrieveModelMixin,
                          GenericAPIView):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class StartStudyingLectureView(GenericAPIView):
    serializer_class = StartStudyingLectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.start_study()
        return Response(LectureSerializer(serializer.validated_data['lecture'],
                                          context={'request': request}).data,
                        status=status.HTTP_200_OK)


class FinishStudyingLectureView(GenericAPIView):
    serializer_class = FinishStudyingLectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not serializer.finish_study():
            raise ResponseException('You havent started studying this lecture yet!',
                                    status_code=status.HTTP_400_BAD_REQUEST)
        return Response(LectureSerializer(serializer.validated_data['lecture'],
                                          context={'request': request}).data,
                        status=status.HTTP_200_OK)
