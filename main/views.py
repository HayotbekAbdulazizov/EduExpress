from traceback import print_tb
from .models import ClientRequest, University, Country, Post
from django.views.generic import DetailView, TemplateView, View
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.contrib import messages
from .forms import RequestForm
from .tg_sender import telegram_bot_sendtext

class HomePageView(View):
	def get(self,request):
		context = {
			'status':200,
			'universities': University.objects.all(),
			'countries': Country.objects.all(),
			'posts': Post.objects.all().order_by("-date")[:4],
            "form":RequestForm,
		}		    
		return render(request, 'index.html', context)

	def post(self, request):
		types = request.POST.get("type")
		print(types)
		print("Language Certificate",request.POST.get("radio-group"))
		print("IN FREE CONSULTING")
		name = request.POST.get('name')
		language_certificate = request.POST.get('language_certificate')
		phone = request.POST.get('phone')
		additional = request.POST.get('message')
		client_request = ClientRequest.objects.create(name=name, phone=phone, lang_certificate=language_certificate, additional=additional)
		messages.success(request, _(f"{client_request.name}, Your message was successfully submitted, please wait our call !"))
		telegram_bot_sendtext(f"  ClientMessage  \n Name: {client_request.name} \n Lang Certificate :  {client_request.lang_certificate}  \n Phone: +{client_request.phone} \n Link: https://www.eduexpress.info/admin/main/request/{client_request.id}/change")
		return redirect(f'/') 
	


class UniversityDetailView(View):
	def get(self,request, slug):

		object = University.objects.get(slug=slug)
		print(object.country)
		context = {
			"object":object,
			"form":RequestForm,
			# "similar_universities":University.objects.filter(country=object.country.id).order_by("?")
			"similar_universities":University.objects.all().order_by("?")[:5]
		}
		return render(request, 'university_detail.html', context)

	def post(self, request, slug):
		form  = RequestForm(request.POST)
		if form.is_valid():
			# university_id = form.cleaned_data['university_id']
			university_id = request.POST.get('university_id')
			print(form.cleaned_data)
			univ = University.objects.get(id=int(university_id))
			# univ = University.objects.get(id=)

			name = form.cleaned_data['name']
			surname = form.cleaned_data['surname']
			age = form.cleaned_data['age']
			program = form.cleaned_data['program']
			language = form.cleaned_data['language']
			degree = form.cleaned_data['degree']
			score = form.cleaned_data['score']
			print(score)
			phone = form.cleaned_data['phone']
			additional = form.cleaned_data['additional']
			requester = Request.objects.create(university=univ, name=name, surname=surname, age=age, program=program, language=language, degree=degree, score=score, phone=phone, additional=additional)
			requester.country = univ.country.name
			requester.save()
			print(name, phone, "Thing have came !!!")
			messages.success(request, _(f"{requester.name}, Your message was successfully submitted, please wait our call !"))
			print("Requester Country", requester.country)
			telegram_bot_sendtext(f'NEW USER {requester.country}',)
			return redirect(f'/') 
		else:
			form = RequestForm
			return redirect('/')





class PostDetailView(View):
	def get(self,request, slug):

		object = Post.objects.get(slug=slug)
		# print(object.)
		context = {
			"object":object,
			# "form":RequestForm,
			"similar_posts":Post.objects.all().order_by("?")[:5],
			# "similar_universities":University.objects.all().order_by("?")[:5]
		}
		return render(request, 'post_detail.html', context)

	# def post(self, request, slug):
	# 	form  = RequestForm(request.POST)
	# 	if form.is_valid():
	# 		# university_id = form.cleaned_data['university_id']
	# 		university_id = request.POST.get('university_id')
	# 		print(form.cleaned_data)
	# 		univ = University.objects.get(id=int(university_id))
	# 		# univ = University.objects.get(id=)

	# 		name = form.cleaned_data['name']
	# 		surname = form.cleaned_data['surname']
	# 		age = form.cleaned_data['age']
	# 		program = form.cleaned_data['program']
	# 		language = form.cleaned_data['language']
	# 		degree = form.cleaned_data['degree']
	# 		score = form.cleaned_data['score']
	# 		print(score)
	# 		phone = form.cleaned_data['phone']
	# 		additional = form.cleaned_data['additional']
	# 		requester = Request.objects.create(university=univ, name=name, surname=surname, age=age, program=program, language=language, degree=degree, score=score, phone=phone, additional=additional)
	# 		requester.country = univ.country.name
	# 		requester.save()
	# 		print(name, phone, "Thing have came !!!")
	# 		messages.success(request, _(f"{requester.name}, Your message was successfully submitted, please wait our call !"))
	# 		print("Requester Country", requester.country)
	# 		telegram_bot_sendtext(f'NEW USER {requester.country}',)
	# 		return redirect(f'/') 
	# 	else:
	# 		form = RequestForm
	# 		return redirect('/')









import json
from django.http import HttpResponse,JsonResponse
from django.core import serializers

import pickle

# AJAX category filter
def load_more(request):
	universities = list(University.objects.all()[0:int(request.GET.get('data'))+3].values())
	return JsonResponse(data={'universities':universities,'totalCount':University.objects.count()})


def load_less(request):
	universities = list(University.objects.all()[0:3].values())
	return JsonResponse(data={'universities':universities,'totalCount':University.objects.count()})

def country_filter(request):
	country_id = request.GET.get("data")
	print("Country ID", country_id)
	print("Country ID", country_id)
	if country_id != 'all':
		universities = list(University.objects.filter(country_id=country_id).values())
	else:
		universities = list(University.objects.all().values())
	return JsonResponse(data={'universities':universities,'totalCount':University.objects.count()})




def get_message(request):
	print("IN GET_MESSAGE FUNCTION ")
	
	return redirect("/")




