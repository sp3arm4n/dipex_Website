from rest_framework import generics

from dipex.models import Interview
from dipex.serializers import InterviewSerializer


# Interview 뷰 셋
# TODO: Interview마다 filter 적용한 쿼리 필요
# TODO: 주제별 [Disease-keyword]
# TODO: 연령별 [Interview-interview_age]
# TODO: 전문가 [Person-is_expert]

class InterviewDetailView(generics.RetrieveAPIView):
    """
    get interview by primary key
    단일 질병 인터뷰 반환
    """

    serializer_class = InterviewSerializer

    def get_queryset(self):
        queryset = Interview.objects.all()
        return queryset


class InterviewByDiseaseView(generics.ListAPIView):
    """
    get interview list by disease
    질병명에 따른 인터뷰 목록
    """
    serializer_class = InterviewSerializer

    def get_queryset(self):
        disease = self.kwargs['disease']
        queryset = Interview.objects.filter(disease__disease_name=disease)
        return queryset


class InterviewByKeywordView(generics.ListAPIView):
    """
    get interview list by disease & keyword
    질병명, 키워드에 따른 인터뷰 목록
    """
    serializer_class = InterviewSerializer

    def get_queryset(self):
        disease = self.kwargs['disease']
        keyword = self.kwargs['keyword'].split(',')

        queryset = Interview.objects.filter(disease__disease_name=disease)
        for i in range(len(keyword)):
            # keyword 수만큼 filter 적용해서 모든 keyword 가 포함된 결과 반환
            queryset = queryset.filter(keyword__keyword=keyword[i])

        return queryset


class InterviewByAgeView(generics.ListAPIView):
    """
    get interview list by disease & interviewee age
    질병명에 따른 연령별 인터뷰 목록
    """
    serializer_class = InterviewSerializer

    def get_queryset(self):
        disease = self.kwargs['disease']
        queryset = Interview.objects.filter(
            disease__disease_name=disease).order_by('interviewee_age')
        return queryset


class InterviewByExpertView(generics.ListAPIView):
    """
    get interview list by disease & expert
    질병명에 따른 전문가 인터뷰 목록
    """
    serializer_class = InterviewSerializer

    def get_queryset(self):
        disease = self.kwargs['disease']
        queryset = Interview.objects.filter(
            disease__disease_name=disease, person__is_expert=True)
        return queryset
