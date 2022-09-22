
from rest_framework import serializers
from .models import Livre,LivreListe
class LivreSerializers(serializers.ModelSerializer):
    class Meta :
        model = Livre
        exclude =['id']

class LivreListeSerializers(serializers.ModelSerializer):
    class Meta :
        model = LivreListe
        fields = '__all__'