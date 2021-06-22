from django.db import models
from django.db.models.deletion import CASCADE

from django.urls import reverse


from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.template.defaultfilters import slugify

class MyManager(models.Manager):
    def get_queryset(self):#all()
        return super().get_queryset().order_by('date')



class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField()
    slug=models.SlugField(max_length=120)
    
    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('name',kwargs={'slug':self.slug})



    def save(self, *args, **kwargs): # new
        
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    


    
    def __str__(self):
        return self.name


class Feedback(models.Model):
    customer_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    details=models.TextField()
    
    happy=models.BooleanField()
    date=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.customer_name


# Create your models here.
