from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('cake', 'Cake'),
        ('brownie', 'Brownie'),
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
