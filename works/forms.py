from django.forms import ModelForm
from .models import Serv, Work


class ServForm(ModelForm):
    class Meta:
        model = Serv
        fields = '__all__'
        exclude = ['owner']


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
        exclude = ['owner']


