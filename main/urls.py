from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^(?P<player_id>[0-9]+)/$', views.player_detail, name='player_detail'),
]
