from django.conf.urls import url
from django.contrib import admin
from oppey_ml_api.views import OppeyMLAppView, OppeyMLApiView


urlpatterns = [
    url(r'^$', OppeyMLAppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/oppey/', OppeyMLApiView.as_view(), name='oppey'),
]
