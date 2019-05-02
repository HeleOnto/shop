from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name


