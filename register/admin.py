from django.contrib import admin
from .models import Profile, Country, Sex, Theme, Paper, Year
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'birthday', 'country')
    list_filter = ('country', 'sex')
    search_fields = ('user__first_name','user__last_name')

@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'theme', 'year', 'user', 'presence')
    list_filter = ('user', 'theme', 'year', 'presence')
    search_fields = ('name',)
    list_editable = ('presence',)

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year', 'id')


admin.site.register(Country)
admin.site.register(Sex)
admin.site.register(Theme)
