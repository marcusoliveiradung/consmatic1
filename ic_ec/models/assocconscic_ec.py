#-*- coding: utf-8 -*-

from django.db import models

#from ic_ec.models.consc import Consc
from cons.models import Consc
from ic_ec.models.emp import Area

class TipoAssocConscIc_Ec(models.Model):
 
    nome = models.CharField(max_length=200)  
    descricao = models.TextField()   

    def __unicode__(self):
        return self.nome
    
    class Meta:
        app_label = 'ic_ec' 

class AssocConscIc_Ec(models.Model):
    area_trabalho =  models.ManyToManyField(Area,blank='True', null='True') #through = "AssocConscin_Area",
    #areaic_assoc = models.ForeignKey(Area)
    tipo_assocconscic_ec = models.ForeignKey(TipoAssocConscIc_Ec)
    consc =  models.ForeignKey(Consc)
    ind_tenepes = models.NullBooleanField()
    ind_docencia = models.NullBooleanField()
    obs_docencia = models.TextField(blank='True')    
     
                                           

    def __unicode__(self):
        return self.consc.nome 
    
    class Meta:
        app_label = 'ic_ec'


#class AssocConscin_Area(models.Model):
#    assocconscin = models.ForeignKey(AssocConscin)
#    area = models.ForeignKey(Area)  
     
#    def __unicode__(self):
#        return self.
       
#    class Meta:
#        app_label = 'ic'
#        
