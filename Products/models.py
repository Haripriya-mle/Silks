# products/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class LiveProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=1, is_active=True)

class Product(models.Model):
    STATUS_CHOICES = [
        (1, 'Live'),
        (0, 'Deleted'),
    ]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    sku = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    priority=models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # The default manager
    live = LiveProductManager()  # Custom manager for live products

    def __str__(self):
        return self.name
