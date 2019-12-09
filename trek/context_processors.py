from .models import *

def footer(request):
    context = {
        'about': AboutUsDetail.objects.last(),
        'about_nepal': Generic.objects.filter(section='About_Nepal'),
        'before_visit': Generic.objects.filter(section='Before_Visit'),
        'popular_links': Generic.objects.filter(section='Popular_Links')
    }
    return context