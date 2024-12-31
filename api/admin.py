from django.contrib import admin
from api.models import Category, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # list_display = "__all__"

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # list_display = "__all__"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
