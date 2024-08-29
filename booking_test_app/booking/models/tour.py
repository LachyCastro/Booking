from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.name)