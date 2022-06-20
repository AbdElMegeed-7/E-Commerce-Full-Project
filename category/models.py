from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/category')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
