from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from . models import Stat, Coment

def index(request):
	last_stat = Stat.objects.order_by('-pub_date')[:5]
	return render(request, 'blog/list.html', {'last_stat': last_stat})

def detail(request, stat_id):
	try:
		a = Stat.objects.get( id = stat_id )

	except:
		raise Http404('Статья ненайдена')

	last_coment = a.coment_set.order_by('-id')[:10]	

	return render(request, 'blog/detail.html', {'stat': a, 'last_coment': last_coment})



def leave_coment(request, stat_id):
	try:
		a = Stat.objects.get( id = stat_id )

	except:
		raise Http404('Статья ненайдена')

	a.coment_set.create(coment_auther = request.POST['name'], coment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('blog:detail', args = (a.id,)) )
