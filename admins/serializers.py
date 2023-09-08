from rest_framework import serializers
from .models import Admin


class AdminSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Admins
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
             'image', 'is_owner',
]
