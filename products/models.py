from django.db import models
from django.shortcuts import reverse

from .base_model import BaseModel
from categories.models import Category


class Product(BaseModel):
   name = models.CharField(max_length=100)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
   price = models.DecimalField(max_digits=10, decimal_places=2)
   desc = models.TextField()
   image = models.ImageField(upload_to='products_image/')

   def __str__(self):
      return self.name

   def get_detail_url(self):
      return reverse('products:detail', args=[self.pk])

   def get_delete_url(self):
      return reverse('products:delete', args=[self.pk])

   def get_update_url(self):
      return reverse('products:update', args=[self.pk])