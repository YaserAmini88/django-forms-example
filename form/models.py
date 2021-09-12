from django.db import models


class formModel(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email