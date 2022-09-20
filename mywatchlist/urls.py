from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_xml, show_xml_by_id
from mywatchlist.views import show_json, show_json_by_id


app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('html/', show_mywatchlist, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]