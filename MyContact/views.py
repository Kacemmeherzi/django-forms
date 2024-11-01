from django.shortcuts import render , redirect 
from django.core.mail import send_mail ,BadHeaderError
# Create your views here.


from django.http import HttpResponse

from MyContact.models import Contact
from .forms import contactform2 , ContactForm
# Create your views here.
def controleform1(request):
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        e = request.POST['email']
        m = request.POST['message']
       
        # Create the Contact object
        contact = Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
        #contact=Contact(firstname=f,lastname=l,Email=e,msg=m)

        # contact.save()  # This line is not necessary since create() already saves it

        return HttpResponse('<h2> Data has been submitted </h2>')

    return render(request, "myform1.html")


def controleform2(request):
    if request.method == 'POST':  # Check if the form is submitted via POST
        form = contactform2(request.POST)  # Populate the form with POST data
        if form.is_valid():  # Validate the form data
           
            # Process the form data
            f = contactform2.cleaned_data['firstname']
            l = contactform2.cleaned_data['lastname']
            e = contactform2.cleaned_data['email']
            m = contactform2.cleaned_data['msg']
           
            # Save the data to the database using the Contact model
            Contact.objects.create(firstname=f, lastname=l, email=e, message=m)

            # Return a success message
            return HttpResponse('<h2>Data has been submitted successfully</h2>')
    else:  # If it's not a POST request, create a blank form
        form = contactform2()
        
    # Render the template with the form context
    return render(request, "myform2.html", {'mycontactform2': form})


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email_list = []
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            to_email = form.cleaned_data['to_email']
            email_list.append(to_email)

            try:
                send_mail(subject, message, from_email, email_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')