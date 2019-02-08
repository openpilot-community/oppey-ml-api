
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
import re
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
      messages_query = DiscordMessages.objects.filter(trained=False).order_by('created_at')
      # messages = messages_query.values_list('content', flat=True)
      messages_to_train = []
      
      trainer = ListTrainer(oppey_chatbot)
      
      for message in messages_query:
        message.trained = True
        
        message_content = re.sub(r'\<\@\![0-9]+\>', '', message.content)
        message_content = re.sub(r'\<\@\[0-9]+\>', '', message.content)
        # message.save()
        message_content = ' '.join(message_content.split())
        message_content = message_content.replace(' ,',',')
        messages_to_train.append(message_content)
      print(messages_to_train)
      trainer.train(messages_to_train)
      return JsonResponse({
        'message': 'Oppey has been successfully trained.',
        'trained': len(messages_to_train)
      }, status=200)