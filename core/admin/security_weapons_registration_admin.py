# from django.contrib import admin
# from django.utils.translation import gettext_lazy as _

# from core.models import SecurityWeaponAccreditation


# @admin.register(SecurityWeaponAccreditation)
# class SecurityWeaponAccreditationAdmin(admin.ModelAdmin):
#     ...

# fieldsets = [
#     (_('control date'), {
#         'fields': [
#             'date_control',
#             'time_control',
#             'disclaimer_accepted',
#         ]
#     }),

#     (_('weapon data'), {
#         'fields': [
#             'weapon',
#             'brand',
#             'model',
#             'weapon_type',
#             'serial_number',
#             'caliber',
#             'magazine_quantity',
#             'ammunition_quantity',
#         ]
#     }),

#     (_('communication equipment data'), {
#         'fields': [
#             'communication_radio',
#             'communication_model',
#             'communication_type',
#             'communication_serial',
#             'communication_frequency',
#         ]
#     })
# ]

# def render_change_form(self, request, context, *args, **kwargs):

#     context['adminform'].form.fields['weapon_type'].widget = forms.CheckboxSelectMultiple(
#         choices=[
#             (item.id, item.name)
#             for item in WeaponType.objects.all()
#         ]
#     )

#     context['adminform'].form.fields['communication_type'].widget = forms.CheckboxSelectMultiple(
#         choices=[
#             (item.id, item.name)
#             for item in CommunicationType.objects.all()
#         ]
#     )
#     return super().render_change_form(request, context, *args, **kwargs)
