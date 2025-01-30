from django.urls import path
from . import views

urlpatterns = [
    path("webhook/chatbot/", views.ChatbotWebhookApiView.as_view()),
]
