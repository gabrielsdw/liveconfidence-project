from rest_framework import serializers


class ChatbotWebhookRequestSerializer(serializers.Serializer):
    model_info = serializers.JSONField(required=True)
    model_physics_characteristics = serializers.JSONField(required=True)
    chat_history = serializers.ListField(required=True)
