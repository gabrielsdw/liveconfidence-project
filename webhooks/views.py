from random import randint
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from services.callmebot import CallMeBot
from ai.workflows import ChatBotWorkflow
from ai.utils import format_dict, format_chat_history
from . import serializers


class ChatbotWebhookApiView(APIView):
    
    def __init__(self, **kwargs) -> None:
        self.__callmebot_service = CallMeBot()
        super().__init__(**kwargs)

    def post(self, request: Request) -> Response:
        data = request.data
        
        model = data.get('model')
        if not model:
            return Response(
                {"msg": "Error, send the model field"},
                status=status.HTTP_400_BAD_REQUEST
            )
        model_info = model.get('model_info')
        model_physics_characteristics = model.get('physics_characteristics')
        
        chat_history = data.get('messages')

        serializer = serializers.ChatbotWebhookRequestSerializer(
            data={
                "chat_history": chat_history,
                "model_info": model_info,
                "model_physics_characteristics": model_physics_characteristics
            }
        )
        if serializer.is_valid():
            chatbot_service = ChatBotWorkflow()
            
            model_info_formatted = format_dict(dict(serializer.validated_data.get('model_info')))
            model_physics_characteristics_formatted = format_dict(dict(serializer.validated_data.get('model_physics_characteristics')))

            response = chatbot_service.run({
                "chat_history": list(serializer.validated_data.get('chat_history')),
                "model_info": model_info_formatted ,
                "model_physics_characteristics": model_physics_characteristics_formatted,
            })
            id = randint(0, 100)

            chat_history_message = f"""
            CHAT HISTORY - {id}
            {format_chat_history(list(serializer.validated_data.get('chat_history')))}
            """
            print(chat_history_message)
            agent_message = f"""
            AGENT RESPONSE - {id}
            {response.get('agent_response')}
               
            """
            final_response_message = f"""
            FINAL RESPONSE - {id}           
            
            {response.get('final_response')}                
            
            """

            self.__callmebot_service.send_message(chat_history_message)
            self.__callmebot_service.send_message(agent_message)
            self.__callmebot_service.send_message(final_response_message)

            print("------------------------------ AGENT RESPONSE ------------------------------")
            print(response.get('agent_response'))
            print("------------------------------ END AGENT RESPONSE ------------------------------")
            print('\n'*5)

            print("------------------------------ FINAL RESPONSE ------------------------------")            
            response = response.get('final_response')
            print(response)
            print("------------------------------ END FINAL RESPONSE ------------------------------")
            print('\n'*5)
            return Response(
                {
                    "data": {
                        "ai_response": str(response)
                    } 
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                "msg": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
