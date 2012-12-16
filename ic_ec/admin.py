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
class AssocConscIc_EcInline(admin.TabularInline):
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
    
class AtividadeInline(admin.TabularInline):
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
    

class FaseInline(admin.TabularInline):
    model = FaseProjeto
    extra = 4


class ConteudoInline(admin.TabularInline):
    model = Conteudo
    extra = 3

class PortfolioInline(admin.TabularInline):
    model = Portfolio_Projeto
    extra = 3

class Portfolio_ProjetoAdmin(admin.ModelAdmin):
    model = Conteudo
    inlines = [PortfolioInline]
    extra = 3


class ProjetoAdmin(admin.ModelAdmin):
    model = Projeto
    inlines = [FaseInline, PortfolioInline]
    extra = 3
    



    
#class ProjetoInline(admin.TabularInline):
#    model = Projeto
#    extra = 3
    
#class AreaProjetoAdmin(admin.ModelAdmin):
#    model = Area
#    inlines = [ProjetoInline]
#    extra = 3
#
#


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
admin.site.register(Participacao)
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


