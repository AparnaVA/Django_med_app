from rest_framework import serializers
from medical_store.models import medicine

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicine
        fields = '__all__'
        