from rest_framework import serializers
from api.models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = "__all__"
        lookup_field = "slug"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        lookup_field = "name"
