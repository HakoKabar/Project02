from asyncio.windows_events import NULL
from pyexpat import model
from django.db import models

class  Livre(models.Model):
    titre=models.CharField(max_length=100)
    date_de_sorti=models.DateField()
    favorite=models.BooleanField()


    Liste=models.ForeignKey('LivreListe', null=False, on_delete=models.CASCADE)

    def __str__(self) :
        return self.titre


        
class LivreListe(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self) :
        return self.name
    

    """  class Meta:
        livre_name='Livre List'
        livre_name_pluieriel='Livres Lists'"""