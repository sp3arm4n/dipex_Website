from django.contrib import admin

from dipex.models import Person, Disease, DiseaseKeyword, Interview

admin.site.register(Person)
admin.site.register(Disease)
admin.site.register(DiseaseKeyword)


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    readonly_fields = ['video_path_encrypt']
