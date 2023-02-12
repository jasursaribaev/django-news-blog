from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name
    
class News(models.Model):
    
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
    
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_news')
    
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)
    
    class Meta:
        ordering = ["-published_time"]
        
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    arrival_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject