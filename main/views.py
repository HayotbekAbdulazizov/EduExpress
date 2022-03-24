from .models import *
from django.views.generic import DetailView, TemplateView, View
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.contrib import messages
from .forms import RequestForm

class HomePageView(View):
	def get(self,request):
		context = {
			'status':200,
			'universities': University.objects.all()[0:3],
			'countries': Country.objects.all(),
            "form":RequestForm,
		}		    
		return render(request, 'index.html', context)

	def post(self, request):
		form  = RequestForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			surname = form.cleaned_data['surname']
			age = form.cleaned_data['age']
			country = form.cleaned_data['country']
			program = form.cleaned_data['program']
			language = form.cleaned_data['language']
			degree = form.cleaned_data['degree']
			score = form.cleaned_data['score']
			print(Request)
			print(type(Request))
			phone = form.cleaned_data['phone']
			additional = form.cleaned_data['additional']
			requester = Request.objects.create(name=name, surname=surname, age=age, country=country, program=program, language=language, degree=degree, score=score, phone=phone, additional=additional)
			print(name, phone, "Thing have came !!!")
			# messages.success(request, _(f"{requester.name}, Your message was successfully submitted, please wait our call !"))
			print("redirecting !!!")
			return redirect(f'/') 
		else:
			form = RequestForm
			print("There is an ERROR !!!")
			return redirect('/')
		
		


		# client_message = ClientMessage.objects.create( name=name, phone=phone, email=email, message=message)
		# telegram_bot_sendtext(f"  ClientMessage  \n Name: {name} \n Email :  {email}  \n Phone: +{phone} \n Link: https://paddingpack.uz/admin/main/clientmessage/{client_message.id}/change")
		# messages.success(request, _("Your message was successfully submitted, please wait our call !"))
	


class UniversityDetailView(View):
	def get(self,request, slug):

		context = {
			"object":University.objects.get(slug=slug),
			"form":RequestForm,
		}
		return render(request, 'university_detail.html', context)

	def post(self, request, slug):
		form  = RequestForm(request.POST)
		if form.is_valid():
			# university_id = form.cleaned_data['univ_id']
			# print(university_id)
			univ = University.objects.get(id=1)

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
			# requester.country = univ.country.name
			requester.save()
			print(name, phone, "Thing have came !!!")
			messages.success(request, _(f"{requester.name}, Your message was successfully submitted, please wait our call !"))
			print("redirecting !!!")
			return redirect(f'/') 
		else:
			form = RequestForm
			print("There is an ERROR !!!")
			return redirect('/')















import json
from django.http import HttpResponse,JsonResponse
from django.core import serializers

import pickle

# AJAX category filter
def load_more(request):
	# print('CAME TO FILTER')
	# datas = {}
	# info = request.GET.get('data')
	# print(info)
	# universities_all = list(University.objects.language(request.LANGUAGE_CODE).values())
	# universities = universities_all[0:6]
	# print(universities)
	# print(type(request.LANGUAGE_CODE),request.LANGUAGE_CODE)
	# print(universities_all)

	#     print('Len 0 Events', len(events))
	#     datas ['cities'] = []
	#     for city in City.objects.all():
	#         for location in events.values('location'):
	#             print('CITY', city.name, location['location'], city.name in location['location'])
	#             if city.name in location['location']:
	#                 datas['cities'].append({'name':city.name, 'id':city.id})    
	#                 break
	#             # datas['cities'].append({'name':city.name, 'id':city.id} if str(city.name) in location['location'] else print('None'))
	#             # print(datas['cities'])
	#     print('CITIES', datas['cities'])
	#     datas['themes'] = list(Theme.objects.filter(category_id=info[0]).values())
	# else:
	#     events = Event.objects.all()
	#     datas['themes'] = list(Theme.objects.all().values())
	#     print('Len Events ', len(events))
	#     # datas['cities'] = list(City.objects.all().values())
	# if info[1] != '':
	#     events = events.filter(location__icontains=info[1])
	# datas['data'] = events 
	#     print('Len 2 Events ', len(events))
	# for i in universities_all:
		# print(i.name)
	# universities_json = serializers.serialize('json',universities_all)
	# return True

	# qs 	= University.objects.values_list('id')

	# qs = University.objects.language(request.LANGUAGE_CODE).all()[0]
	qs = list(University.objects.language(request.LANGUAGE_CODE).all())
	print(qs)


	# print(qs.translations.values())
	# print(dict(.translations.values_list("name", "slug")))

	# QuerySet [(1, 'Beatles Blog')]>
	# reloaded_qs = University.objects.all()
	# reloaded_qs.query = pickle.loads(pickle.dumps(qs.query))
	# print(reloaded_qs)
	return JsonResponse(data={'universities':200,'totalCount':University.objects.count()})