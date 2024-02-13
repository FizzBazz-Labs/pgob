from django.contrib import admin
from django.db import models
from django import forms
from django.utils.translation import gettext as _

from core.models import *


@admin.register(NationalAcreditation)
class NationalAcreditationAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (_('Personal Info'), {
            'fields': [ 
                'first_name',
                'last_name',
                'image',
                'nationality',
                'passport_id',
                'position',
                'media_channel',
                'institution',
                'address',
                'phone',
                'cellphone',
                'email',
                'birthday',
                'birthplace',
                'blood_type',
                'authorized_by',
                'date',
                'letter_of_authorization',
                'accreditation_type',
            ]
        })

    ]
