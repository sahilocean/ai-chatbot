from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False,allow_null=True, allow_blank=True)

    class Meta:
        model = User
        fields = ("username",'first_name','last_name','password','email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
