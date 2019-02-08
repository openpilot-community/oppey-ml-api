from django.conf.urls import url
from django.contrib import admin
from oppey_ml_api.views.app import AppView
from oppey_ml_api.views.api import ApiChatView, ApiTrainView

urlpatterns = [
    url(r'^$', AppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/chat/', ApiChatView.as_view(), name='chat'),
    url(r'^api/train/', ApiTrainView.as_view(), name='train'),
]
