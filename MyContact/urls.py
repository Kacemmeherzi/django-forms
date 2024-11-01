from django.urls import  path

from MyContact import views


urlpatterns = [
   path('add',views.controleform1, name='add'),


]