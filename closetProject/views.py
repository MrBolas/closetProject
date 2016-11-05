from django.shortcuts import render
from django.http import HttpResponse

from myShoppingHistory.models import changeLogs


def defaultBaseView(request):
    clogs= changeLogs.objects.order_by('-t_stamp')
    return render(request, 'index/index.html', {'clogs': clogs})

def defaultBaseLogEntry(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST["Title"] and request.POST["Description"]:
            #DB
            instance, created = changeLogs.objects.get_or_create(title=request.POST["Title"], description=request.POST["Description"])
            return render(request, 'index/indexEntry.html')

    return render(request, 'index/indexEntry.html', {
        'clogs': changeLogs,
    })