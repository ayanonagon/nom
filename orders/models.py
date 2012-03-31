from django.db import models
from django.contrib.auth.models import User
     
class UserProfile(models.Model):
    """A Django model representing a user."""
    phone_number = models.CharField(max_length=11) 
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
        return self.phone_number
