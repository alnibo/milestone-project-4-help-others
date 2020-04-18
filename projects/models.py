from django.db import models

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

    def __str__(self):
        return self.name
