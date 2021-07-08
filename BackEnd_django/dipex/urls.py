from django.urls import path

from dipex.views import (
    InterviewByDiseaseView,
    InterviewByKeywordView,
    InterviewByAgeView,
    InterviewByExpertView,
    InterviewDetailView
)

urlpatterns = [
    path('interview/<int:pk>/', InterviewDetailView.as_view()),
    path('interview/<str:disease>/', InterviewByDiseaseView.as_view()),
    path('interview/<str:disease>/age/', InterviewByAgeView.as_view()),
    path('interview/<str:disease>/expert/', InterviewByExpertView.as_view()),
    path('interview/<str:disease>/<str:keyword>/', InterviewByKeywordView.as_view()),
]
