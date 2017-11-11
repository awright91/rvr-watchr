
from django.conf.urls import url, include
from rivers.views import RiverDetail, state_index
from django.conf.urls.static import static

from river_subs.views import RiverSubscribe



urlpatterns = [
    url(r'^(?P<state_abrv>[\w-]+)/$', state_index, name="state_index"),
    url(r'^(?P<state_abrv>[\w-]+)/(?P<pk>[-\w]+)/$', RiverDetail, name="river_detail"),
    url(r'^(?P<state_abrv>[\w-]+)/(?P<pk>[-\w]+)/subscribe$', RiverSubscribe, name="river_subscribe"),
]
