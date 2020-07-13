# -*- coding: utf-8 -*-
from django.urls import path
from .views import ShowIndexView, ListPublicImagesView, DetailCategoryView, DetailImageView

app_name = 'home'
urlpatterns = [
    path('', ShowIndexView.as_view(), name='index'),
    path('list_public_images/', ListPublicImagesView.as_view(), name='list_public_images'),
    path('category_detail/', DetailCategoryView.as_view(), name='create_category'),
    path('category_detail/<int:pk>', DetailCategoryView.as_view(), name='detail_category'),
    path('image_detail/', DetailImageView.as_view(), name='create_image'),
    path('image_detail/<int:pk>', DetailImageView.as_view(), name='detail_image'),
]
