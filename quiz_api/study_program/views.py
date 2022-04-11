from rest_framework.generics import ListAPIView
from core.permissions import IsAuthenticated
from study_program.models import StudyProgram
from study_program.serializers import StudyProgramSerializer


class StudyProgramView(ListAPIView):
    queryset = StudyProgram.objects.all().order_by('stage')
    permission_classes = (IsAuthenticated, )
    serializer_class = StudyProgramSerializer
