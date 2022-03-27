from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=64)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"