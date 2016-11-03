from django.shortcuts import render
from django.http import HttpResponse


def defaultBaseView(request):
    return render(request, 'base.html')