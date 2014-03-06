#-*- coding: utf-8 -*-
from django.db import models

from corpus.models import Especialidade
#from ic.models.conscin import *

#class Classe(models.Model):
#    nome = models.CharField(max_length=200) 
   # data_nascimento = models.DateField('Data de Nascimento', blank= 'True', null='True')
   # email = models.EmailField( blank= 'True', null='True')
   # tel_resid = models.CharField("Telefone Residencial", max_length=20,blank= 'True', null='True')
   # tel_cel = models.CharField("Telefone Celular", max_length=20, blank= 'True', null='True')
   # tel_cel_2 = models.CharField("Telefone Celular 2", max_length=20, blank= 'True', null='True')    
#    def __unicode__(self):
#       return self.nome


   # class Meta:
   #     app_label = 'ic'
   
class Ic_Ec(models.Model):
    
    especialidade =  models.ForeignKey(Especialidade, blank= 'True', null='True')
    nome = models.CharField(max_length=200)
    categoria_transempresarial = models.CharField(max_length=2)
    estagio_transempresa = models.CharField(max_length=5)
#    Pessoa = models.OneToOneField(Pessoa, primary_key=True)                                           
 
    def __unicode__(self):
        return self.categoria_transempresarial + " " + self.nome  
   
#   
   
#class Area(models.Model):
#    """ Ex: Banco de Dados, Comunicacao etc.. 
#    
#    Pode conter sub-areas (campo area_sup)
#    """
#    nome = models.CharField(max_length=200)  
#    descricao = models.TextField()   
#    area_sup= models.ForeignKey('self', related_name = 'area_sup_self', 
#                                blank= 'True', null='True')
    
    
#    def __unicode__(self):
#        return self.nome

#    class Meta:
#        app_label = 'ic'