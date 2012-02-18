from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from artikel.models import Artikel

def index(request):
    try:
        articles = Artikel.objects.order_by('-art_pub_date')[:10]
    except Artikel.DoesNotExist:
        articles = "No content available!"
        
    return render_to_response('index.html', {"articles":articles})

def tagged(request, tag_id):
	try:
		content = Artikel.objects.filter(art_tags__icontains=tag_id)
	except Artikel.DoesNotExist:
		raise Http404
		
	return render_to_response('tagged.html', {"articles": content, "tag_id":tag_id})

