from django.shortcuts import render
from .models import Documents, EcolePartenaire,Livres

# Create your views here.
def home(request):
    return render(request,'marketing/index.html')

def marketing(request):
    document = Documents.objects.filter(type_doc__categorie ='marketing')
    livre = Livres.objects.filter(type_livre__categorie = 'marketing')
    ecole = EcolePartenaire.objects.all()
    context = {'livre':livre,'document':document,
               'ecole':ecole}
    return render(request,'marketing/marketing.html',context)