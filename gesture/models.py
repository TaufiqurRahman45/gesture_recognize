from django.db import models


class GestureImage(models.Model):
    image = models.ImageField(upload_to="gestures")
    time = models.IntegerField()
