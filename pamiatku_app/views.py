from django.shortcuts import render

from .models import PamTitle

def index(request):
    titles = PamTitle.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'pamiatku_app/index.html', context)
