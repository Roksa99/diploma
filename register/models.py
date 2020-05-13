from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Sex(models.Model):
    """Стать"""
    sex = models.CharField("Стать", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.sex

    class Meta:
        verbose_name = "Стать"
        verbose_name_plural = "Стать"


class Country(models.Model):
    """Країни"""
    country = models.CharField("Країна", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Країну"
        verbose_name_plural = "Країни"



class Profile(models.Model):
    """Користувачі додатково"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Користувач")
    sex = models.ForeignKey(Sex, on_delete = models.CASCADE, verbose_name="Стать")
    birthday = models.DateField(null=True, blank=True, verbose_name="День народження")
    country = models.ForeignKey(Country, on_delete = models.CASCADE, verbose_name="Країна")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Користувача"
        verbose_name_plural = "Користувачі"


class Theme(models.Model):
    """Теми"""
    name = models.CharField("Тема", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тему"
        verbose_name_plural = "Теми"


class Year(models.Model):
    """Рік"""
    year = models.CharField("Рік", max_length=4)

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = "Рік"
        verbose_name_plural = "Рік"


DEFAULT_YEAR_ID = 1

class Paper(models.Model):
    """Статті"""

    class Precense(models.TextChoices):
        TRUE = 'Виступали'
        FALSE = 'Не виступали'
    # PRESENCE_CHOICES =[
    #     (TRUE, 'Виступали'),
    #     (FALSE, 'Не виступали')
    # ]
    name = models.CharField("Назва", max_length=150)
    file = models.FileField("Файл", upload_to="file/")
    theme = models.ForeignKey(Theme, verbose_name="Тема", on_delete = models.CASCADE)
    year = models.ForeignKey(Year, verbose_name="Рік", default=DEFAULT_YEAR_ID, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="Автор")
    presence = models.CharField("Виступав на конференції", max_length=15, choices=Precense.choices, default=Precense.FALSE)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Статтю"
        verbose_name_plural = "Статті"