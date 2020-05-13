"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib import admin, auth
from django.contrib.auth import views
from django.urls import path, include
import register.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", register.views.register, name="register"),
    path("filter/", register.views.FilterYearView.as_view(template_name = 'paper/paper_list.html'), name="filter"),
    path("paper/", register.views.PaperListView.as_view(), name="paper"),
    path("upload/", register.views.upload, name="upload"),
    path("user_paper/", register.views.user_paper, name="user_paper"),
    path('<int:id>/delete_paper/', register.views.delete_paper, name='delete_paper'),
    # path('user_paper/edit/<int:pk>', register.views.PaperUpdate.as_view(), name="edit"),
    path('edit/<int:id>', register.views.edit_paper, name='edit'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path("st_theme/", register.views.st_theme, name="st_theme"),
    # path("st_theme_filter/", register.views.FilterYearView.as_view(template_name = 'statistics/st_theme.html'), name="st_theme_filter"),
    path("st_presence/", register.views.st_presence, name="st_presence"),
    path("st_sex/", register.views.st_sex, name="st_sex"),
    path("st_age/", register.views.st_age, name="st_age"),
    path("st_country/", register.views.st_country, name="st_country"),
    path("st_paper_spiker/", register.views.st_paper_spiker, name="st_paper_spiker"),
    path("st_theme_paper/", register.views.st_theme_paper, name="st_theme_paper"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)