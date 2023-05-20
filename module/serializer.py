
from rest_framework import serializers
from .models import product


class productSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price= serializers.FloatField()

    def create(self, validated_data):
        return product.objects.create(**validated_data)

    
    

    

