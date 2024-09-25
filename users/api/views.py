from typing import Any
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from users.api.serializers import UserSerializer


from users.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAdminUser()]
        return super().get_permissions()

    def create(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            usuario = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                name=serializer.validated_data['name'],
                cpf=serializer.validated_data['cpf'],
                role=serializer.validated_data['role'],
                phone=serializer.validated_data['phone'],
                address=serializer.validated_data['address'],
                expertise=serializer.validated_data['expertise'],
                experience=serializer.validated_data['experience']
            )

            grupo_funcionarios, created = Group.objects.get_or_create(name="Funcionario")
            usuario.groups.add(grupo_funcionarios)
            usuario.save()

            dados_saida = UserSerializer(usuario)

            return Response(dados_saida.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

