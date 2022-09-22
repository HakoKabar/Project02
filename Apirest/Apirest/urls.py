
from django.contrib import admin
from django.urls import path,include
from livre.urls import routers_Livre_and_livrelist as rlal
from  rest_framework import routers

router_principale=routers.DefaultRouter()
router_principale.registry.extend(rlal.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router_principale.urls)),
]
