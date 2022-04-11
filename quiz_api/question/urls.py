from django.urls import path
from question.views import QuestionRetrieveView

urlpatterns = [
    path('/<uuid:pk>', QuestionRetrieveView.as_view()),
]
