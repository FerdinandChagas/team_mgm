from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["id","username", "password", "name", "cpf","role","phone","address", "expertise", "experience"]