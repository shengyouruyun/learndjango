from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):

# 	if request.method == 'GET':
# 		return HttpResponse('I am called from a get Request')
# 	elif request.method == 'POST':
# 		return HttpResponse('I am called from a post Request')

from django.views.generic import View 
from django.shortcuts import render

class Index(View):
	def get(self, request):
		params = {}
		params['name'] = "Django"
		return render(request, 'base.html', params)
	




	def post(self, request):
		return HttpResponse('I am called from a post Request')




