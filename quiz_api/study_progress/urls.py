from django.urls import path
from study_progress.views import StudyProgressView

urlpatterns = [
    path('/<uuid:pk>', StudyProgressView.as_view()),
    # path('/quiz_result', )
]
