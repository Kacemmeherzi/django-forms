from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=50)  # First name
    lastname = models.CharField(max_length=50)   # Last name
    email = models.EmailField()                    # Email address
    message = models.TextField()                   # Message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the message was created

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"  # String representation of the object