from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drink
        #field = ['id', 'name', 'Description']
        fields = '__all__'
