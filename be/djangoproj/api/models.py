from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
