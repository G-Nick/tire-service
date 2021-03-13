from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=100)

    class Meta:
        ordering = ["brand"]

    def __str__(self):
        return self.brand
