from django.urls import path

from . import views

urlpatterns = [
    path('listappart', views.list_apartments_view, name='list_appart'),
    path('propose_offer', views.propose_offer, name='offer'),
]