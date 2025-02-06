from django.db import models
from django.shortcuts import reverse

from products.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='categories_image/')

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('categories:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('categories:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('categories:delete', args=[self.pk])

    def get_delete_list_url(self):
        return reverse('categories:delete_list', args=[self.pk])
