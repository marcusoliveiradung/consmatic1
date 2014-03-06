# _*_ coding: utf8 _*_

from django.contrib import admin
from cons.models import Consc

from holoteca.models import  Tipo_Assoc, Artefato, Artefato_has_Ocurrences, Assoc_Consc_Artefato,Teca, Config_Teca, Dominiologia_Atribut, Tipo_Atributo, Config_Atribut_ATTR, Fichamento_Artefato
from holoteca.models import  Artefato_Teca, Artefato_Remissiologia #, Artefato_Remissiologia
#********ARTEFATO*e FICHA*************************************************
class Fichamento_Inline(admin.StackedInline):
    model = Fichamento_Artefato
    fieldsets = [
    ('Info Data', {'fields': ['artefato','config_atribut_attr','dominiologia_atribut','conteudo'],
    'classes': ['collapse']}),
    ]
    
                
class Artefato_Teca_Inline(admin.StackedInline):
    model = Artefato_Teca
    fieldsets = [
    ('Info Data', {'fields': ['artefato','teca','ind_insercao_primaria','obs'],
    'classes': ['collapse']}),
    ]
    
#    list_display = ('artefato','teca','ind_insercao_primaria','obs')
#    artefato = models.ForeignKey(Artefato, blank= 'True', null='True')
#    teca = models.ForeignKey(Teca, blank= 'True', null='True')
#    ind_insercao_primaria = models.NullBooleanField(blank= 'True', null='True')
#    obs = models.TextField( blank= 'True', null='True')
  

#class Artefato_Remissiologia_Inline(admin.TabularInline):
#    model = Artefato_Remissiologia

class Artefato_has_Ocurrences_Inline(admin.StackedInline):
    model = Artefato_has_Ocurrences
    
#**********************************
class ArtefatoAdmin(admin.ModelAdmin):
    model = Artefato
    inlines = [Artefato_Teca_Inline,Fichamento_Inline,Artefato_has_Ocurrences_Inline]#, Artefato_Remissiologia_Inline]
    extra = 20
##     fieldsets = [
##     (None,{'fields': ['descricao']}),
## Aqui no admin é que se pode alterar  a ordem de apresentação dos atributos    ]
#    fieldsets = [
#    ('Ref_Bibliog:', {'fields': ['artefato_remissiologia']}),
##        ('Info Data', {'fields': ['tertulia_data'], 'classes': ['collapse']}),
#    ],
##    list_display = ('artefato','teca','ind_insercao_primaria','obs')
#    list_display = ('artefato','teca','ind_insercao_primaria','obs')
   
    
#***************CLASSIFICAÇÂO**TECOLÓGICA da ARTEFATOLOGIA**************************************************************88

#class Artefato_Teca_Admin(admin.ModelAdmin):
#    model = Artefato
#    inlines = [Artefato_Teca_Inline]
#    extra = 8
    
class TecaAdmin(admin.ModelAdmin):
    model = Teca
    inlines = [Artefato_Teca_Inline]
    extra = 8     
        
#**************ATRIBUTOLOGIA E DOMÌNIOS***********************************************8  

class Dominiologia_Inline(admin.TabularInline):
    model = Dominiologia_Atribut
    

#**********************************
class Config_Atribut_ATTR_Admin(admin.ModelAdmin):
#     fieldsets = [
#     (None,{'fields': ['descricao']}),
#     ]
    model = Config_Atribut_ATTR
    inlines = [Dominiologia_Inline]
    extra = 8  

  
#*************************************************************8   
admin.site.register(Teca, TecaAdmin) 
admin.site.register(Tipo_Assoc)
admin.site.register(Artefato, ArtefatoAdmin)#, Artefato_Teca_Admin)
#admin.site.register(Artefato_Teca)
#admin.site.register(Artefato_has_Ocurrences)
admin.site.register(Fichamento_Artefato)
admin.site.register(Assoc_Consc_Artefato)
admin.site.register(Config_Teca)
admin.site.register(Artefato_Remissiologia)    
admin.site.register(Config_Atribut_ATTR, Config_Atribut_ATTR_Admin)







