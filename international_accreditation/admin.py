from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from international_accreditation.models import InternationalAccreditation as International


class InternationalResource(resources.ModelResource):
    class Meta:
        model = International


@admin.register(International)
class InternationalAdmin(ImportExportModelAdmin):
    resource_classes = [InternationalResource]
