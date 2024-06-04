from django.contrib import admin

from .models import HelpSection, HelpSectionItem


class HelpSectionItemInline(admin.TabularInline):
    model = HelpSectionItem
    extra = 0


@admin.register(HelpSection)
class HelpSectionAdmin(admin.ModelAdmin):
    inlines = [HelpSectionItemInline]
    list_display = ['title']
    search_fields = ['title']
