from rest_framework import permissions

class IsInSpecificGroup(permissions.BasePermission):
    group_name = 'admins'
    
    def has_permission (self, request, view):
        return request.user.groups.filter(name = self.group_name).exists()
