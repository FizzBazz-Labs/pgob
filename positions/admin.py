from django.contrib import admin

from positions.models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    ...
