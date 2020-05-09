from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''Allow users to edit their own profile'''

    def has_object_permission(self, request, view, object):
        '''Check user is trying to edit their own profile'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    '''Allows users update own status'''
    def has_object_permission(self, request, view, object):
        '''Check is trying to update own status'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.user_profile.id == request.user.id
