from django.core.exceptions import PermissionDenied

def superuser_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied 
        return view_func(request, *args, **kwargs)
    return wrapped_view
