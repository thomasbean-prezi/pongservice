from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^players/$', views.players, name='players'),
    url(r'^players/(?P<player_id>[0-9]+)/$', views.player_detail, name='player_detail'),
    url(r'^fields/$', views.fields, name='fields'),
    url(r'^api/players/$', views.api_players, name='api_players'),
    url(r'^api/fields/$', views.api_fields, name='api_fields'),
    url(r'^api/matches/$', views.api_matches, name='api_matches'),
    url(r'^api/players/(?P<player_id>[0-9]+)/$', views.api_player_detail, name='api_player_detail'),
    url(r'^api/fields/(?P<field_id>[0-9]+)/$', views.api_field_detail, name='api_field_detail'),
    url(r'^api/matches/(?P<match_id>[0-9]+)/$', views.api_match_detail, name='api_match_detail'),
    url(r'^api/remove-invalid-matches/$', views.api_remove_invalid_matches, name='api_remove_invalid_matches'),
]
