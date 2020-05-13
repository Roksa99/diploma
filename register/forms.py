from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Paper
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(widget=DateInput(format='%d/%m/%Y'),
                               input_formats=('%d/%m/%Y',))
    class Meta:
        model = Profile
        fields = ["sex", "birthday", "country"]


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["last_name", "first_name",  "username", "email", "password1", "password2"]
    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ["name", "theme", "file"]


class PaperEdit(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ["name", "theme", "file"]

