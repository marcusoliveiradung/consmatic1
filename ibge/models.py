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

from django.db import models


class UnidadeFederativa(models.Model):
    REGIAO_CHOICES = (
        ('SL', 'Sul'),
        ('SD', 'Sudeste'),
        ('CO', 'Centro-Oeste'),
        ('NE', 'Nordeste'),
        ('NO', 'Norte'),
    )
    codigo_ibge = models.PositiveIntegerField(
        u'código IBGE',
        primary_key=True,
        unique=True,
        help_text='Código do estado segundo IBGE.'
    )
    nome = models.CharField(max_length=32)
    sigla = models.CharField(
        max_length=2,
        unique=True,
        help_text="Exemplo: <em>MG</em>.",
    )
    regiao = models.CharField('região', max_length=2, choices=REGIAO_CHOICES)
    populacao = models.PositiveIntegerField('população')

    class Meta:
        ordering = ('nome',)
        verbose_name = 'Unidade Federativa'
        verbose_name_plural = 'Unidades Federativas'

    def __unicode__(self):
        return self.nome


class Municipio(models.Model):
    codigo_ibge = models.PositiveIntegerField(
        u'código IBGE',
        primary_key=True,
        unique=True,
        help_text='Código do município segundo IBGE.'
    )
    codigo_mesorregiao = models.PositiveIntegerField(
        u'código mesorregião',
        blank=True,
        null=True
    )
    codigo_microrregiao = models.PositiveIntegerField(
        u'código microrregião',
        blank=True,
        null=True
    )
    nome = models.CharField(max_length=64)
    uf = models.ForeignKey(UnidadeFederativa, verbose_name='UF')
    is_capital = models.BooleanField('capital')
    populacao = models.PositiveIntegerField(u'população')
    is_polo = models.BooleanField(u'pólo')
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=8,
        null=True,
        blank=True,
        help_text='Exemplo: <em>-20,464</em>.'
    )
    longitude = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        null=True,
        blank=True,
        help_text='Exemplo: <em>-45,426</em>.'
    )

    class Meta:
        ordering = ('nome', 'codigo_ibge')
        verbose_name = 'município'
        verbose_name_plural = 'municípios'

    def __unicode__(self):
        return "%s, %s" % (self.nome, self.uf)
