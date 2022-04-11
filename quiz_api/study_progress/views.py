from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from core.permissions import IsAuthenticated
from study_progress.models import StudyProgress
from study_progress.serializers import StudyProgressSerializer, StudyProgressSendResultsSerializer


class StudyProgressView(RetrieveModelMixin,
                        GenericAPIView):
    serializer_class = StudyProgressSerializer
    queryset = StudyProgress.objects.all()
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return StudyProgressSendResultsSerializer
        return self.serializer_class

