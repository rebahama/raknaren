from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """ For user authentication"""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_name = serializers.ReadOnlyField(source='profile.name')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id',
            'profile_name',
            'username',

        )