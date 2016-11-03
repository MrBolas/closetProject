from django.shortcuts import render
from django.http import HttpResponse

from myShoppingHistory.models import Item


# Create your views here.

def myShoppingDbEntry(request):
    #print("hello!")
    if request.method == 'POST':
        print(request.POST)
        if request.POST["Item"] and request.POST["Description"]:
            #DB
            instance, created = Item.objects.get_or_create(title=request.POST["Item"], description=request.POST["Description"], quantity=request.POST["Quantity"])
            return render(request, 'myShoppingHistory/myShoppingIndex.html')

    items = Item.objects.exclude(quantity=0)
    return render(request, 'myShoppingHistory/myShoppingIndex.html', {
        'items': items,
    })

def myShoppingDbQuery(request):


    items = Item.objects.all()

    return render(request, 'myShoppingHistory/myShoppingQuery.html',{
        'items': items,
    })
