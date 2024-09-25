from rest_framework import permissions


class IsFuncionario(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Funcionario").exists()

class IsDiretor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Diretor").exists()

class IsRecrutador(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Recrutador").exists()
