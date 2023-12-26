from django.contrib import admin
from .models import Categorie,Service,AdminScolaire,Accompagnement

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Service)
admin.site.register(AdminScolaire)
admin.site.register(Accompagnement)