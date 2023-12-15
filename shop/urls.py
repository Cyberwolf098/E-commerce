from django.urls import path
from shop.views import index

urlpatterns = [
    path('', index, name='home'),
    # ... d'autres configurations d'URLs peuvent être ajoutées ici
]

 

