from .models import *

def footer(request):
    context = {
        'about': AboutUsDetail.objects.last()
    }
    return context