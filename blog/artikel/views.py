# Create your views here.

from artikel.models import Artikel, Podcast
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import artikel.config as settings


def index(request, article_id):
    try:
        content = Artikel.objects.get(pk=article_id)
    except Artikel.DoesNotExist:
        raise Http404
        
        
    try:
        podcasts = Podcast.objects.filter(article__exact=content.id)
        podcasts_exist = True
    
    except Podcast.DoesNotExist:
        podcasts = None
        podcasts_exist = False
        
    return render_to_response('articles.html', {"article":content,
        "podcasts":podcasts,
        "podcasts_exist":podcasts_exist, 
	"settings":settings,
    })
    
def tagged(request, tag_id):
	try:
		content = Artikel.objects.filter(art_tags__icontains=tag_id)
	except Artikel.DoesNotExist:
		raise Http404
		
	return render_to_response('tagged.html', {"articles": content, "tag_id":tag_id})
