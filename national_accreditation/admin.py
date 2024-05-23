from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from national_accreditation.models import NationalAccreditation as National


class NationalResource(resources.ModelResource):
    class Meta:
        model = National


@admin.register(National)
class NationalAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'passport_id', 'position', 'id')
    readonly_fields = ('created_at', 'updated_at')
    resource_classes = [NationalResource]
