from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to="photos/cars")
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('car_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.car_name

