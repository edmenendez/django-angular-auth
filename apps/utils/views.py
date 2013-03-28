import traceback
from functools import wraps
from django.http import HttpResponseBadRequest, HttpResponse  # , Http404
from django.utils import simplejson


class HttpResponseJson(HttpResponse):
    def __init__(self, data):
        json_data = simplejson.dumps(data)
        super(HttpResponseJson, self).__init__(
            content=json_data, mimetype='application/json')


def ajax_get(func):
    """
    Convert views's output into JSON.

    Decorated view should return dict object.

    If view raises Exception then return JSON message with error description.
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        try:
            response = func(request, *args, **kwargs)
        except Exception, ex:
            response = {'error': traceback.format_exc()}
        if isinstance(response, dict):
            return HttpResponseJson(response)
        else:
            return response
    return wrapper
