from django.contrib import admin

# from corpus - app
from corpus.models import  Especialidade, Tema, Escala_Evolutiva, Faixas_Etaria, Procedex, Hominologia
#****************
class EspecialidadeAdmin(admin.ModelAdmin):
     model = Especialidade
     #inlines = [EspecialidadeInline]
     extra = 3
     search_fields = ['nome']
     list_filter = ['ordem_logica','ind_subespec', 'espec_sup'] 
#********************************
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Escala_Evolutiva)
admin.site.register(Faixas_Etaria)
admin.site.register(Procedex)

admin.site.register(Hominologia)

admin.site.register(Tema) # Cosmograma

#admin.site.register(Fase)

#ETC
#********************************




