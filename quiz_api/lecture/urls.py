from django.urls import path
from lecture.views import LectureRetrieveView, StartStudyingLectureView, FinishStudyingLectureView

urlpatterns = [
    path('/<uuid:pk>', LectureRetrieveView.as_view()),
    path('/start_studying', StartStudyingLectureView.as_view()),
    path('/finish_studying', FinishStudyingLectureView.as_view()),
]
