from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^contribute$', contribute, name="contribute"),
    url(r'^add$', add_quote, name="add"),
    url(r'^admin$', admin_quote, name="admin"),
    url(r'^approve/(?P<quote_id>\d+)$', approve_quote, name="approve"),
    url(r'^delete/(?P<quote_id>\d+)$', delete_quote, name="delete"),
    url(r'^add_tag/(?P<quote_id>\d+)$', add_tag, name="add_tag"),
]