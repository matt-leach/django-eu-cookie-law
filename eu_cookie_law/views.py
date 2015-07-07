from django.http import HttpResponse
from django.views.generic import View

from eu_cookie_law import COOKIE_MESSAGE_KEY


class HideCookieMessageView(View):

    def post(self, request):
        response = HttpResponse('')
        response.set_cookie(key=COOKIE_MESSAGE_KEY, max_age=60*60*24*365*100)
        return response
