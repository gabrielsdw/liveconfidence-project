from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from ai.workflows import ChatBotWorkflow


class ChatbotWebhookApiView(APIView):
    
    def post(self, request: Request) -> Response:
        data = request.data
        print(data)
        chatbot_service = ChatBotWorkflow()
        """
        response = chatbot_service.run({
            "chat_history": "",
            "characteristics_emotionals": "",
            "characteristics_fisics": "",
        })
        """
        response = ''
        return Response(
            {"data": str(response)},
            status=status.HTTP_200_OK
        )