from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

def analys_def(request):
	return render(request, 'analys/analys.html')

def leave_coment(request, analys_id):
	try:
		a = Anslys.objects.get( id = analys_id )

	except:
		raise Http404('Статья ненайдена')

	a.coment_set.create(coment_auther = request.POST['name'], coment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('analys:analys', args = (a.id,)) )
