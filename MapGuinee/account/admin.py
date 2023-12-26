from django.contrib import admin
from .models import Commentaire, Contact, Utilisateur

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Commentaire)
admin.site.register(Contact)
