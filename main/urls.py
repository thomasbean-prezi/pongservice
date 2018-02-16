from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^players/$', views.players, name='players'),
    url(r'^players/(?P<player_id>[0-9]+)/$', views.player_detail, name='player_detail'),
    url(r'^fields/$', views.fields, name='fields'),
    url(r'^api/players/$', views.api_players, name='api_players'),
    url(r'^api/players/(?P<player_id>[0-9]+)/$', views.api_player_detail, name='api_player_detail'),

]
