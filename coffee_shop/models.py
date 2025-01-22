from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    serving_time_period = models.CharField(max_length=50, null=True, blank=True)
    estimated_cooking_time = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    def __str__(self):
        return self.name
