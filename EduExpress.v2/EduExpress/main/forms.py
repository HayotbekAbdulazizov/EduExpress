# from attr import field, fields
from urllib.request import Request
from django.forms import ModelForm
from main.models import ClientRequest

class RequestForm(ModelForm):
     class Meta:
        model = ClientRequest
        fields = '__all__'
        exclude = ["date",]


