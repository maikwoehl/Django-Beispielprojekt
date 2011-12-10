# Create your views here.

from artikel.models import Artikel, Podcast
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

def index(request, article_id):
    try:
        content = Artikel.objects.get(pk=article_id)
    except Artikel.DoesNotExist:
        raise Http404
        
    try:
        podcast = Podcast.objects.get(pk=article_id)
        podcast_exist = True
    except Podcast.DoesNotExist:
        podcast = None
        podcast_exist = False
        
    return render_to_response('article/index.html', {"article":content,"podcast":podcast,"podcast_exist":podcast_exist})

