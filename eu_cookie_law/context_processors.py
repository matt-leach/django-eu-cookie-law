from eu_cookie_law import COOKIE_MESSAGE_KEY


def cookie_message(request):
    try:
        request.COOKIES[COOKIE_MESSAGE_KEY]
        return {}
    except KeyError:
        return {"show_cookie_message": True}
