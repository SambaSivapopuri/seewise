from rest_framework import serializers
from .models import Machine, ProductionLog
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class ProductionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionLog
        fields = '__all__'

class OEESerializer(serializers.Serializer):
    availability = serializers.FloatField()
    performance = serializers.FloatField()
    quality = serializers.FloatField()
    oee = serializers.FloatField()
