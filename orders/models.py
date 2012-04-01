from django.db import models
from django.contrib.auth.models import User
     
class UserProfile(models.Model):
    """A Django model representing a user."""
    phone_number = models.CharField(max_length=11) 
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.phone_number

class Order(models.Model):
    """A Django model representing a food order."""
    owner = models.OneToOneField(UserProfile) # The user who started the order.
    # joiners = models.ManyToManyField(UserProfile) # Other users who want in on the order.
