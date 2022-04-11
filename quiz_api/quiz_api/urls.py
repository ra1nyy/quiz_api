from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account', include('account.urls')),
    path('api/v1/lecture', include('lecture.urls')),
    path('api/v1/quiz', include('quiz.urls')),
    path('api/v1/question', include('question.urls')),
    path('api/v1/study_program', include('study_program.urls')),
    path('api/v1/study_progress', include('study_progress.urls')),
]
