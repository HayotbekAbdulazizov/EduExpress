# from attr import field, fields
from django.forms import ModelForm
from main.models import Request

class RequestForm(ModelForm):
     class Meta:
        model = Request
        fields = '__all__'
        exclude = ["date",]


