from django.http import HttpResponse, HttpResponseNotFound


class Error404Mixin:
    def get(self, request, *args, **kwargs) -> HttpResponse | HttpResponseNotFound:
        try:
            res = super().get(self, request, *args, **kwargs)
            return res
        except Exception as exc:
            return HttpResponseNotFound('404 this order is not found')
