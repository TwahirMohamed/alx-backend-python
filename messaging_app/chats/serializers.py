from rest_framework import serializers
from .models import User, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'user_id', 'username', 'first_name', 'last_name',
            'email', 'phone_number', 'role', 'created_at', 'full_name'
        ]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = Message
        fields = [
            'message_id', 'sender', 'sender_name', 'conversation',
            'message_body', 'sent_at'
        ]

    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message body cannot be empty.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True, source='messages')

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']

