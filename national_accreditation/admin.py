from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from national_accreditation.models import NationalAccreditation as National


class NationalResource(resources.ModelResource):
    class Meta:
        model = National


@admin.register(National)
class NationalAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'passport_id', 'position', 'type', 'id')
    list_filter = ('position', 'status', 'country')
    readonly_fields = ('created_at', 'updated_at')
    resource_classes = [NationalResource]
    search_fields = ['first_name', 'last_name', 'passport_id', 'id']
