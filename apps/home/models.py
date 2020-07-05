# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from .choices import IMAGE_TYPES_CHOICES


# --------------------------------------------------------- #
#         Tabela de Categorias das Imagens                  #
# --------------------------------------------------------- #
class Categories(models.Model):
    pk_categories = models.AutoField(primary_key=True, verbose_name='Código')
    dsc_cat = models.CharField(max_length=50)
    insert_date = models.DateTimeField('Data Inserção', auto_now_add=True)
    update_date = models.DateTimeField(
        'Data Edição', auto_now=True, null=True, blank=True
    )

    class Meta:
        db_table = 'ghome_categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'{str(self.pk_categories)} - {self.dsc_cat}'


# --------------------------------------------------------- #
#         Tabela de Imagens                                 #
# --------------------------------------------------------- #
class ImagesData(models.Model):
    pk_images = models.AutoField(primary_key=True, verbose_name='Código')
    fk_user = models.ForeignKey(
        User,
        models.PROTECT,
        'fk_images_users',
        verbose_name='Proprietário'
    )
    fk_categories = models.ForeignKey(
        Categories,
        models.PROTECT,
        'fk_images_categories',
        verbose_name='Categoria'
    )
    image = models.ImageField(upload_to='images/high', null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='images/thumbnail')
    dsc_image = models.TextField(verbose_name='Descrição')
    image_size = models.IntegerField(verbose_name='Tamanho')
    image_width = models.IntegerField(verbose_name='Comprimento')
    image_height = models.IntegerField(verbose_name='Altura')
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPES_CHOICES)
    flag_public = models.BooleanField(verbose_name='Público', default=True)
    insert_date = models.DateTimeField('Data Inserção', auto_now_add=True)
    update_date = models.DateTimeField(
        'Data Edição', auto_now=True, null=True, blank=True
    )

    class Meta:
        db_table = 'ghome_images'
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return f'{str(self.pk_categories)} - {self.dsc_cat}'
