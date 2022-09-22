
from rest_framework import routers

from .views import Livre_ViewSet, livreLIste_ViewSet


routers_Livre_and_livrelist =routers.DefaultRouter()
routers_Livre_and_livrelist.register('livre',Livre_ViewSet)
routers_Livre_and_livrelist.register('LivreList',livreLIste_ViewSet)