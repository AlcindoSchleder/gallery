# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.shortcuts import render
from django.db.models import Q
from .models import Categories, ImagesData

# Create your views here.


class ShowIndexView(TemplateView):
    template_name = 'home/index.html'
    allowed_methods = ['GET', 'POST']

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

    # def get_initial_queryset(self):
    #     if self.request.user.is_authenticated:
    #         user = self.request.user
    #         try:
    #             qs_images = self.request.user.fk_images_users.filter(fk_user=user)
    #         except ObjectDoesNotExist:
    #             user = None
    #             qs_images = None
    #     else:
    #         user = None
    #         qs_images = ImagesData.objects.filter(flag_public=True)
    #     return qs_images
    #
    # def filter_queryset(self, qs):
    #     # use request parameters to filter queryset
    #     # simple example:
    #     search = self.request.GET.get('search[value]', None)
    #     if search:
    #         qs = qs.filter(name__istartswith=search)
    #
    #     # more advanced example
    #     filter_user = self.request.GET.get('fk_user', None)
    #     filter_category = self.request.GET.get('fk_categories', None)
    #
    #     if filter_user:
    #         user_parts = filter_user.split(' ')
    #         qs_params = None
    #         for part in user_parts:
    #             q = Q(user_firstname__istartswith=part) | Q(user_lastname__istartswith=part)
    #             qs_params = qs_params | q if qs_params else q
    #         qs = qs.filter(qs_params)
    #     if filter_category:
    #         qs_params = None
    #         q = Q(fk_categories_dsc_cat__istartswith=part)
    #         qs_params = qs_params | q if qs_params else q
    #         qs = qs.filter(qs_params)
    #     return qs
    #
    # def prepare_results(self, qs):
    #     # prepare list with output column data
    #     # queryset is already paginated here
    #     json_data = []
    #     for item in qs:
    #         json_data.append([
    #             escape(item.number),  # escape HTML for security reasons
    #             escape(f"{item.user_firstname} {item.user_lastname}"),  # escape HTML for security reasons
    #             item.get_state_display(),
    #             item.created.strftime("%Y-%m-%d %H:%M:%S"),
    #             item.modified.strftime("%Y-%m-%d %H:%M:%S")
    #         ])
    #     return json_data

