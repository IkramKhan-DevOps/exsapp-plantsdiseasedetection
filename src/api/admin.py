from django.contrib import admin
from .models import (
    Plant, Disease, Canopy, Capture, DiseaseImage, PlantImage
)

admin.site.register(Plant)
admin.site.register(DiseaseImage)
admin.site.register(Disease)
admin.site.register(PlantImage)
admin.site.register(Canopy)
admin.site.register(Capture)
