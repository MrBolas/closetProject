from django.conf.urls import url

from . import views

app_name='myShoppingHistory'

urlpatterns = [
    url(r'^$', views.defaultBaseView, name='index' ),
    url(r'^entry/', views.myShoppingDbEntry, name='myShoppingEntry' ),
    url(r'^query/', views.myShoppingDbQuery, name='myShoppingQuery' ),
]