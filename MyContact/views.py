from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from MyContact.models import Contact
# Create your views here.
def controleform1 (request):
        if request.method == 'POST':
            f=request.POST['firstname']# firstname c'est name dans page html
            1=request.POST['lastname']
            e=request.POST['email']
            m=request.POST['message' ]
            contact=Contact.objects.create(firstname=f, Lastname=1,Email=e,msg=m) #contact=Contact(firstname=f, lastname=1, Email=e, msg=m)
        #contact.save()
            return HttpResponse(' <h2> Data has been submitted </h2>')

        return render(request, "myform1.html")