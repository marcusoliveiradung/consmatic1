# _*_ coding: utf8 _*_

from django.contrib import admin
#from guardian.admin import admin.ModelAdmin

#from ic_ec.models.consc import  Consc 
from cons.models import Consc
from ic_ec.models.base import  TipoAtividade, FuncaoAtividade, FormaPagto

from ic_ec.models.emp import Area
from ic_ec.models.assocconscic_ec import TipoAssocConscIc_Ec, AssocConscIc_Ec #, AssocConscin_Area
from ic_ec.models.conteudo import Conteudo, TipoConteudo
from ic_ec.models.projetoatividade import Atividade,  Projeto,\
     FaseProjeto, Participacao, Portfolio_Projeto  #, Utilizacao_Conteudo
 # Conteudo_AssocConscin #, Conteudo_Area

#TIPOASSOCCONSCIN ADMIN
class AssocConscIc_EcInline(admin.StackedInline):
#     fieldsets = [
#     (None,{'fields': ['descricao']}),
#     ]
    model = AssocConscIc_Ec

class TipoAssocConscIc_EcAdmin(admin.ModelAdmin):
    model = TipoAssocConscIc_Ec
    inlines = [AssocConscIc_EcInline]
    extra = 7
    
class ParticipacaoInline(admin.StackedInline):
    model = Participacao
    fieldsets = [
    ('Info Data', {'fields': ['atividade','assocconscic_ec','funcao','obs','ind_pagto','valor_pago','forma_pagto',
    'ind_presenca','percentual_presenca'],
    'classes': ['collapse']}),
    ]
    #-------------------------------------------------
    #atividade = models.ForeignKey(Atividade)
    #assocconscic_ec = models.ForeignKey(AssocConscIc_Ec)
    #funcao = models.ForeignKey(FuncaoAtividade, blank=True, null=True)
###   area = models.ForeignKey(Area,blank=True, null=True)
    #obs = models.TextField(blank=True, null=True)
    #ind_pagto = models.NullBooleanField(blank=True, null=True)
    #valor_pago = models.IntegerField(blank=True, null=True)
    #forma_pagto = models.ForeignKey(FormaPagto,blank=True, null=True)
    #ind_presenca = models.NullBooleanField(blank=True, null=True)
    #percentual_presenca = models.SmallIntegerField(blank=True, null=True)
    #----------------------------------------------------
class AtividadeInline(admin.StackedInline):
#     fieldsets = [
#     (None,{'fields': ['descricao']}),
#     ]
    model = Atividade
    

#**********************************
class AtividadeAdmin(admin.ModelAdmin):
#     fieldsets = [
#     (None,{'fields': ['descricao']}),
#     ]
    model = Atividade
    inlines = [ParticipacaoInline]
    extra = 4


class TipoAtividadeAdmin(admin.ModelAdmin):
#    fieldsets = [ 
#     ('Equipe', {'fields': ['equipe_atividade'], 'classes':['collapse']}),
#     ]
    model = TipoAtividade
    inlines = [AtividadeInline]
    extra = 3


   

class AssocConscIc_EcAdmin(admin.ModelAdmin):
    model = AssocConscIc_Ec   
    inlines = [ParticipacaoInline]
    extra= 7 

class Arealine(admin.TabularInline):
    model = Area
    extra = 4

class AreaAdmin(admin.ModelAdmin): #(admin.ModelAdmin)
    #     fieldsets = [ 
#     ('IC', {'fields': ['ic'], }),
#     ]
    model = Area
    inlines = [Arealine]
    extra = 10
    

class FaseInline(admin.StackedInline):
    model = FaseProjeto
    #fieldsets = [  'classes':['collapse']],
    fieldsets = [
    ('Info Data', {'fields': ['codigo_fase','nome','descricao','inicio','fim','projeto','fase_projeto_sup'],
    'classes': ['collapse']}),
    ]
    
  
class PortfolioInline(admin.StackedInline):
    model = Portfolio_Projeto
  

class ProjetoAdmin(admin.ModelAdmin):
    model = Projeto
    inlines = [FaseInline, PortfolioInline]
    extra = 3
    
class ConteudoInline(admin.StackedInline):
    model = Conteudo
    fieldsets = [
    ('Info Data', {'fields': ['nome','descricao','artefato_area','funcaoatividade','assocconscic_ec'
    ,'conteudo'],  'classes': ['collapse']}),
    ]

class TipoConteudoAdmin(admin.ModelAdmin):
    model = TipoConteudo
    inlines = [ConteudoInline]
    extra = 3

#admin.site.register(Consc)
admin.site.register(TipoAssocConscIc_Ec, TipoAssocConscIc_EcAdmin)
admin.site.register(AssocConscIc_Ec, AssocConscIc_EcAdmin) 
#admin.site.register(AssocCadmin.ModelAdminonscin_Area) 
admin.site.register(Area, AreaAdmin)
#admin.site.register(AreaProjetoAdmin)
admin.site.register(TipoAtividade, TipoAtividadeAdmin)
admin.site.register(FuncaoAtividade)
admin.site.register(FormaPagto)
admin.site.register(Atividade, AtividadeAdmin)
#admin.site.register(Participacao)
#admin.site.register(Utilizacao_Conteudo)
admin.site.register(TipoConteudo, TipoConteudoAdmin)
admin.site.register(Conteudo)
#admin.site.register(Conteudo_Area)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Portfolio_Projeto)#, Portfolio_ProjetoAdmin)

#********************************
#Exs:
#fieldsets = [
        #(None, {'fields': ['id']}),
        #('Artefato', {'fields': ['artefato']}),
        #('Conteudo', {'fields': ['conteudo'], 'classes': ['collapse']})]
        #('Arquivo_Associado',        {'fields': ['foto.name']}), 


