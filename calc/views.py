from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'name': 'Yash'})


def add(request):
    num1 = request.POST["num1"]
    num2 = request.POST['num2']
    result = int(num1) + int(num2)
    return render(request, 'result.html', {'result': result})
