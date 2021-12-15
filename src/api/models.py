from django.db import models


""" PLANTS > DISEASES > CANOPIES """


class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default="Information not available.")
    canopy = models.ForeignKey('Canopy', on_delete=models.SET_NULL, null=True, blank=False)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PlantImage(models.Model):
    plant = models.ForeignKey('Plant', models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/plants/')

    def __str__(self):
        return self.plant.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(PlantImage, self).delete(*args, **kwargs)


class Disease(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default="Information not available.")

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DiseaseImage(models.Model):
    disease = models.ForeignKey('Disease', models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/diseases/')

    def __str__(self):
        return self.disease.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(DiseaseImage, self).delete(*args, **kwargs)


class Canopy(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/canopies/')
    description = models.TextField(null=True, blank=True, default="Information not available.")

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Canopy, self).delete(*args, **kwargs)


""" CAPTURES """


class Capture(models.Model):
    image = models.ImageField(upload_to='images/captures/')
    x_axis = models.CharField(max_length=255, null=True, blank=True)
    y_axis = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.url

    def delete(self, *args, **kwargs):
        self.image.delete(save=True)
        super(Capture, self).delete(*args, **kwargs)
