#-*- coding: utf-8 -*-

from django.db import models
#from holociclo.models.Dominios import Especialidade
from cons.models import *

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

#-- -----------------------------------------------------
#-- Classe Tipo_Assoc_`
#-- -----------------------------------------------------
class Tipo_Assoc(models.Model):
    #idTipo_Assoc INT NOT NULL ,
    nome = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nome
#-- -----------------------------------------------------
#-- Classe Teca`
#-- -----------------------------------------------------
class Teca(models.Model):
    
#  `id_teca` ***Não precisa declarar a PK Id_Classe; o Django já gera auto
#  `Tipologia_id_tipologia`   ***Subtipo ( Especialização) para Tipologia
    teca_sup= models.ForeignKey('self',related_name = 'teca_sup_',blank= 'True', null='True')
    #NXM RelashionshipRemissiologia. Volicioteca, potencioteca, politicoteca, argumentoteca, agrilhoteca e demo-cracioteca.
    #cASO UNIFIQUE OS RELACIONAMENTOS ( IDEAL DENTRO DA MODELAGEM DE CLASSES - E DA PŔOPRIA ÁLGEBRA RELACIONAL - THROUGH class Config_Teca(models.Model):
    nome = models.CharField(max_length=200)
    definiologia = models.TextField(max_length=300)
    correlacionologia = models.TextField(blank= 'True', null='True')   #O Atributo Correlacionologia na verdade é chave transposta ( link) nXn da Teca ( Verbete-prefixo da teca) para Verbete sem Geral
    #especialidade = models.ForeignKey(Especialidade,blank= 'True', null='True')
    etimologia = models.TextField(blank= 'True', null='True')#. O vocábulo abjunrir é o mesmo que abjugar, do idioma Latim, abjugo, “desprender do jugo, afastar, apartar, separar”. Aparece no Século XIX. 
    tematologia= models.NullBooleanField(blank= 'True', null='True')# Homeostática.
    #hominologia = models.ForeignKey(Hominologia,blank= 'True', null='True')# Homo sapiens abjuncius.
    exemplologia = models.TextField(blank= 'True', null='True')#. Ãchãryadeva, Srila; Os Valores da Liberdade; Deikman, Arthur; Liberdade Pessoal; Dewey, John; Liberdade e Cultura.
    #Amostragem com algumas instâncias ( objetos; ocorrências) ARTEFATOS relacionadas (ou sobsua TAXOLOGIA)
    def __unicode__(self):
        return self.nome


#-- -----------------------------------------------------
#-- Classe Artefato`
#-- -----------------------------------------------------
class Artefato(models.Model):
   #1.id_artefato ***Não precisa declarar a PK Id_Classe; o Django já gera auto
   #2.`Tipologia_id_tipologia = models.tipo_conteudo = models.ForeignKey(Tipologia)
   # Relacionamento (FK) para a Classe genérica de Tipologia prevendo categorização para o Artefato,
   # além da TECA   
 #   teca_principal = models.ForeignKey(Teca, blank= 'True', null='True')
 # Uma outra relação poderia ser o autorelacionamento NXN diretos entre os artefatos, independente
 # mente de de tipologia qqer ou da própria teca de insercao 
    artefato_tec = models.ManyToManyField(Teca,related_name="art_teca",symmetrical='False', through='Artefato_Teca',blank= 'True', null='True')
    #artefato_auto= models.ManyToManyField('self',through='Artefato_Remissiologia',symmetrical='False',blank= 'True', null='True')#related_name = 'artefato_artefato+',blank= 'True', null='True')
    #through= 'Artefato_Remissiologia'
    #teca =  models.ForeignKey(Teca)#, through="Artefato_Teca") 
    nome = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nome
#-------------
class  Artefato_Remissiologia(models.Model):
    from_artefato = models.ForeignKey(Artefato, related_name = "from_artefato_self",blank= 'True', null='True')
    to_artefato = models.ForeignKey(Artefato,related_name="to_artefato_self", blank= 'True', null='True')
    pags = models.CharField(max_length=200) 
    obs = models.TextField( blank= 'True', null='True')
    
    def __unicode__(self):
        return self.artefato.nome + ' / '+  self.teca.nome
            

#------------
class  Artefato_Teca(models.Model):
    artefato = models.ForeignKey(Artefato, blank= 'True', null='True')
    teca = models.ForeignKey(Teca, blank= 'True', null='True')
    ind_insercao_primaria = models.NullBooleanField(blank= 'True', null='True')
    obs = models.TextField( blank= 'True', null='True')
    
    def __unicode__(self):
        return self.artefato.nome + ' / '+  self.teca.nome
            
#-- ----------------------------------------------------

#-------------------------------
#-- Classe Assoc_Conscin
#-- -----------------------------------------------------
class Assoc_Consc_Artefato(models.Model):
    
    consc = models.ForeignKey(Consc, blank= 'True', null='True')
    tipo_assoc =models.ForeignKey(Tipo_Assoc, blank= 'True', null='True')
    teca = models.ManyToManyField(Teca, blank= 'True', null='True')
    artefato = models.ManyToManyField(Artefato, related_name="art", blank= 'True', null='True')
        
    def __unicode__(self):
        return self.consc.nome #+ '' + self.artefato.nome


#-- -----------------------------------------------------
#-- Table `holoteca`.`Teca_has_Teca`
#-- -----------------------------------------------------
class Config_Teca(models.Model):
    teca_a= models.ForeignKey(Teca, related_name = 'teca_sup_a',blank= 'True', null='True')
    teca_b= models.ForeignKey(Teca, related_name = 'teca_sup_b',blank= 'True', null='True')
    comentario = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.teca_a.nome + ' /  ' + self.teca_b.nome
#O ideal aqui seria implementar uma classe associativa NxM de autorelacionamento 
#entre as TECAS                         
                                                    
#- Logical Class structure for table `Atributologia`

#class Atributologia(models.Model):
#    nome_atributo =  models.CharField(max_length=200)
#  
#    def __unicode__(self):
#        return self.nome
                                                                                                                   
class Tipo_Atributo(models.Model):
    teca = models.ForeignKey(Teca,blank= 'True', null='True')
    nome = models.CharField(max_length=200,blank= 'True', null='True')
    desc = models.TextField(blank= 'True', null='True')
    def __unicode__(self):
        return self.teca.nome + ' / ' + self.nome 


#-- -----------------------------------------------------
#-- Table `holoteca`.`Config_Atributológica_ATTR`
#-- -----------------------------------------------------
class  Config_Atribut_ATTR(models.Model):
#`Config_Atributológica_ATRIBUTO_id_Config` INT NOT NULL ,
#  `Atributologia_id_atributo(Logical)` INT NOT NULL ,
    teca = models.ForeignKey(Teca,blank= 'True', null='True') 
    tipo_atributo = models.ForeignKey(Tipo_Atributo,blank= 'True', null='True')
    nome = models.CharField(max_length=200,blank= 'True', null='True')
    codigo =  models.CharField(max_length=010,blank= 'True', null='True')
    desc = models.TextField(blank= 'True', null='True')
    def __unicode__(self):
        return self.teca.nome + ' / '   + self.nome #+ self.tipo_atributo.nome
        

#--------------------------------------
#-- Classe Dominiologia Atributológica
#-- ----------------------------------------------------- 
#OBS. Essa Classe pode ser um autorelacionamento ( classe autassociativa) do/com a própria Atributologia, possivelmente#
   
class Dominiologia_Atribut(models.Model):
#  `idDominiologia Atributológica` INT NOT NULL ,
#  `Tipologia(Logical)_id_tipologia` INT NOT NULL ,
    atributo_dominio = models.ForeignKey(Config_Atribut_ATTR, blank= 'True', null='True')
    nome = models.CharField(max_length=200,blank= 'True', null='True')
    codigo = models.CharField(max_length=010,blank= 'True', null='True')
    desc = models.TextField(blank= 'True', null='True')
    valor = models.CharField(max_length=50,blank= 'True', null='True')
    def __unicode__(self):
        return  self.valor   # self.atributo_dominio.nome + '' +


#- -----------------------------------------------------
#- Classe Fichamento Artefato
#-- -----------------------------------------------------
class Fichamento_Artefato(models.Model):
#  `id_Fichamento Artefato` INT NOT NULL ,
    artefato =  models.ForeignKey(Artefato,blank= 'True', null='True')
    config_atribut_attr = models.ForeignKey(Config_Atribut_ATTR,blank= 'True', null='True')
    dominiologia_atribut =  models.ForeignKey(Dominiologia_Atribut,blank= 'True', null='True')
    conteudo =   models.CharField(max_length=200)
    def __unicode__(self):
        return self.artefato.nome + '  /  ' + self.config_atribut_attr.nome + '   /  ' # + self.dominiologia_atribut.valor 
#-- -----------------------------------------------------
#Tabela autoassociativa entre artefatos com declaração explícita
#class  Artefato_Remissiologia(models.Model):
#    artefato_faz_ref= models.ForeignKey(Artefato, related_name='artef1+',blank= 'True', null='True')
#    artefato_referenciado = models.ForeignKey(Artefato, related_name='artef2+',blank= 'True', null='True') 
#    obs = models.TextField( blank= 'True', null='True')
    #def __unicode__(self):
    #    return self.artefato_faz_ref.nome + '   ' + self.artefato_referenciado.nome
            
#---------------------------------------------------------------
#-- Classe Artefato_has_Ocurrences
##-- -----------------------------------------------------
class Artefato_has_Ocurrences(models.Model):
    artefato = models.ForeignKey(Artefato,blank= 'True', null='True') 
    #  Localização(LOGICAL)_idLocalização(LOGICAL)` INT NOT NULL ,
    local_fisica =  models.CharField(max_length=200)
    local_virtual = models.FileField(upload_to = 'conteudo') 
    
    def __unicode__(self):
        return self.artefato.nome + '  /   ' + self.local_fisica + ' / ' + self.local_virtual
    
    

    
#**************************************    
#  PRIMARY KEY (`Artefato_id_artefato`, `Localização(LOGICAL)_idLocalização(LOGICAL)`) ,
##  INDEX `fk_Artefato_has_Localização(LOGICAL)_Localização(LOGICAL)1` (`Localização(LOGICAL)_idLocalização(LOGICAL)` ASC) ,
#  INDEX `fk_Artefato_has_Localização(LOGICAL)_Artefato1` (`Artefato_id_artefato` ASC) ,
#  CONSTRAINT `fk_Artefato_has_Localização(LOGICAL)_Artefato1`
#    FOREIGN KEY (`Artefato_id_artefato` )
#    REFERENCES `holoteca`.`Artefato` (`id_artefato` )
#    ON DELETE NO ACTION
#    ON UPDATE NO ACTION,
#  CONSTRAINT `fk_Artefato_has_Localização(LOGICAL)_Localização(LOGICAL)1`
#    FOREIGN KEY (`Localização(LOGICAL)_idLocalização(LOGICAL)` )
##    REFERENCES `holoteca`.`Localização(LOGICAL)` (`idLocalização_virtual_física` )
#    ON DELETE NO ACTION
#    ON UPDATE NO ACTION)
#ENGINE = InnoDB;



