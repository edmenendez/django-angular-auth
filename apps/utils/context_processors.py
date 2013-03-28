from django.conf import settings


def misc(request):
    c = {
        "DEBUG": settings.DEBUG,
    }

    return c
