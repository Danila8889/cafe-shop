from django.db import models


class Item(models.Model):
    class Meta:
        ordering = ["name", "price"]

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)


class Table(models.Model):
    number = models.IntegerField(null=False)


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.ForeignKey(Table, related_name='orders', on_delete=models.CASCADE, default=1)
    items = models.ManyToManyField(Item, related_name="orders")
    total_price = models.IntegerField(null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='В ожидании')
