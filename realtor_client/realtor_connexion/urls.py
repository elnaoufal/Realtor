from django.urls import path

from . import views

urlpatterns = [
    path('', views.odoo_login, name='login'),
    path('sign_in', views.sign_in, name='sign_in'),
]