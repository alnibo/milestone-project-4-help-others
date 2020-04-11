from django.db import models

categories = (
    ('Education', 'Education'),
    ('Housing', 'Housing'),
    ('Health', 'Health'),
)


class Project(models.Model):
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254, choices=categories)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
