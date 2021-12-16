from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Plant, Disease, Canopy, Capture, DiseaseImage, PlantImage
)


class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'canopy', 'is_active', 'created_on')

    def canopy_view(self, obj):
        if obj.canopy:
            return format_html(
                '<a href="/admin/accounts/user/{}/change/">{}</a>',
                obj.canopy.pk, obj.canopy.name
            )
        else:
            return format_html(
                '<a href="#">-</a>',
            )


class PlantImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant_view', 'image')

    def plant_view(self, obj):
        return format_html(
            '<a href="/admin/api/plant/{}/change/">{}</a>',
            obj.plant.pk, obj.plant.name
        )


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_on')


class DiseaseImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'disease_view', 'image')

    def disease_view(self, obj):
        return format_html(
            '<a href="/admin/api/disease/{}/change/">{}</a>',
            obj.disease.pk, obj.disease.name
        )


class CanopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'is_active', 'created_on')


class CaptureAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'x_axis', 'y_axis', 'user_view', 'is_active', 'created_on')

    def user_view(self, obj):
        return format_html(
            '<a href="/admin/accounts/user/{}/change/">{}</a>',
            obj.user.pk, obj.user.username
        )


admin.site.register(Plant, PlantAdmin)
admin.site.register(DiseaseImage, DiseaseImageAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(PlantImage, PlantImageAdmin)
admin.site.register(Canopy, CanopyAdmin)
admin.site.register(Capture, CaptureAdmin)
