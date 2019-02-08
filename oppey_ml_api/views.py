import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot.ext.django_chatterbot import settings
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging
logging.basicConfig(level=logging.INFO)

class OppeyMLAppView(TemplateView):
    template_name = 'app.html'


class OppeyMLApiView(View):
    """
    Provide an API endpoint to interact with OppeyML.
    """
    oppey = ChatBot(**settings.CHATTERBOT)

    def train(self, request, *args, **kwargs):
      trainer = ListTrainer(self.oppey)
      trainer.train("chatterbot.corpus.english")
      return JsonResponse({
        'message': 'Oppey has been successfully trained.'
      }, status=200)
      
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

        response = self.oppey.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.oppey.name
        })
