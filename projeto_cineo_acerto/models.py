# _*_ coding: utf8 _*_
from django.db import models
from django.forms import ModelForm
from django.core.files import File
#
import datetime
 
 
#Importação de referência de Classes externas ( de outras áreas)
# authentication in Django
#from django.contrib.auth.models import User, Group
###Por enquanto está desativada a restrição ( amarração) de acesso/operação, associada ao usuário ou grupo

#Demais Classes "externas" associadas das APIs das/para as subáreas CONSC e Holoteca principalmente.

from cons.models  import Consc 
 
#User authentication in Django
#from django.contrib.auth.models import User, Group
###Por enquanto está desativada a restrição ( amarração) de acesso/operação, associada ao usuário ou grupo
 
#Demais Classes "externas" associadas das APIs das/para as subáreas CONSC e Holoteca principalmente.
 
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
     # data_criacao = models.DateTimeField(auto_now_add='True' ,blank= 'True', null='True')
     #autor =  models.ForeignKey(Autor,related_name= 'autor_acerto', blank= 'True', null='True')
     #data_criacao = models.DateTimeField('Data de Criação da Ficha:',blank= 'True', null='True')
#    autor = models.CharField(max_length=400) 
     reported_by = models.CharField('Terminólogo',max_length=50)#Terminologo
     created_at = models.DateTimeField('Data/Hora de Criação da Ficha:', blank='True', null='True')
     ########O campo Nome de Termiólogo Fichador entra pelo módulo de segurança (horizontal), atualmente no final da lista de campos na tela correspondente a esse modelo no ADMIN
     nome = models.CharField('Entrada - termo ou fraseologismo', max_length=150) 
#=======
 
     #data_criacao = models.DateTimeField('Data de Criação da Ficha:',blank= 'True', null='True')
#    autor = models.CharField(max_length=400)
     reported_by = models.CharField('Terminólogo:',max_length=50)#Terminologo
     created_at = models.DateTimeField('Data/Hora de Criação da Ficha:', blank='True', null='True')
     ########O campo Nome de Termiólogo Fichador entra pelo módulo de segurança (horizontal), atualmente no final da lista de campos na tela correspondente a esse modelo no ADMIN
     nome = models.CharField('Entrada - termo ou fraseologismo:', max_length=150)
     #Entrada: Ent. - Termo ou Fraseologismo (Lema).     
     ### Os seguintes attrs saem da classe básica de Terminologia (TERMoS), passando para a CLASSE das VARIÁVEIS:
     #***************************************************************<<< HEA
     ##categ_gram = models.CharField(max_length=02, blank= 'True', null='True') 
     #Referência ou Categoria Gramatical : Cat. - Referências Gramativcais (Classe e Gênero)
     ##reducao = models.CharField(max_length=02, blank= 'True', null='True') 
     #Redução: Rd. - (Abreviatura: Siglaçãoou acronímia, qdo houver)
     #****************************************************************
     
     especialidade_central = models.ForeignKey(Especialidade, related_name= 'especialidade_acerto', blank= 'True', null='True')
     #'Especialidade central (Área Temática):',
     #FK para Especialidade (classe Externa) 
     Tipo_termo = models.CharField('Tipo de termo', max_length=03, blank= 'True', null='True') 
     #Tipo do Termo ( ou Fraseologismo). Por enquanto, o domínio é:  TRM - Termo; FRA - Fraselogismo; ESP - Especialidades Conscienciológicas) 
     idioma_orig = models.ForeignKey(Idioma,related_name= 'idioma_acerto', blank= 'True', null='True')
     #'Idioma (da entrada):'
     #FK para Idioma (classe Externa)
     transc_fonet= models.CharField('Transcrição fonética',max_length=20, blank= 'True', null='True') 
#=======
     ##categ_gram = models.CharField(max_length=02, blank= 'True', null='True')
     #Referência ou Categoria Gramatical : Cat. - Referências Gramativcais (Classe e Gênero)
     ##reducao = models.CharField(max_length=02, blank= 'True', null='True')
     #Redução: Rd. - (Abreviatura: Siglaçãoou acronímia, qdo houver)
     #****************************************************************
     
     especialidade_central = models.ForeignKey(Especialidade,related_name= 'especialidade_acerto', blank= 'True', null='True')
     #FK para Especialidade (classe Externa)
     Tipo_termo = models.CharField(max_length=03, blank= 'True', null='True')
     #Tipo do Termo ( ou Fraseologismo). Por enquanto, o domínio é:  TRM - Termo; FRA - Fraselogismo; ESP - Especialidades Conscienciológicas)
     idioma_orig = models.ForeignKey(Idioma,related_name= 'idioma_acerto', blank= 'True', null='True')
     #FK para Idioma (classe Externa)
     transc_fonet= models.CharField(max_length=20, blank= 'True', null='True')
     #Transcrição Fonética: Tf.
     
     ### Os seguintes attrs saem da classe básica de Terminologia (TERMoS), passando para a CLASSE das VARIÁVEIS:
     #**********************************************************
     #status_termo= models.CharField(max_length=02,blank='True')
     #Status do Termo: St. (Normalizado - Nor. ou Proposição Neológica - Neo)
     #****************************************************************
     
     traduciologia = models.ManyToManyField("self",blank= 'True', null='True') #,related_name= 'traducao'
     #'Termos equivalentes (traduciologia):', 
     #AutoFK - Faz referência 'a própria classe (Termo), instâncias de termos de tradução para o termo.
     remissiologia = models.ManyToManyField("self", blank= 'True', null='True')   #,related_name= 'remissao
     #'Remissivas:',
     #AutoFK - Faz referência 'a própria classe (Termo), instâncias de termos de referência relevantes para o termo.
      

#=======
     traduciologia = models.ManyToManyField("self", blank= 'True', null='True') #,related_name= 'traducao'
     #AutoFK - Faz referência 'a própria classe (Termo), instâncias de termos de tradução para o termo.
     remissiologia = models.ManyToManyField("self", blank= 'True', null='True')   #,related_name= 'remissao
     #AutoFK - Faz referência 'a própria classe (Termo), instâncias de termos de referência relevantes para o termo.
 
 
     #tema = models.ForeignKey(Tema,related_name= 'conscin_acervo', blank= 'True', null='True')
     
      def __unicode__(self):
         return self.nome #+  ' / ' + self.especialidade_central.nome + ' / '  + self.idioma_orig.nome + ' / ' # + self.autor.conscin.nome
 
     class Meta:
         ordering = ["nome"]
#        verbose_name = "Termos ou Fraseologismos"
         verbose_name_plural = "Termos ou Fraseologismos"
         
         #permissions = (
        #('view_projeto', 'View projeto'),
        #)
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
     conteudo= models.CharField(max_length=250,blank= 'True', null='True') 
#    data_criacao = models.DateTimeField('DataData Inicial do Verbete:')
#    autor = models.CharField(max_length=400) 
     #def __unicode__(self):
     #    return self.termo.nome  + ' /    ' + self.variavel.nome + ' /      '  + self.conteudo      conteudo= models.TextField(blank= 'True', null='True')
#    data_criacao = models.DateTimeField('Data Inicial do Verbete:')
#    autor = models.CharField(max_length=400)
     #def __unicode__(self):
     #    return self.termo.nome  + ' /    ' + self.variavel.nome + ' /      '  +  self.conteudo
     
     class Meta:
         #ordering = ["sequencia"]
         verbose_name = "FICHA do TERMO ou FRASEOLOGISMO CONSCIENCIOLÓGICO:"
         verbose_name_plural = "FICHAMENTO do TERMO ou FRASEOLOGISMO CONSCIENCIOLÓGICO:" 
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

