from dipex.models import Disease, DiseaseKeyword, Interview, Person

from rest_framework import serializers


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        exclude = ('id',)


class DiseaseKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseKeyword
        exclude = ('id', 'disease')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'organization', 'is_expert',
                  'research_field', 'expert_bio', 'profile_photo')


class InterviewSerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer(read_only=True)
    keyword = DiseaseKeywordSerializer(many=True, read_only=True)
    person = PersonSerializer(read_only=True)

    class Meta:
        model = Interview
        fields = '__all__'
