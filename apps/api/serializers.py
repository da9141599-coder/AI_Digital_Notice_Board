from rest_framework import serializers
from apps.accounts.models import User
from apps.notice.models import Notice

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']


class NoticeSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Notice
        fields = [
            'id',
            'title',
            'content',
            'attachment',
            'created_by',
            'created_at',
            'expires_at',
            'category',
            'priority',
        ]


class AIPredictionSerializer(serializers.Serializer):
    text = serializers.CharField()
