from django.contrib import admin

# from corpus - app
from projeto_cineo_acerto.models import  Idioma, Variavel, Termo_ou_Fraseologismo, Conteudo, Entrada #, Autor
#****************
#*****************
class EntradaInline(admin.StackedInline):
     fieldsets = [
     ('Info Data', {'fields': ['variavel','termo','conteudo'], 'classes': ['collapse']}),
     ]   
     model = Entrada
     extra = 3
#********************
class Termo_ou_FraseologismoAdmin(admin.ModelAdmin):
   
     inlines = [EntradaInline]
   
    
   
#******************************************
admin.site.register(Variavel)
#admin.site.register(Autor)
admin.site.register(Idioma)
admin.site.register(Termo_ou_Fraseologismo,Termo_ou_FraseologismoAdmin)
admin.site.register(Entrada)#,EntradaAdmin)
admin.site.register(Conteudo)
#********************************
