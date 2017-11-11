"""river_info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from web_pages.views import ThanksPage, UserSignUp, Home
from river_subs.views import UserAdmin, SendEmail
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home, name="home"),
    url(r'^accounts/', include('web_pages.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^rivers/', include('rivers.urls')),
    url(r'^useradmin/', UserAdmin, name="user_admin"),
    url(r'^thanks/', ThanksPage.as_view(), name="thanks"),
    url(r'^send/', SendEmail, name="send_email"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
