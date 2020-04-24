from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Donations(models.Model):
    user = models.ForeignKey(User, null=True, default="1", on_delete=models.SET_DEFAULT)
    project = models.ForeignKey(Project)
    amount = models.IntegerField(blank=False)

    def __str__(self):
        return self.user
