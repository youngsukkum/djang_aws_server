"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from . import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phonebook/', include('phonebook.urls')),
    path('border/', include('border.urls')),
    path('updown/', include('updown.urls')),
    path("", views.index),
    path("account/login/", views.login, name='login'),
    path("account/logout/", views.logout, name='logout'),
    path("account/register/", views.createAccount, name="create"),
    path('account/myinfo/', views.myinfo, name='myinfo'),
    path('account/myinfoDel/', views.myinfoDel, name='delete'),
]

handler404 = views.page_not_found
handler500 = views.custom_500

