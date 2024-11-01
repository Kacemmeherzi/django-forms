from django.urls import  path
from MyContact import views


urlpatterns = [
 path('form1/', views.controleform1, name='controleform1'),  
path('form2/', views.controleform2, name='controleform2'),



]