from .models import Producto
from rest_framework import serializers

# Creamos un serializador desde una clase
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Producto
        fields = ['name', 'stock']