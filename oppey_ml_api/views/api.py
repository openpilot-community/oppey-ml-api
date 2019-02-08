
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot.ext.django_chatterbot import settings
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from oppey_ml_api.models import DiscordMessages
import logging
logging.basicConfig(level=logging.INFO)
oppey_chatbot = ChatBot(**settings.CHATTERBOT)

class ApiChatView(View):
    """
    Provide an API endpoint to interact with OppeyML.
    """
    
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = oppey_chatbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': oppey_chatbot.name
        })

class ApiTrainView(View):
    """
    Provide an API endpoint to interact with OppeyML.
    """
    
    def get(self, request, *args, **kwargs):
      print("Training Oppey from latest messages...")
      messages_query = DiscordMessages.objects.order_by('-created_at')[:5]
      messages = messages_query.values_list('content', flat=True)
      messages = list(messages)
      print()
      trainer = ListTrainer(oppey_chatbot)
      trainer.train(messages)
      return JsonResponse({
        'message': 'Oppey has been successfully trained.',
        'trained': messages
      }, status=200)