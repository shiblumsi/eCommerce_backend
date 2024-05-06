from rest_framework import serializers
from .models import CustomUser


class VendorSignupSerilizer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password2']

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password do not matched!")
        return data

    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        password = validated_data.pop('password')
        return CustomUser.objects.create_vendor(password=password, **validated_data)
        
        
class CustomerSignupSerilizer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password2']

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password do not matched!")
        return data

    def create(self, validated_data):
        password2 = validated_data.pop('password2')
        password = validated_data.pop('password')
        return CustomUser.objects.create_customer(password=password, **validated_data)



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
