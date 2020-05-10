from django.shortcuts import render
from .models import Student
from django.http import HttpResponse


def home(request):
    # text = "Nous, etudiants congolais en Afrique du Sud facons un challenge avec nos passeport.
    # Nous sommes obliges de repartir au pays quand nous devons renouveller nos visas Ceci est us
    # vrai probleme parcequ'on risque souvent de rater des cours ou examens, et meme d'avoir des
    # complications de repartir en Afrique du Sud si nos visas s'expire quand nous attendants
    # nos passeports.<br> C'est pour cela que l'association des etudiants congolais en afrique
    # du Sud qui se chargent de plusieurs affaires nous concernant s'etaient plaint a l'embassadeur
    #  concernant ce probleme. Et la solution avait ete de resenser le nombre d'etudiants
    # en Afrique comme ca ils pouront decider s'il faudra emmener la machine en afrique du sud..."

    return render(request, 'form/index.html',
    {'message': 'text'})
