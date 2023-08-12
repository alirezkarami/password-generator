from django.db import models
from password.models import Password


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    pass_id = models.ManyToManyField(Password)
