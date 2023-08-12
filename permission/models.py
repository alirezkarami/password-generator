from django.db import models
from password.models import Password
from user.models import UserCust


class Group:
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(UserCust)
