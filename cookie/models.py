from django.db import models

# Create your models here.
class Cookie(models.Model):
    title = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    serial = models.CharField(max_length=1024, unique=True, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='media/images/cookie')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)