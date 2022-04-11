from django.urls import path
from quiz.views import QuizRetrieveView

urlpatterns = [
    path('/<uuid:pk>', QuizRetrieveView.as_view()),
]
