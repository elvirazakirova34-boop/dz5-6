from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Order
        fields = '__all__'

        
