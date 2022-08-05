from django.db import models
from django.db.models import JSONField


class Input(models.Model):
    value = JSONField()

    def __str__(self):
        return self.value