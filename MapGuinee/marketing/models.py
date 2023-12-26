from django.db import models

from pedagogie.models import Categorie, Service

# Create your models here.

    

# classe pour stocker les ecole partenaire
class EcolePartenaire(models.Model):
    logo = models.ImageField(upload_to='media/logo_ecole',null=True,blank=True)
    nom_ecole = models.CharField(max_length= 64)
    adresse = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    service = models.ForeignKey(Service,on_delete = models.CASCADE)

    def __str__(self):
        return self.nom_ecole

# classe pour stocker les livres
class Livres(models.Model):
   
    titre = models.CharField(max_length=64)
    auteur = models.CharField(max_length=32)
    description = models.TextField()
    type_livre = models.ForeignKey(Categorie,on_delete = models.CASCADE)
    date_ajout = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.titre
    
#classe pour stocker les documents
class Documents(models.Model):
   
    titre_document = models.CharField(max_length= 32)
    contenu = models.TextField()
    image = models.ImageField(upload_to='media/img_doc',null=True,blank=True)
    video = models.FileField(upload_to = 'media/video_doc')
    type_doc = models.ForeignKey(Categorie,on_delete = models.CASCADE)

    def __str__(self):
        return self.titre_document
    


 


