# Generated by Django 3.0.7 on 2020-07-05 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagesdata',
            old_name='image_id',
            new_name='pk_images',
        ),
    ]
