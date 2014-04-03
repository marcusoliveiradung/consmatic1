# _*_ coding: utf8 _*_
from django.contrib import admin

from corpus.models import Especialidade
from holoteca.models  import  Dominiologia_Atribut, Tipo_Atributo, Config_Atribut_ATTR
from projeto_cineo_acerto.models import  Idioma, Variavel, Termo_ou_Fraseologismo,  Entrada 
#, Autor ,Conteudo,
#****************

     
     
  
#**************************
#class DominioInline(admin.StackedInline):
#      model =  Dominiologia_Atribut
#     fieldsets = [
#      ('Info Data', {'fields': ['variavel.','conteudo'],
#      'classes': ['collapse']}),
#      ]   
#********************
class VariavelInline(admin.StackedInline):
     model =  Variavel     
     ordering = ['sequencia']
     #fieldsets = [
     #('Info Data', {'fields': ['termo','variavel', 'conteudo', ],#'self.variavel.atributo',
     #'classes': ['collapse']# 
     #}),
     #     ]
#*********************
class VariavelAdmin(admin.ModelAdmin):
     model =  Variavel
     ordering = ['sequencia']
     list_filter = ['prioridade'] 
     
       
#********************
class EntradaInline(admin.StackedInline):
     model =  Entrada     
     fieldsets = [
     ('Detalhe', {'fields': ['termo','variavel', 'conteudo' ],'classes': ['collapse']}),
     ]
     list_filter = ['variavel'] 
     
#********************     
class TermoEspecialidadeInline(admin.StackedInline):
     model = Termo_ou_Fraseologismo  

class Termo_ou_FraseologismoAdmin(admin.ModelAdmin):
     model =  Termo_ou_Fraseologismo #, Config_Atribut_ATTR]
     list_filter = ['idioma_orig','especialidade_central'] 
     list_display = ('nome', 'data_criacao','especialidade_central')
     fieldsets = [
        (None,           {'fields': ['data_criacao']}),
        #('data_criacao', {'fields': ['pub_date']}),
     ]
     search_fields = ['nome']
     inlines = [EntradaInline]
     
     #ordering = ['sequencia']
     extra = 1
#********************
#class EntradaAdmin(admin.ModelAdmin):
#     model =  Entrada     
#     fieldsets = [
#     ('Info Data', {'fields': ['termo','variavel', 'conteudo', ],#'self.variavel.atributo',
#     #'classes': ['class TermoEspecialidadeInline(admin.StackedInline):
#     model = Termo_ou_Fraseologismo  collapse']# 
#     })],
#     list_filter = ['variavel'] 
             
#*************************

  
     
class TermoEspecialidadeAdmin(admin.ModelAdmin):
     model =  Especialidade  #, Config_Atribut_ATTR]
     search_fields = ['nome']
     list_filter = ['ordem_logica','ind_subespec'] 
     inlines = [TermoEspecialidadeInline]
     #ordering = ['sequencia']
     extra = 05
 #********************     

 #********************
 #class Atributo_Admin(admin.ModelAdmin):
 #   model = Termo_ou_Fraseologismo #, Config_Atribut_ATTR]
 #    inlines = [DominioInline]
 #    extra = 3
   
#******************************************
admin.site.register(Especialidade,TermoEspecialidadeAdmin)
admin.site.register(Variavel, VariavelAdmin)
#admin.site.register(Autor)
#admin.site.register(Idioma)
admin.site.register(Termo_ou_Fraseologismo, Termo_ou_FraseologismoAdmin)



#admin.site.register(Atributo_Admin)
#admin.site.register(Entrada)#,EntradaAdmin)
#admin.site.register(Conteudo)
#********************************
