from django import forms
from .models import Review
from django.forms import ModelForm


# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=15)
#     last_name = forms.CharField(label='Last Name', max_length=15)
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'email-inform'}))
#     review = forms.CharField(label='Review', widget=forms.Textarea(attrs={'class': 'text-inform'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'stars': 'Stars'
        }

        error_messages = {
            'stars': {
                'min_value': 'You Should Enter 1 Or More',
                'max_value': 'You Should Enter 5 or Less'
            }
        }
