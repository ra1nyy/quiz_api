from django.urls import path
from study_program.views import StudyProgramView

urlpatterns = [
    path('/', StudyProgramView.as_view()),
]
