from django import template
from register.models import Sex, Country, Theme, Paper

register = template.Library()

@register.simple_tag()
def get_sex():
    return Sex.objects.all()

@register.simple_tag()
def get_country():
    return Country.objects.all()

@register.simple_tag()
def get_theme():
    return Theme.objects.all()

@register.inclusion_tag('paper/tags/last_paper.html')
def get_last_paper(request):
	last_paper = Paper.objects.filter(user=request.user).order_by("-id")[:3]
	return  {'last_paper': last_paper}
