# Generated by Django 3.0.7 on 2020-07-05 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('pk_categories', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('dsc_cat', models.CharField(max_length=50)),
                ('insert_date', models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Data Edição')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'ghome_categories',
            },
        ),
        migrations.CreateModel(
            name='ImagesData',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Código')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/high')),
                ('thumbnail_image', models.ImageField(upload_to='images/thumbnail')),
                ('dsc_image', models.TextField(verbose_name='Descrição')),
                ('image_size', models.IntegerField(verbose_name='Tamanho')),
                ('image_width', models.IntegerField(verbose_name='Comprimento')),
                ('image_height', models.IntegerField(verbose_name='Altura')),
                ('image_type', models.CharField(choices=[('Arquivo jpeg', 'jpg'), ('Arquivo png', 'png'), ('Arquivo bmp', 'bmp')], max_length=20)),
                ('flag_public', models.BooleanField(default=True, verbose_name='Público')),
                ('insert_date', models.DateTimeField(auto_now_add=True, verbose_name='Data Inserção')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Data Edição')),
                ('fk_categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_images_categories', to='home.Categories', verbose_name='Categoria')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fk_images_users', to=settings.AUTH_USER_MODEL, verbose_name='Proprietário')),
            ],
            options={
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
                'db_table': 'ghome_images',
            },
        ),
    ]