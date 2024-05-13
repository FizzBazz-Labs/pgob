from django.contrib import admin

from commerce.models import Commerce, CommerceEmployee


class CommerceEmployeeInline(admin.TabularInline):
    model = CommerceEmployee
    extra = 1


@admin.register(Commerce)
class CommerceAdmin(admin.ModelAdmin):
    inlines = [CommerceEmployeeInline]
    list_display = (
        'commercial_name',
        'company_name',
        'address',
        'admin_name',
        'admin_phone_number',
        'commerce_type',
        'commerce_type_other',
        'created_by',
    )
