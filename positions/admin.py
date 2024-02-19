from django.contrib import admin

from positions.models import Position, SubPosition


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


@admin.register(SubPosition)
class SubPositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
