# -*- coding: utf-8 -*-
from django import forms
from commom.utils import Utilities
from .models import Categories, ImagesData


class CategoriesForm(forms.ModelForm):
    dsc_cat = forms.CharField(
        label='Descrição',
        help_text='Descrição da Categoria',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Descrição',
                'required': True
            }
        )
    )

    def clean(self):
        self.dsc_cat = self.cleaned_data.get('dsc_cat')
        return self.cleaned_data

    class Meta:
        model = Categories
        fields = ('dsc_cat', )


class ImagesForm(forms.ModelForm):
    fk_categories = forms.TypedChoiceField(
        label='Categoria',
        help_text='Seleção da Categoria',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            },
        ),
        empty_value='Selecione uma Categoria...',
        choices=Utilities.get_database_choices(
            Categories, ['dsc_cat']
        )
    )
    image = forms.ImageField(
        label='Imagem', help_text='Imagem da galeria',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Imagem'
            }
        )
    )
    dsc_image = forms.CharField(
        label='Descrição', help_text='Descrição da Imagem',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Descrição',
                'required': True
            }
        )
    )
    flag_public = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control form-control-user'
            }
        ),
        label='Imagem Pública', help_text='Informe se a Imagem é Pública ou Proprietária'
    )

    def clean(self):
        self.fk_categories = self.cleaned_data.get('fk_categories')
        self.dsc_image = self.cleaned_data.get('dsc_image')
        self.image = self.cleaned_data.get('image')
        self.flag_public = self.cleaned_data.get('flag_public')
        return self.cleaned_data

    class Meta:
        model = ImagesData
        fields = (
            'fk_categories', 'dsc_image', 'image', 'flag_public',
        )
