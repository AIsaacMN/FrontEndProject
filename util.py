from typing import Any, Final
from django.http import HttpResponseRedirect

MONGO_URI: Final[str] = "http://localhost:3000"

SESSION_USER: Final[str] = "SESSION_USER"

def create_session(request: Any, value: dict[str]):
    request.session[SESSION_USER] = {
        "username": value['username'],
        "user_id": value['_id']
    }

def redirect_dashboard(function):
    def wrapper(request, *args, **kwargs):
        try:
            temp_session = request.session[SESSION_USER]
            return HttpResponseRedirect('/dashboard')
        except KeyError:
            pass
    return wrapper