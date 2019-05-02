from django.db import models
from catalog.models import Product

# Create your models here.

STATUS_CHOICES = (
    (1, ("Processing")),
    (2, ("Completed"))
)


class Order(models.Model):
    ref_code = models.CharField(max_length=60)
    customer_email = models.EmailField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    date_ordered = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __str__(self):
        return '{0} - {1}'.format(self.customer_email, self.ref_code)
