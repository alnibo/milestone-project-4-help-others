from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Donations(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    project = models.ForeignKey(Project)
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return self.user
