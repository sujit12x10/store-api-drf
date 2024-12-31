from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.ImageField(upload_to="categories")

    class Meta:
        ordering = ("name",)
        # varbose_name = "category"
        # # varbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    category = models.ManyToManyField(Category, related_name="products")
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url1 = models.TextField()
    image_url2 = models.TextField(blank=True)
    image_url3 = models.TextField(blank=True)
    image_url4 = models.TextField(blank=True)
    decription = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
