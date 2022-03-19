from attr import field, fields
from django.forms import ModelForm
from main.models import Message

class MessageForm(ModelForm):
     class Meta:
        model = Message
        fields = '__all__'
        exclude = ["date",]

