# -*- coding: utf-8 -*-
#
# Copyright (c) 2011 Guilherme Gondim
# Copyright (c) 2009 Interlegis
#
# This file is part of Django IBGE.
#
#   Django IBGE is free software under terms of the GNU General Public License
#   version 3 (GPLv3) as published by the Free Software Foundation.  See the
#   file README for copying conditions.
#

import ibge
from django.contrib import admin


class UnidadeFederativaAdmin(admin.ModelAdmin):
    list_display = ('codigo_ibge', 'nome', 'sigla', 'regiao', 'populacao')
    list_display_links = ('codigo_ibge', 'nome')
    list_filter = ('regiao',)
    search_fields = ('codigo_ibge', 'nome', 'sigla', 'regiao')


class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('codigo_ibge', 'nome', 'uf', 'is_capital', 'populacao',
                    'is_polo')
    list_display_links = ('codigo_ibge', 'nome')
    list_filter = ('is_capital', 'is_polo', 'uf')
    fieldsets = (
        (None, {
            'fields': ('codigo_ibge', 'codigo_mesorregiao',
                       'codigo_microrregiao', 'nome', 'uf', 'is_capital',
                       'populacao', 'is_polo')
        }),
        ('Posição geográfica', {
            'fields': ('latitude', 'longitude'),
        }),
    )
    search_fields = ('codigo_ibge', 'codigo_mesorregiao',
                     'codigo_microrregiao', 'nome', 'uf__nome', 'uf__sigla')


admin.site.register(ibge.models.UnidadeFederativa, UnidadeFederativaAdmin)
admin.site.register(ibge.models.Municipio, MunicipioAdmin)
