from django import forms
from django.core import validators
from .models import Movel

def check_for_z(value):
        if value[0].lower() !='z':
                raise forms.ValidationError("NAME NEEDS TO START WITH Z")


class MyForm(forms.Form):
        name = forms.CharField()
        email = forms.EmailField()
        text = forms.CharField(widget=forms.Textarea)
        botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(11)])
          
        def clean_botcatcher(self):
                        botcatcher = self.cleaned_data['botcatcher']
                        if len(botcatcher) > 0:
                                raise forms.ValidationError("GOTCHA BOT!")
                        return botcatcher

class movelform(forms.ModelForm):

        class Meta:
                model = Movel
                fields ='__all__'