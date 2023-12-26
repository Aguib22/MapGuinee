from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


# Create your models here.
class User(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
 
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **kwargs)


class Utilisateur(AbstractBaseUser, PermissionsMixin):
    
    nom = models.CharField(max_length=32, blank=True)
    prenom = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True,null=True,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = User()

    def __str__(self):
        return self.nom
    

class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

class Commentaire(models.Model):
     user = models.ForeignKey(Utilisateur,on_delete= models.CASCADE)
     contenu = models.TextField()
     date = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.user.nom
     
class Contact(models.Model):
     nom = models.CharField(max_length=32)
     prenom = models.CharField(max_length=32)
     email = models.EmailField(blank=True,null=True)
     subjet = models.TextField()

     def __str__(self):
          return self.nom

      


