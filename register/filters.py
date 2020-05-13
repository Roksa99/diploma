from django import forms
from django.contrib.auth.models import User
from .models import Paper, Theme, User, Year

import django_filters


class YearFilter(django_filters.FilterSet):
    # year = django_filters.ModelMultipleChoiceFilter(field_name='year', queryset=Paper.objects.values_list('year', flat=True).order_by('year').distinct(), widget=forms.CheckboxSelectMultiple)
    year = django_filters.ModelMultipleChoiceFilter(field_name='year', queryset=Year.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Paper
        fields = ['year']


class ThemeFilter(django_filters.FilterSet):
    theme = django_filters.ModelMultipleChoiceFilter(field_name='theme', queryset=Theme.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Paper
        fields = ['theme']


class YearThemeFilter(django_filters.FilterSet):
    theme = django_filters.ModelMultipleChoiceFilter(field_name='theme', queryset=Theme.objects.all(), widget=forms.CheckboxSelectMultiple)
    year = django_filters.ModelMultipleChoiceFilter(field_name='year', queryset=Year.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Paper
        fields = ['year', 'theme']



# class UserFilter(django_filters.FilterSet):
#     # year = django_filters.ModelMultipleChoiceFilter(field_name='year', queryset=Paper.objects.all(), widget=forms.CheckboxSelectMultiple)
#
#     class Meta:
#         model = User
#         fields = ['username']