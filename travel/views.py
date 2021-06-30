from django.shortcuts import render
from .models import destination
def index(request):
    dest1 = destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'Beautifull city with lots of opportunity'
    dest1.img = 'images/1.jpg'

    dest2 = destination()
    dest2.name = 'Delhi'
    dest2.desc = 'Beautifull city with lots of opportunity'
    dest2.img = 'images/2.jpg'

    dest3 = destination()
    dest3.name = 'kolkata'
    dest3.desc = 'Beautifull city with lots of opportunity'
    dest3.img = 'images/3.jpg'

    dest = [dest1, dest2, dest3]

    return render(request, 'index.html', { 'dest' : dest})
