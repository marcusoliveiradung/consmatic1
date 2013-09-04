# _*_ coding: utf8 _*_
dir

from django.db import models
from django.core.files import File

#----- Evolution for enc
#from django_evolution.mutations import *
#from django.db import models
#
#MUTATIONS = [
#    DeleteField('Secao_Enc', 'verbete')
#]
#----------------------


import datetime
# Create your models here.
#----------------------------------------------
#Escalas




#Escala  Evolutiva Conscienciológica
class Escala_Evolutiva(models.Model):
    nivel  = models.CharField(max_length=200) 
    descricao = models.CharField(max_length=300)  
    def __unicode__(self):
        return self.nivel


#Quadros
#Quadro Sinopticos 
#das Especialidades:
class Especialidade(models.Model):
    nome  = models.CharField(max_length=200) 
     
    descricao = models.CharField(max_length=300)  
    ordem_logica = models.IntegerField()
    espec_assoc = models.ForeignKey("self",blank= 'True', null='True')
    #espec_assoc = models.ManyToManyField("self",blank= 'True', null='True') 
    def __unicode__(self):
        return self.nome
    
# Listas e Tabelas

class Faixas_Etaria(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    #localizacao_parageografica = models.CharField(max_length=300,blank= 'True', null='True')
    #rRelacao_geografica = models.CharField(max_length=300,blank= 'True', null='True')
    def __unicode__(self):
        return self.nome
    
class Procedex(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    localizacao_parageografica = models.CharField(max_length=300)
    relacao_geografica = models.CharField(max_length=300)
    def __unicode__(self):
        return self.nome

#---------------------------------------------
#---------------------------------------------
#NOVAS CLASSES 
class Hominologia(models.Model): 
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    def __unicode__(self):
        return self.nome
    
#---------------------------------------------------------
#___Temas Conscienciológicos ( usados para/no Cosmograma)___________________________________________________
class Tema(models.Model):
    tema  = models.CharField(max_length=50) 
    def __unicode__(self):
        return self.tema
#---------------------------------------------
#---------------------------------------------
