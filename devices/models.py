from django.db import models

TYPES = (("JSON", "json"), ("PLAINTEXT", "plaintext"), ("BINARY", "binary"))


class Property(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    type = models.CharField(choices=TYPES, max_length=200)


class Device(models.Model):
    name = models.CharField(max_length=200)
    properties = models.ManyToManyField(to=Property, related_name="devices")
