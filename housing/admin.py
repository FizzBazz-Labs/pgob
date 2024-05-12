from django.contrib import admin

from housing.models import Housing, HousingPerson


class HousingPersonInline(admin.TabularInline):
    model = HousingPerson
    extra = 1


@admin.register(Housing)
class HousingAdmin(admin.ModelAdmin):
    inlines = [HousingPersonInline]
    list_display = (
        'building_type',
        'house_number',
        'apartment_tower',
        'building_admin_name',
        'apartment_number',
        'apartment_floor',
        'is_owner',
        'owner_name',
        'owner_phone_number',
        'created_by',
    )
