from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Service(models.Model):
    CATEGORY_CHOICES = [
        ('cleaning', 'Cleaning'),
        ('it', 'IT & Software'),
        ('math', 'Mathematics Meditations'),
        ('garden', 'Garden'),
    ]

    title = models.CharField(max_length=200, unique=True)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services")
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='services/', default='services/default.jpg', blank=True)
    

    def __str__(self):
        return f"{self.title} | {self.provider.username}"