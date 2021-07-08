import base64
import os

from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=190)
    e_mail = models.CharField(max_length=190, unique=True)
    phone_number = models.CharField(max_length=190, unique=True)
    mobile_phone_number = models.CharField(max_length=190, unique=True)
    organization = models.CharField(max_length=190, blank=True)
    major = models.CharField(max_length=190, blank=True)
    # 전문가 여부
    is_expert = models.BooleanField(default=False)
    research_field = models.CharField(max_length=190, blank=True)
    expert_bio = models.TextField(blank=True)
    profile_photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    # 질병 생성은 DISEASE_LIST 에 정의된 질병만 생성 가능
    DISEASE_LIST = [
        ("당뇨병", "당뇨병"),
        ("유방암", "유방암"),
        ("위암", "위암"),
        ("우울증", "우울증"),
        ("호스피스 완화의료", "호스피스 완화의료"),
        ("치매", "치매")
    ]

    disease_name = models.CharField(max_length=190, choices=DISEASE_LIST, unique=True)
    disease_description = models.TextField(blank=True)

    def __str__(self):
        return self.disease_name


class DiseaseKeyword(models.Model):
    disease = models.ForeignKey('Disease', on_delete=models.DO_NOTHING, related_name="disease")
    keyword = models.CharField(max_length=190)
    keyword_description = models.TextField(blank=True)

    def __str__(self):
        # "질병명 - 키워드" 로 표시
        return f"{self.disease} - {self.keyword}"

    class Meta:
        # disease-keyword 쌍으로 unique 속성 추가
        unique_together = (("disease", "keyword"),)


class Interview(models.Model):
    disease = models.ForeignKey('Disease', on_delete=models.DO_NOTHING, related_name="disease_interview")
    person = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
    # 질병별 키워드 (M2M)
    keyword = models.ManyToManyField('DiseaseKeyword')

    # 인터뷰 제목
    title = models.CharField(max_length=190)
    # 관리용 원본 비디오 파일
    # 업로드 경로: media/video
    # TODO: unique는 파일이름에 영향 X, 빈칸으로 들어가면 unique 적용
    video_path = models.FileField(max_length=254, upload_to="video_original", blank=True, unique=True)
    # API용 암호화된 비디오 파일
    # 업로드 경로: media/video_encrypt
    video_path_encrypt = models.FileField(max_length=254, upload_to="video_encrypt", blank=True)
    # 자막
    subtitle = models.TextField()
    # 인터뷰 상 나이 (0일 경우, 미분류 처리)
    interviewee_age = models.IntegerField(default=0)
    # 진단 나이 (0일 경우, 미분류 처리)
    diagnosis_age = models.IntegerField(default=0)

    def encrypt_video_base64(self):
        # 비디오 파일 이름을 base64로 암호화
        # video_path_encrypt에 저장

        # TODO: base64 encrypt시 / 와 \ 등 제거 -> replace

        binary_video_path = str(self.video_path).encode("UTF-8")
        base64_video_path = base64.b64encode(binary_video_path)

        encrypt_file_name = f"{base64_video_path.decode('ascii')}.{str(self.video_path).split('.')[1]}"

        # replace / with _ to prevent divided by directory
        encrypt_file_name.replace('/', '_')
        self.video_path_encrypt.save(encrypt_file_name, self.video_path, save=False)

    def check_video_format(self):
        # TODO: Video 업로드 시, wma|wmv 일 경우, 비디오 반환 후 업로드 필요
        # TODO: 비디오 전환이 어려울 것 같아 type check 정도로만 하는게 좋을 듯
        pass

    def save(self, *args, **kwargs):
        if self.video_path != '':
            # encrypt video path with base64
            self.encrypt_video_base64()
        super(Interview, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
