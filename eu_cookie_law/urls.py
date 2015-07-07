from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hide/$', views.HideCookieMessageView.as_view(), name='hide_cookie_message'),
]
