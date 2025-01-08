
from django.contrib.auth.models import AbstractUser
from django.db import models


class MemberUser(AbstractUser):
    # joined_date = models.DateField(default=now)  # set date as default today

    # Add any other fields specific to your Member model

    def __str__(self):
        return self.username