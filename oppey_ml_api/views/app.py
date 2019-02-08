
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse

class AppView(TemplateView):
    template_name = 'app.html'