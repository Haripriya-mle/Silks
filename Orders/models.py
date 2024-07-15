# orders/models.py

from django.conf import settings
from Products.models import Product
from Customers.models import Customer
from django.db import models

class Order(models.Model):
    DELETE_CHOICES = [
        (1, 'Live'),
        (0, 'Deleted'),
    ]
    STATUS_CHOICES = [
        (1, 'Order Confirmed'),
        (2, 'Order Processed'),
        (3, 'Order Delivered'),
        (4, 'Order Rejected'),
    ]
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, related_name='orders')
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    status = models.IntegerField(choices=DELETE_CHOICES, default=1)

    def __str__(self):
        return f"Order {self.order_id} by {self.owner.name}"

class OrderItem(models.Model):
    owner = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.SET_NULL,null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
