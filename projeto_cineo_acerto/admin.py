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
     ('Info Data', {'fields': ['termo','variavel', 'conteudo' ],'classes': ['collapse']}),
     ]
     list_filter = ['variavel'] 
     
#********************     
class Termo_ou_FraseologismoAdmin(admin.ModelAdmin):
     model =  Termo_ou_Fraseologismo #, Config_Atribut_ATTR]
     search_fields = ['nome']
     inlines = [EntradaInline]
     list_filter = ['idioma_orig','especialidade_central'] 
     #ordering = ['sequencia']
     extra = 3
#********************
#class EntradaAdmin(admin.ModelAdmin):
#     model =  Entrada     
#     fieldsets = [
#     ('Info Data', {'fields': ['termo','variavel', 'conteudo', ],#'self.variavel.atributo',
#     #'classes': ['collapse']# 
#     })],
#     list_filter = ['variavel'] 
             
#*************************

class EspecialidadeInline(admin.StackedInline):
     model =  Especialidade      
     
class Termo_EspecialidadeAdmin(admin.ModelAdmin):
     model =  Termo_ou_Fraseologismo  #, Config_Atribut_ATTR]
     #search_fields = ['nome']
     #list_filter = ['idioma_orig','especialidade_central'] 
     inlines = [EspecialidadeInline]
     #ordering = ['sequencia']
     extra = 10
 #********************     

 #********************
 #class Atributo_Admin(admin.ModelAdmin):
 #   model = Termo_ou_Fraseologismo #, Config_Atribut_ATTR]
 #    inlines = [DominioInline]
 #    extra = 3
   
#******************************************
admin.site.register(Variavel, VariavelAdmin)
#admin.site.register(Autor)
#admin.site.register(Idioma)
admin.site.register(Termo_ou_Fraseologismo, Termo_ou_FraseologismoAdmin)
#admin.site.register(Termo_EspecialidadeAdmin)


#admin.site.register(Atributo_Admin)
#admin.site.register(Entrada)#,EntradaAdmin)
#admin.site.register(Conteudo)
#********************************
