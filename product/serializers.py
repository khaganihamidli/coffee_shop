from rest_framework import serializers
from .models import Coffee


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'