from django.db import models

# Create your models here.
class Categorie(models.Model):
    categorie = models.CharField(max_length=128)

    def __str__(self):
        return self.categorie
    

class Service(models.Model):
    nom_service = models.CharField(max_length=32)
    desc_service = models.TextField()
    type_service = models.ForeignKey(Categorie,on_delete = models.CASCADE)

    def __str__(self):
        return self.nom_service
    
class AdminScolaire(models.Model):
    type_admins = [("Gestion_ecole","Gestion_ecole"),
                   ("dev_ecole","dev_ecole")]
    experience = models.TextField()
    conseil = models.TextField()
    type_admin = models.CharField(max_length = 123, 
                                  choices = type_admins,default = "Gestion_ecole") 

    def __str__(self):
        return self.type_admin
    
class Accompagnement(models.Model):
    type_accompagnement = [("Coaching","Coaching"),
                   ("Soutient Scolaire","Soutient Scolaire")]
    methode = models.TextField()
    conseil_acc = models.TextField()
    type_acc = models.CharField(max_length = 123,
                                 choices = type_accompagnement,default = "Coaching")
    def __str__(self):
        return self.type_acc