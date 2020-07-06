from django.contrib import admin
from .models import Categories, ImagesData


@admin.register(Categories)
class HomeCategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'pk_categories', 'dsc_cat', 'update_date', 'insert_date',
    )
    list_filter = ('dsc_cat', 'insert_date')


@admin.register(ImagesData)
class HomeImages_dataAdmin(admin.ModelAdmin):
    list_display = (
        'fk_categories', 'fk_user', 'dsc_image', 'image', 'insert_date', 'update_date',
    )
    list_filter = ('dsc_image', 'fk_user', 'fk_categories', 'insert_date')
