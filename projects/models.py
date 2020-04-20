from django.db import models
from django.contrib.auth.models import User

categories = (
    ('Animals', 'Animals'),
    ('Arts', 'Arts & Culture'),
    ('Community', 'Community & Family'),
    ('Education', 'Education'),
    ('Environment', 'Environment'),
    ('Disaster', 'Disaster Relief'),
    ('Health', 'Health & Medical'),
    ('Human', 'Human Services'),
    ('Housing', 'Housing'),
)


class Project(models.Model):
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254, choices=categories)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    added_by = models.ForeignKey(User, null=True, default="1", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return "{0} {1}".format(
            self.name, self.added_by)
