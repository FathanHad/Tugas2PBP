from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchlistMovies
# Create your views here.
def show_mywatchlist(request):
    data_film_mywatchlist = WatchlistMovies.objects.all()
    context = {
        'list_film': data_film_mywatchlist,
        'nama': 'Fathan Hadyan',
        'student_id':'2106751940'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistMovies.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistMovies.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchlistMovies.objects.filter(pk=id)    
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = WatchlistMovies.objects.filter(pk=id)    
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



