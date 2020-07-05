# -*- coding: utf-8 -*-
from django.urls import path
from .views import ShowIndexView, ListPublicImagesView

app_name = 'home'
urlpatterns = [
    path('', ShowIndexView.as_view(), name='index'),
    path('list_public_images/', ListPublicImagesView.as_view(), name='list_public_images'),
]