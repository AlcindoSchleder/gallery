# -*- coding: utf-8 -*-
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
        else:
            return super(ListPublicImagesView, self).render_column(row, column)


class DetailCategoryView(PermissionRequiredMixin, LoginRequiredMixin, BaseFormView):

    permission_required = 'finance.transactions'
    login_url = 'login/'
    permission_denied_message = 'Você ão tem permissão para esta operação!'
    template_name = 'home/categories.html'
    form_class = CategoriesForm

    def get(self, request, *args, **kwargs):
        try:
            category = Categories.objects.get(pk=kwargs.get('pk', 0))
        except ObjectDoesNotExist:
            category = Categories(pk=0)
        form = self.form_class(category)
        render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponse(form.data, 200)

        return render(request, self.template_name, {'form': form})

