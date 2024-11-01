from django.urls import  path
from MyContact import views


urlpatterns = [
path('form1/', views.controleform1, name='controleform1'),  
path('form2/', views.controleform2, name='controleform2'),

path('contact/', views.contactView, name='contact'),  # URL for the contact form
path('success/', views.successView, name='success'),  # URL for success page

]