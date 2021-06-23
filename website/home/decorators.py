from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def unauthorized_user(view_func):
    def wrap_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrap_func


def allowed_user(allowed_user=[]):
    def decorator(view_func):
        def wrap_func(request, *args, **kwargs):
            # print(request.user.groups.all().exists())
            group = None
            if request.user.groups.all().exists():
                group = request.user.groups.first().name
            # print(type(allowed_user))
            # print(type(group))
            # print(group not in allowed_user, group in allowed_user)
            if group not in allowed_user:
                return redirect('home')
            return view_func(request, *args, **kwargs)
        return wrap_func
    return decorator
