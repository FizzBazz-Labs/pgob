from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from international_accreditation.models import InternationalAccreditation as International


class InternationalResource(resources.ModelResource):
    class Meta:
        model = International


@admin.register(International)
class InternationalAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'passport_id', 'position', 'id')
    list_filter = ('position', 'country', 'status')
    resource_classes = [InternationalResource]
    search_fields = ['first_name', 'last_name', 'passport_id', 'id']
