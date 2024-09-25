from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","username", "password", "name", "cpf","role","phone","address", "expertise", "experience"]

class UserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["cpf"]