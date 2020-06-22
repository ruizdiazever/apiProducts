from .models import Producto
from rest_framework import serializers

# Creamos un serializador desde una clase
# Sirve para serializar python a json
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # Con '__all__' le decimos que use todos los campos
        fields = '__all__'