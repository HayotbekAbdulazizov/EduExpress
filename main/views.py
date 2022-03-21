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
			'universities': University.objects.all(),
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
