# -*- coding: utf-8 -*-
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.views.generic import TemplateView
from django.views.generic.edit import BaseFormView
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.shortcuts import render, HttpResponse
from .models import Categories, ImagesData
from .forms import CategoriesForm, ImagesForm

# Create your views here.


class ShowIndexView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        message = kwargs.get('message', '')
        qs_categories = Categories.objects.all()
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        params = {
            'user': user,
            'profile': True,
            'qs_categories': qs_categories,
            'message': message
        }
        return render(request, self.template_name, params)


class ListPublicImagesView(BaseDatatableView):
    model = ImagesData
    columns = [
        'thumbnail_image', 'fk_categories', 'pk_images', 'fk_user', 'image_size',
        'image_width', 'image_height', 'image_type', 'flag_public'
    ]
    order_columns = ['fk_categories', 'fk_user', 'flag_public', 'image_size']

    def render_column(self, row, column):
        # We want to render thumbnail_image as a custom column
        if column == 'thumbnail_image':
            if row.thumbnail_image:
                return escape(row.thumbnail_image.url)
            else:
                return escape('static/logo.png')
        elif column == 'fk_categories' and self.request.user.is_authenticated:
            return escape(f'{row.fk_categories.pk_categories} - {row.fk_categories.dsc_cat}')
        else:
            return super(ListPublicImagesView, self).render_column(row, column)


class DetailCategoryView(PermissionRequiredMixin, LoginRequiredMixin, BaseFormView):

    permission_required = 'finance.transactions'
    login_url = '/login/'
    permission_denied_message = 'Você não tem permissão para esta operação!'
    template_name = 'home/categories.html'
    form_class = CategoriesForm

    def get(self, request, *args, **kwargs):
        category = None
        try:
            category = Categories.objects.get(pk=kwargs.get('pk', 0))
            data = {
                'pk_categories': category.pk_categories,
                'dsc_cat': category.dsc_cat
            }
        except ObjectDoesNotExist:
            data = {
                'pk_categories': 0,
                'dsc_cat': ''
            }
        form = self.form_class(data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save()
            res = {
                'result': 200,
                'pk_categories': data.pk_categories,
                'dsc_cat': data.dsc_cat
            }
            return HttpResponse(
                json.dumps(res),
                content_type="application/json"
            )

        return render(request, self.template_name, {'form': form})


class DetailImageView(PermissionRequiredMixin, LoginRequiredMixin, BaseFormView):

    permission_required = 'finance.transactions'
    login_url = '/login/'
    permission_denied_message = 'Você não tem permissão para esta operação!'
    template_name = 'home/images.html'
    form_class = ImagesForm

    def get(self, request, *args, **kwargs):
        image = None
        try:
            image = Categories.objects.get(pk=kwargs.get('pk', 0))
            data = {
                'pk_images': image.pk_images,
                'fk_user': image.fk_user,
                'fk_categories': image.fk_categories,
                'image': image.image,
                'thumbnail_image': image.thumbnail_image,
                'dsc_image': image.dsc_image,
                'image_size': image.image_size,
                'image_width': image.image_width,
                'image_height': image.image_height,
                'image_type': image.image_type,
                'flag_public': image.flag_public,
            }
        except ObjectDoesNotExist:
            data = {
                'pk_images': 0,
                'fk_user': None,
                'fk_categories': None,
                'image': None,
                'thumbnail_image': None,
                'dsc_image': '',
                'image_size': 0,
                'image_width': 0,
                'image_height': 0,
                'image_type': '',
                'flag_public': True,
            }
        form = self.form_class(data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.save()
            res = {
                'result': 200,
                'pk_images': data.pk_images,
                'fk_user': data.fk_user.id,
                'fk_categories': data.fk_categories.id,
                'image': data.image,
                'thumbnail_image': data.thumbnail_image,
                'dsc_image': data.dsc_image,
                'image_size': data.image_size,
                'image_width': data.image_width,
                'image_height': data.image_height,
                'image_type': data.image_type,
                'flag_public': data.flag_public,
            }
            return HttpResponse(
                json.dumps(res),
                content_type="application/json"
            )

        return render(request, self.template_name, {'form': form})

