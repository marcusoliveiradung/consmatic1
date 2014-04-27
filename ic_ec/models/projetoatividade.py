#-*- coding: utf-8 -*-


from django.db import models

from django.contrib.auth.models import User, Group
from ic_ec.models.base import TipoAtividade, FuncaoAtividade, FormaPagto
from ic_ec.models.emp import Area
from ic_ec.models.assocconscic_ec import AssocConscIc_Ec
from ic_ec.models.conteudo import Conteudo 




class Projeto(models.Model):
    """ Conjunto de atividades que tem uma data para acabar """
    
    nome = models.CharField(max_length=500) 
    descricao = models.TextField()
    inicio = models.DateTimeField('Inicio')
    duracao_meses = models.IntegerField()
    prioridade = models.IntegerField()
    area = models.ManyToManyField(Area, blank='True', null='True')
    tipo_atividade = models.ManyToManyField(TipoAtividade, blank='True', null='True')
    #artefatos_projeto = models.ManyToManyField(Conteudo, blank= 'True', null='True') #
    bola = models.ManyToManyField(Conteudo, through= "Portfolio_Projeto") #, through= "Utilizacao_Conteudo")  
    reported_by = models.ForeignKey(User)
    created_at = models.DateTimeField('Hora', blank='True', null='True') #

    def __unicode__(self):
        return self.nome
 

    class Meta:
        app_label = 'ic_ec'
        
    	permissions = (
        ('view_projeto', 'View projeto'),
        )

  
class Portfolio_Projeto(models.Model):
    conteudo = models.ForeignKey(Conteudo, related_name= 'cp')
    projeto = models.ForeignKey(Projeto, related_name= 'pc')
    obs = models.TextField()
     
    def __unicode__(self):
        return   self.projeto.nome    + " / " + self.conteudo.nome  + " / " #  +  self.atividade.inicioself.obs
 
    class Meta:
        app_label = 'ic_ec'



class FaseProjeto(models.Model): 
    """ Fase de um projeto. Ex: 
    
    """
    codigo_fase = models.CharField(max_length=100)  
    nome = models.CharField(max_length=500) 
    descricao = models.TextField()  
    inicio = models.DateTimeField('Inicio')
    fim = models.DateTimeField('Fim')
    projeto = models.ForeignKey(Projeto)
    fase_projeto_sup = models.ForeignKey('self', blank= 'True', null='True')
    
    def __unicode__(self):
        return self.nome

    class Meta:
        app_label = 'ic_ec'


class Atividade(models.Model):
    """ Evento em si ou Ocorrencia da Atividade """
    
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    inicio = models.DateTimeField('Inicio')
    fim = models.DateTimeField('Fim')
    tipo_atividade = models.ForeignKey(TipoAtividade)
    atividade_projeto_sup = models.ForeignKey('self', blank= 'True', null='True') 
    area = models.ManyToManyField(Area, blank= 'True', null='True')
    assocconscic_ec = models.ManyToManyField(AssocConscIc_Ec, through="Participacao") 
    uso_artefato = models.ManyToManyField(Conteudo, blank= 'True', null='True') #, through= "Utilizacao_Conteudo")  
    projeto = models.ManyToManyField(Projeto, blank= 'True', null='True')
    obs = models.TextField(blank= 'True', null='True')
    
    #pessoal_envolvido = models.ManyToManyField(AssocConscin,related_name='pessoal_envolvido', blank= 'True', null='True')
   # producao = models.ManyToManyField(Conteudo, blank= 'True', null='True') #avaliar dependencia a Conteudo
 
    def __unicode__(self):
        return self.nome
   
    class Meta:
        app_label = 'ic_ec'

 
class Participacao(models.Model):
    atividade = models.ForeignKey(Atividade)
    assocconscic_ec = models.ForeignKey(AssocConscIc_Ec)
    funcao = models.ForeignKey(FuncaoAtividade, blank=True, null=True)
###   area = models.ForeignKey(Area,blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    ind_pagto = models.NullBooleanField(blank=True, null=True)
    valor_pago = models.IntegerField(blank=True, null=True)
    forma_pagto = models.ForeignKey(FormaPagto,blank=True, null=True)
    ind_presenca = models.NullBooleanField(blank=True, null=True)
    percentual_presenca = models.SmallIntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return self.atividade.nome    + " / " + self.assocconscic_ec.consc.nome  + " / " #  +  self.atividade.inicio
    
    class Meta:
        app_label = 'ic_ec'

 
#class Utilizacao_Conteudo(models.Model):
#    conteudo = models.ForeignKey(Conteudo)    
#    evento   = models.ForeignKey(Evento) 
   ## descricao   = models.CharField(max_length=100)
    
#    def __unicode__(self):
#        return self.evento.nome + ' / ' + self.conteudo.nome   
    
#    class Meta:
#        app_label = 'ic'
 
