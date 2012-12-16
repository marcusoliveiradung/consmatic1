# _*_ coding: utf8 _*_

from django.db import models
from django.forms import ModelForm
from django.core.files import File
#



#Importação de referência de Classes externas ( de outras áreas)
from cons.models import Consc 
from corpus.models import Especialidade,Tema

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

#----------------------------
#-- Classe Verbetografo
#-- -------------------------
class Verbetografo(models.Model):
    conscin =  models.ForeignKey(Consc, blank= 'True', null='True')
    iniciais = models.CharField(max_length=200)
    nome = models.CharField(max_length=400) 
    ano_nascimento = models.CharField(max_length=4)
    curriculum = models.TextField()
    
    def __unicode__(self):
        return self.conscin

#-- -----------------------------------------------------
#-- Table `enciclopedia`.`verbetografos`
#-- -----------------------------------------------------
###----------------------------------
##CREATE TABLE `enc_verbetografo` (
##  `id` int(11) NOT NULL AUTO_INCREMENT,
##  `iniciais` varchar(15) DEFAULT NULL,
##  `nome` varchar(50) NOT NULL,
##  `ano_nascimento` smallint(6) DEFAULT NULL,
##  `curriculum` text,
##  PRIMARY KEY (`id`),
##  UNIQUE KEY `nome_UNIQUE` (`nome`)
##--------------------------------------------------
###----------------------------
#-- Classe Divisao
#-- -------------------------
class Divisao(models.Model):
    nome =  models.CharField(max_length=50)
    sequencia = models.IntegerField() 
    numeracao = models.CharField(max_length=4)
    maximos = models.IntegerField()
    def __unicode__(self):
        return self.nome
#-- -----------------------------------------------------
#-- Table `enciclopedia`.`divisao`
#-- -----------------------------------------------------
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  `divisao` varchar(50) DEFAULT NULL,
#  `sequencia` int(11) DEFAULT NULL,
#  `numeracao` varchar(10) DEFAULT NULL,
#  `maximos` int(11) DEFAULT '0',
#  PRIMARY KEY (`id`),
#  UNIQUE KEY `id_UNIQUE` (`id`),
#  UNIQUE KEY `secao_UNIQUE` (`divisao`)

###------------------------------------------------------
#-- Classe Secao
#-- -----------------------------------------------------
class Secao(models.Model):
    divisao =  models.ForeignKey(Divisao, blank= 'True', null='True')
    nome =  models.CharField(max_length=50)
    terminador = models.CharField(max_length=1)
    item_fixo = models.IntegerField()
    item_basico = models.IntegerField()
    maximo = models.IntegerField()
    descricao = models.TextField()
    def __unicode__(self):
        return self.nome
#-- -----------------------------------------------------
#-- Table `enciclopedia`.`secao`
#-- -----------------------------------------------------
##CREATE TABLE `enciclopedia_secao` (
## `id` int(11) NOT NULL AUTO_INCREMENT,
##  `secao` varchar(50) NOT NULL,
##  `terminador` varchar(1) DEFAULT '.',
##  `divisao` int(11) NOT NULL,
##  `item_fixo` tinyint(4) NOT NULL DEFAULT '0',
##  `item_basico` tinyint(4) NOT NULL DEFAULT '0',
##  `maximo` tinyint(4) NOT NULL DEFAULT '0',
##  `descricao` text,







##----------------------------------------------

# CLASS VERBETE
class Verbete(models.Model):
#    #campos temporarios
     nome = models.CharField(max_length=150) 
     especialidade = models.ForeignKey(Especialidade, blank= 'True', null='True')
     tema = models.ForeignKey(Tema, blank= 'True', null='True')
     tertulia_aula = models.IntegerField() 
     tertulia_data= models.DateField()
     verbetografo =  models.ForeignKey(Verbetografo, blank= 'True', null='True')
     paginas = models.IntegerField()
     #remissiologia_id = models.IntegerField()
     #remissiologia_id1= models.IntegerField()  
#    data_criacao = models.DateTimeField('Data Inicial do Verbete:')
#    autor = models.CharField(max_length=400) 
     def __unicode__(self):
         return self.nome
    
#     def was_published_today(self):
#         return self.tertulia_data.date() == datetime.date.today()
#         was_published_today.short_description = 'Published today?'

# Create the form class.
class VerbeteForm(ModelForm):
    class Meta:
        model = Verbete

# Creating a form to add an article.
#        form = VerbeteForm()

# Creating a form to change an existing article.
#        verbete = Verbete.objects.get(pk=1)
#        form = Verbete(instance=verbete)
#
#    #

#CREATE  TABLE IF NOT EXISTS `enciclopedia`.`verbetes` (
# `id` INT(11) NOT NULL ,
#  `verbete` VARCHAR(150) NOT NULL ,
#  `especialidade` INT(11) NULL DEFAULT NULL ,
#  `tema` INT(11) NULL DEFAULT '2' ,
# `tertulia_aula` INT(11) NULL DEFAULT NULL
#--------------------------------------
#----------------------------------------

#CREATE TABLE `conteudo` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  `conteudo` text NOT NULL,
#  PRIMARY KEY (`id`),
# KEY `Indx_Conteudo` (`conteudo`(767)),
#  FULLTEXT KEY `Indx_Text` (`conteudo`)
#) ENGINE=MyISAM AUTO_INCREMENT=203480 DEFAULT CHARSET=latin1;
#------------------------------------
class Conteudo(models.Model):
     nome = models.CharField(max_length=500) 
  
     
     def __unicode__(self):
        return self.nome




#-- -----------------------------------------------------
#-- Table `enciclopedia`.`entrada`
#-- -----------------------------------------------------
#----------------------------------------
#CREATE TABLE `enciclopedia_entrada` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#verbete` int(11) NOT NULL,
#  `secao` int(11) NOT NULL,
#  `item_basico` int(11) NOT NULL,
#  `sequencia` int(11) NOT NULL,
#  `pagina` int(11) DEFAULT '0',
#  `conteudo` int(11) DEFAULT NULL,
#----------------------------
class Entrada(models.Model):
     verbete = models.ForeignKey(Verbete, blank= 'True', null='True') 
     secao = models.ForeignKey(Secao, blank= 'True', null='True')
     item_basico = models.IntegerField()
     sequencia = models.IntegerField() 
     paginas = models.IntegerField()
     conteudo= models.ForeignKey(Conteudo, blank= 'True', null='True')  
#    data_criacao = models.DateTimeField('Data Inicial do Verbete:')
#    autor = models.CharField(max_length=400) 
#    def __unicode__(self):
#        return self.verbete.nome
     def __unicode__(self):
         return self.verbete.nome + ' / ' + self.secao.nome + ' / '  + self.conteudo.nome























#  `verbetografo` INT(11) NULL DEFAULT '0' ,
#  `arquivo_doc_size` INT(11) NOT NULL DEFAULT '0' ,
#  `arquivo_doc` MEDIUMBLOB NULL DEFAULT NULL ,
#  `arquivo_pdf_size` INT(11) NOT NULL DEFAULT '0' ,
#  `arquivo_pdf` MEDIUMBLOB NULL DEFAULT NULL ,
#  `paginas` INT(11) NOT NULL DEFAULT '0' ,
#  `remissiologia_id` INT(11) NOT NULL ,
#  `remissiologia_id1` INT(11) NOT NULL ,
#---------------------------------------------------
#  PRIMARY KEY (`id`, `remissiologia_id`, `remissiologia_id1`) ,
#  UNIQUE INDEX `id_UNIQUE` (`id` ASC) ,
#  UNIQUE INDEX `verbete_UNIQUE` (`verbete` ASC) ,
# INDEX `especialidades_KEY` (`especialidade` ASC) ,
#  INDEX `verbetografos_KEY` (`verbetografo` ASC) ,
#  INDEX `tertulia_KEY` (`tertulia_aula` ASC) ,
#  INDEX `verbete_tema` (`tema` ASC) ,
#  INDEX `verbete_verbetografo` (`verbetografo` ASC) ,
#  INDEX `verbete_especialidade` (`especialidade` ASC) )
#ENGINE = MyISAM
#AUTO_INCREMENT = 6140
#DEFAULT CHARACTER SET = latin1;







#NOVAS CLASSES
