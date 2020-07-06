# -*- coding: utf-8 -*-
import os
from io import BytesIO
from PIL import Image as PilImage
from django.db import models
from django.contrib.auth.models import User
from .choices import IMAGE_TYPES_CHOICES
from django.core.files.uploadedfile import SimpleUploadedFile


# --------------------------------------------------------- #
#         Tabela de Categorias das Imagens                  #
# --------------------------------------------------------- #
class Categories(models.Model):
    pk_categories = models.AutoField(primary_key=True, verbose_name='Código')
    dsc_cat = models.CharField(max_length=50, verbose_name='Descrição')
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
    image = models.ImageField(upload_to='images/high')
    thumbnail_image = models.ImageField(upload_to='images/thumbnail', null=True, blank=True)
    dsc_image = models.TextField(verbose_name='Descrição')
    image_size = models.IntegerField(verbose_name='Tamanho', null=True, blank=True)
    image_width = models.IntegerField(verbose_name='Comprimento', null=True, blank=True)
    image_height = models.IntegerField(verbose_name='Altura', null=True, blank=True)
    image_type = models.CharField(max_length=5, choices=IMAGE_TYPES_CHOICES)
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
        return f'{str(self.pk_images)} - {self.dsc_image}'

    def create_thumbnail(self):
        # original code for this method came from
        # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

        # If there is no image associated with this.
        # do not create thumbnail
        if not self.image:
            return

        # Set our max thumbnail size in a tuple (max width, max height)

        django_type = self.image.file.content_type

        if django_type == 'image/jpeg':
            pil_type = 'jpeg'
            file_extension = 'jpg'
        elif django_type == 'image/png':
            pil_type = 'png'
            file_extension = 'png'
        elif django_type == 'image/bmp':
            pil_type = 'bmp'
            file_extension = 'bmp'
        else:
            pil_type = django_type.split('/')
            file_extension = pil_type[1]
            pil_type = file_extension

        # Open original photo which we want to thumbnail using PIL's Image
        image_obj = PilImage.open(self.image)
        self.image_width = image_obj.width
        self.image_height = image_obj.height
        self.image_type = file_extension
        self.image_size = self.image.file.size
        default_size = 50   # define image width and height at 50 pixels to create thumbnail image
        # check if width is greater then height to calculate default percent proportionally
        if self.image_width > self.image_height:
            default_percent = default_size / self.image_width
        # check if height is greater then width to calculate default percent proportionally
        elif self.image_height > self.image_width:
            default_percent = default_size / self.image_height
        else:
            # width equal height
            default_percent = default_size / self.image_width
        thumbnail_size = (self.image_width * default_percent, self.image_height * default_percent)

        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image_obj.thumbnail(thumbnail_size, PilImage.ANTIALIAS)

        # Save the thumbnail
        temp_buffer = BytesIO()
        image_obj.save(fp=temp_buffer, format=pil_type)
        temp_buffer.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        image_name = os.path.split(self.image.name)[-1]
        suf = SimpleUploadedFile(image_name, temp_buffer.read(), content_type=django_type)
        # Save SimpleUploadedFile into thumbnail_image field
        self.thumbnail_image.save(image_name, suf, save=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.create_thumbnail()
        force_update = False
        # If the instance already has been saved, it has an id and we set
        # force_update to True
        if self.pk_images:
            force_update = True
        # Force an UPDATE SQL query if we're editing the image to avoid integrity exception
        super(ImagesData, self).save(force_update=force_update)
