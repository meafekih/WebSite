
from rest_framework import serializers
from .models import product


class productSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price= serializers.FloatField()

    def create(self, validated_data):
        return product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.price= validated_data.get('price',instance.price)
        instance.save()
        return instance
    
    

    

