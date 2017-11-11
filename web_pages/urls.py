from django.conf.urls import url, include
from web_pages.views import ThanksPage, UserSignUp
from river_subs.views import UserAdmin

from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name="web_pages/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^signup/$', UserSignUp.as_view(), name="signup"),
    url(r'^thanks/$', ThanksPage.as_view(), name="thanks"),
]
