from django.contrib import admin

# from corpus - app
from corpus.models import  Especialidade, Tema, Escala_Evolutiva, Faixas_Etaria, Procedex, Hominologia
#****************

#********************************
admin.site.register(Especialidade)

admin.site.register(Escala_Evolutiva)
admin.site.register(Faixas_Etaria)
admin.site.register(Procedex)

admin.site.register(Hominologia)

admin.site.register(Tema) # Cosmograma

#admin.site.register(Fase)

#ETC
#********************************




