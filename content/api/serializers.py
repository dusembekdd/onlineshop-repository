from rest_framework import serializers
from content.models import product
from content.models import Category


class productSerializer(serializers.ModelSerializer):
    category_gender = serializers.CharField(source='category')

    class Meta:
        model = product
        fields = ['name', 'url', 'price', 'image', 'category_gender']