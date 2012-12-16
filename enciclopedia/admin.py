from django.contrib import admin

# from corpus - app
from enciclopedia.models import  Verbetografo, Secao, Divisao, Verbete, Conteudo, Entrada
#****************
#*****************
class EntradaInline(admin.StackedInline):
     model = Entrada
     extra = 3
#********************
class VerbeteAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['nome']}),
#        ('Info Data', {'fields': ['tertulia_data'], 'classes': ['collapse']}),
#    ]    
    inlines = [EntradaInline]
#******************************************
admin.site.register(Secao)
admin.site.register(Verbetografo)
admin.site.register(Divisao)
admin.site.register(Verbete,VerbeteAdmin)
admin.site.register(Entrada)#,EntradaAdmin)
admin.site.register(Conteudo)
#********************************
