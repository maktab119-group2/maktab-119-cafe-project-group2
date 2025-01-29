from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.created_at}"