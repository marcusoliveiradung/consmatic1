# _*_ coding: utf8 _*_

#dir
from django.db import models
from django.forms import ModelForm
from django.core.files import File
#
import datetime


#Importação de referência de Classes externas ( de outras áreas)
from cons.models  import Consc 
from corpus.models import Especialidade,Tema
from holoteca.models import Dominiologia_Atribut, Config_Atribut_ATTR

#----- Evolution for enc
#from django_evolution.mutations import *
#from django.db import models
#
#MUTATIONS = [
#    DeleteField('Secao_Enc', 'verbete')
#]
#----------------------



# Create your models here.

#----------------------------
#-- Classe Autor Terminologico ou Fraseologistico
#-- -------------------------
#class Autor(models.Model):
#    #nome = models.CharField(max_length=400) 
#    conscin =  models.ForeignKey(Consc, related_name= 'conscin_acerto', blank= 'True', null='True')
#    iniciais = models.CharField(max_length=200)
#    ano_nascimento = models.CharField(max_length=4)
#    curriculum = models.TextField()
#    def __unicode__(self):
 #       return self.conscin.nome


###----------------------------
#-- Classe Idioma
#-- -------------------------
class Idioma(models.Model):
    nome =  models.CharField(max_length=50)
    sequencia = models.IntegerField() 
    #numeracao = models.CharField(max_length=4)
    #maximos = models.IntegerField()
    def __unicode__(self):
        return self.nome


###------------------------------------------------------
#-- Classe Secao
#-- -----------------------------------------------------
class Variavel(models.Model):
    #idioma =  models.ForeignKey(Idioma,related_name= 'idioma_acervo', blank= 'True', null='True')
    atributo = models.ForeignKey(Config_Atribut_ATTR, blank= 'True', null='True')
    nome =  models.CharField(max_length=50)
    codigo = models.CharField(max_length=06, blank= 'True', null='True')
    descricao = models.TextField(blank= 'True', null='True')
    sequencia = models.CharField(max_length=02)
    prioridade = models.CharField(max_length=02) # Nível de Preenchimento - 1- MIN; 2- BAS; 3 - EXA
    #    item_fixo = models.IntegerField()
    #    item_basico = models.IntegerField()
    #    maximo = models.IntegerField( blank= 'True', null='True')
    #    variavel_sup = 
    
    def __unicode__(self):
        return    self.nome # + ' / '+ self.sequencia + ' / ' + self.prioridade  #----------------------------------------------
     
    class Meta:
        ordering = ["sequencia"]
        verbose_name_plural = "variaveis" 


# CLASS TERMO
class Termo_ou_Fraseologismo(models.Model):
     #Data de Criação/Nome do Terminólogo Fichador
     data_criacao = models.DateField(blank= 'True', null='True')
     ########O campo Nome de Termiólogo Fichador entra pelo módulo de segurança (horizontal), atualmente no final da lista de campos na tela correspondente a esse modelo no ADMIN
     nome = models.CharField(max_length=150) 
     #Entrada: Ent. - Termo ou Fraseologismo (Lema).
     categ_gram = models.CharField(max_length=02, blank= 'True', null='True') 
     #Referência ou Categoria Gramatical : Cat. - Referências Gramativcais (Classe e Gênero)
     Reducao = models.CharField(max_length=02, blank= 'True', null='True') 
     #Redução: Rd. - (Abreviatura: Siglaçãoou acronímia, qdo houver)
     especialidade_central = models.ForeignKey(Especialidade,related_name= 'especialidade_acerto', blank= 'True', null='True')
     idioma_orig = models.ForeignKey(Idioma,related_name= 'idioma_acerto', blank= 'True', null='True')
     transc_fonet= models.TextField(blank= 'True', null='True') 
     #Transcrição Fonética: Tf.
     status_termo= models.CharField(max_length=02, blank= 'True', null='True')
     #Status do Termo: St. (Normalizado - Nor. ou Proposição Neológica - Neo)
     traduciologia = models.ManyToManyField("self", blank= 'True', null='True') #,related_name= 'traducao'
     remissiologia = models.ManyToManyField("self", blank= 'True', null='True')   #,related_name= 'remissao
      

     #tema = models.ForeignKey(Tema,related_name= 'conscin_acervo', blank= 'True', null='True')
     #autor =  models.ForeignKey(Autor,related_name= 'autor_acerto', blank= 'True', null='True')
#     num_apresentacao = models.IntegerField() 
          #paginas = models.IntegerField()
     #remissiologia_id = models.IntegerField()
     #remissiologia_id1= models.IntegerField()  
#    data_criacao = models.DateTimeField('Data Inicial do Verbete:')
#    autor = models.CharField(max_length=400) 
     
     def __unicode__(self):
         return self.nome #+  ' / ' + self.especialidade_central.nome + ' / '  + self.idioma_orig.nome + ' / ' # + self.autor.conscin.nome 

     class Meta:
         ordering = ["nome"]
#        verbose_name = "Termos ou Fraseologismos"
         verbose_name_plural = "Termos ou Fraseologismos"

#     def was_published_today(self):
#        return self.data_criacao.date() == datetime.date.today()
#     was_published_today.short_description = 'Published today?'

# Create the form class.
#class Termo_ou_FraseologismoForm(ModelForm):
#    class Meta:
#        model = Termo_ou_Fraseologismo

#-- -----------------------------------------------------
#-- Table entrada no ACERVO - Fichamento Terminologico
#------------------------------------
class Conteudo(models.Model):
     nome = models.CharField(max_length=500) 
     def __unicode__(self):
        return self.nome  



#-- -----------------------------------------------------
#-- Table entrada no ACERVO - Ficamento Terminologico
#-- -----------------------------------------------------
#----------------------------------------

class Entrada(models.Model):
     termo = models.ForeignKey(Termo_ou_Fraseologismo) 
     variavel = models.ForeignKey(Variavel)#Variavel)
     ##variavel = models.ForeignKey(Variavel)#Variavel)
     ##idioma = models.ForeignKey(Idioma,blank= 'True', null='True')
     #item_basico = models.IntegerField()
     #sequencia = models.IntegerField() 
     #paginas = models.IntegerField()
     conteudo= models.TextField(blank= 'True', null='True') 
#    data_criacao = models.DateTimeField('Data Inicial do Verbete:')
#    autor = models.CharField(max_length=400) 
     def __unicode__(self):
         return self.termo.nome  #+ ' / ' + self.variavel.nome + ' / '  +  self.conteudo 

     class Meta:
         #ordering = ["sequencia"]
         verbose_name = "FICHA do TERMO ou FRASEOLOGISMO CONSCIENCIOLÓGICO:"
         verbose_name_plural = "FICHA do TERMO ou FRASEOLOGISMO CONSCIENCIOLÓGICO:" 





















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

