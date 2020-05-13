from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q, Count, F
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm, PaperForm, PaperEdit
from django.core.files.storage import FileSystemStorage
from .models import Paper, Theme, User, Profile, Year
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from datetime import date
from .filters import YearFilter, ThemeFilter, YearThemeFilter
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

class ThemeYear:
	def get_year(self):
		return Year.objects.all()

	def get_theme(self):
		return Theme.objects.all()


class PaperListView(ThemeYear, ListView):
    model = Paper
    template_name = 'paper/paper_list.html'


@login_required
def upload (request):
	if request.method == 'POST':
		upload_form = PaperForm(request.POST, request.FILES)
		if upload_form.is_valid():
			peper = upload_form.save(commit=False)
			peper.user = request.user
			upload_form.save()
			return redirect('/user_paper')
	else:
		upload_form = PaperForm()
	return render(request, 'paper/upload.html', {'upload_form': upload_form})


def delete_paper(request, id):
    if request.method == 'POST':
        paper = Paper.objects.get(pk=id)
        paper.delete()
    return redirect('/user_paper')



def user_paper (request):
	user_points = Paper.objects.filter(user=request.user)
	return render(request, 'paper/user_paper.html', {'user_points': user_points})



def edit_paper(request, id):
    paper = Paper.objects.get(id=id)
    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect('/user_paper')
        else:
            form = PaperForm(instance=paper)
    else:
        form = PaperForm(instance=paper)
    return render(request, 'paper/edit.html', {'form':form, 'paper':paper})


# @login_required
# @transaction.atomic
def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		profile_form = ProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():

			user = form.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile_form.save()

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)

		return redirect('/paper')
	else:
		form = RegisterForm()
		profile_form = ProfileForm()

	return render(request, "account/registration.html", {"form":form, "profile_form": profile_form})


class FilterYearView(ThemeYear, ListView):
    """Фильтр статей за роком"""
    def get_queryset(self):
        queryset = Paper.objects.filter(
			Q(year__in = self.request.GET.getlist("year")) |
			Q(theme__in = self.request.GET.getlist("theme"))
        )
        return queryset


def st_theme(request):
	# виводить суму статей


	# виводить суму статей кожної теми
	context = Paper.objects.values('theme__name').annotate(paper_sum=Count('name'))

	year_filter = YearFilter(request.GET, queryset=context)
	return render(request, 'statistics/st_theme.html', {
		'context': year_filter
	})


def st_presence(request):
	pr_true = Paper.objects.values('presence').annotate(paper_sum=Count('name'))
	year_theme_filter = YearThemeFilter(request.GET, queryset=pr_true)
	return render(request, 'statistics/st_presence.html', {
		'insert_true': year_theme_filter
	})


def st_sex(request):
	insert_sex = Paper.objects.values('user__profile__sex__sex').annotate(sex_sum=Count('user__profile__sex__sex'))
	year_theme_filter = YearThemeFilter(request.GET, queryset=insert_sex)
	return render(request, 'statistics/st_sex.html', {
		'insert_sex': year_theme_filter
	})


def st_country(request):
	insert_country = Paper.objects.values('user__profile__country__country').annotate(country_sum=Count('user__profile__country__country'))
	year_theme_filter = YearThemeFilter(request.GET, queryset=insert_country)
	return render(request, 'statistics/st_country.html', {
		'insert_country': year_theme_filter
	})


def st_paper_spiker(request):
	paper_spiker = Paper.objects.values('year__year').annotate(paper_sum=Count('name')).annotate(spiker_sum=Count('user', distinct=True))
	theme_filter = ThemeFilter(request.GET, queryset=paper_spiker)
	return render(request, 'statistics/st_paper_spiker.html', {
		'paper_spiker': theme_filter
	})


def st_theme_paper(request):
	theme_paper = Paper.objects.values('theme__name').annotate(paper_sum=Count('name'))
	year_filter = YearFilter(request.GET, queryset=theme_paper)
	return render(request, 'statistics/st_theme_paper.html', {
		'theme_paper': year_filter
	})


def st_age(request):
	today = date.today()
	insert_age = Paper.objects.values('user__profile__birthday__year').annotate(age_sum=Count('user__profile__birthday__year'))
	year_theme_filter = YearThemeFilter(request.GET, queryset=insert_age)
	return render(request, 'statistics/st_age.html', {
		'insert_age': year_theme_filter, 'today': today
	})


