from django.shortcuts import render
from .models import destination
def index(request):

    dest = destination.objects.all()

    return render(request, 'index.html', { 'dest' : dest})
