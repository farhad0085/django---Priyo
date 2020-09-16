from django.conf import settings 

def get_sitename(request):
    return {'SITENAME': settings.SITENAME}