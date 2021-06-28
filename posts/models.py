from django.db import models


# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=30)

    def __str__(self):
        return self.title
