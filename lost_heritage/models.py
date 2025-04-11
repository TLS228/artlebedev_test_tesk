from django.db import models


class LostObject(models.Model):
    native_id = models.CharField(max_length=50, unique=True)
    register_number = models.CharField(max_length=100)
    name = models.TextField()
    description = models.TextField(blank=True)
    identifying_characteristics = models.TextField(blank=True)
    material = models.CharField(max_length=255, blank=True)
    origin_place = models.CharField(max_length=255, blank=True)
    register_type = models.CharField(max_length=255)
    registration_date = models.DateField()
    loss_place_description = models.TextField(blank=True)
    rnom_register_number = models.CharField(max_length=100, blank=True)
    dokm_base_document = models.TextField(blank=True)
    category = models.CharField(max_length=255, blank=True)
    museum = models.CharField(max_length=255, blank=True)
    creator = models.CharField(max_length=255, blank=True)
    date_creator = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.register_number} — {self.name[:50]}"
