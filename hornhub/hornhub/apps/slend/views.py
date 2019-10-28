from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

def snake_def(request):
	return render(request, 'slend/snake.html')
