from re import template
from .models import *
from django.views.generic import DetailView, TemplateView, View
from django.shortcuts import redirect, render
# from .tg_sender import telegram_bot_sendphoto, telegram_bot_sendtext
from django.utils.translation import gettext as _
from django.contrib import messages
from .forms import MessageForm
from parler.views import TranslatableSlugMixin

class HomePageView(View):
	def get(self,request):
		context = {
			'status':200,
			'universities': University.objects.all(),
			'countries': Country.objects.all(),
            "form":MessageForm,
		}		
		return render(request, 'index.html', context)

	def post(self, request):
		name = request.POST["name"]
		email = request.POST["email"]
		phone = request.POST["phone"]
		message  = request.POST["message"]
		# client_message = ClientMessage.objects.create( name=name, phone=phone, email=email, message=message)
		# telegram_bot_sendtext(f"  ClientMessage  \n Name: {name} \n Email :  {email}  \n Phone: +{phone} \n Link: https://paddingpack.uz/admin/main/clientmessage/{client_message.id}/change")
		# messages.success(request, _("Your message was successfully submitted, please wait our call !"))
		
		return redirect(f'/') 


# class UniversityDetailView(TranslatableSlugMixin,DetailView):
#     def get(self, request, slug):
#         # object  = University.objects.language(request.LANGUAGE_CODE)
#         # object = object.get(slug=slug)
#         object  = University.objects.get(slug=slug, language=request.LANGUAGE_CODE)

#         for i in object:
#             print(i)
#         context = {
#             'status':200,
#             # "object":object,
#         }		
#         return render(request, 'university_detail.html', context)








class BaseUniversityMixin:
    def get_queryset(self):
        return super().get_queryset().filter(id=True)


class UniversityDetailView(BaseUniversityMixin, TranslatableSlugMixin, DetailView):
    model = University
    template_name = "university_detail.html"  # This works as expected

# class UniversityDetailView(TranslatableSlugMixin ,DetailView):
#     model = University
#     template_name = 'university_detail.html'



























































# trash
"""
class UniversityDetailView(TranslatableSlugMixin,DetailView):
    def get(self, request, slug):
        # a = University.objects.translated().annotate(articles_count=(University("articles__translations")))
        a = University.objects.translated().annotate()
        # print(a)
        for i in a:
            print(i)
        # print(slug)
        context = {
            'status':200,
            # 'universities': University.objects.all(),
            # 'countries': Country.objects.all(),
            # "form":MessageForm,
            # "object":University.objects.get(slug=slug)
        }		
        return render(request, 'university_detail.html', context)
"""