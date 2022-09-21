from datetime import datetime
from .models import Livre,LivreListe
from django.test import TestCase

class LivreTest(TestCase):

    def setUp(self) :
        self.livreliste_init=LivreListe()
        self.livreliste_init.name='Humour'
        self.livreliste_init.save()

        self.init_Livre=Livre()
        self.init_Livre.titre="Pipou"
        self.init_Livre.date_de_sorti=datetime.today()
        self.init_Livre.favorite=True
        self.init_Livre.Liste=self.livreliste_init

    def test_create_livre(self):

        self.livreliste_init=LivreListe()
        self.livreliste_init.name='Humour'
        self.livreliste_init.save()
        
        nb_Livre_before=Livre.objects.count()

        new_livre=Livre()
        new_livre.titre='mrbean'
        new_livre.date_de_sorti=datetime.today()
        new_livre.favorite=False
        new_livre.Liste=self.livreliste_init
        new_livre.save()

        nb_Livre_after=Livre.objects.count()

        self.assertTrue(nb_Livre_before+1==nb_Livre_after)

        
    def update_livre(self):
        self.assertEqual(self.init_Livre.titre,"Pipou")
        self.init_Livre.titre="change"
        self.init_Livre.save()

        test_init_livre=self.init_Livre.objects.get(pk=self.init_Livre.pk)
        self.assertEqual(self.test_init_livre.titre,'change')

    def delete_livre(self):
        nbr_livre_before_delete=Livre.objects.count()
        self.init_Livre.delete()
        nbr_livre_after_delete=Livre.objects.count()
        self.assertTrue(nbr_livre_after_delete==nbr_livre_before_delete-1)