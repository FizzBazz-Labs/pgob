from django.contrib import admin

from medical_histories.models import MedicalHistory


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    ...