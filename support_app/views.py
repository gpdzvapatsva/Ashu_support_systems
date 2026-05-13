from django.shortcuts import render
from .models import SupportWorkers

# Create your views here.
def support(request):
    supportw=SupportWorkers.objects.all()
    return render(request, 'support_list.html', {'supportw':supportw})
