from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from orders.models import UserProfile

class RegistrationForm(UserCreationForm):
   
    first_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "phone_number", "password1", "password2")
 
    def save(self, new_data):
        u = User.objects.create_user(new_data['username'],
                                     new_data['first_name'],
                                     new_data['password1'])
        u.is_active = True
        u.save()
        profile = UserProfile(user=u, first_name=u.first_name, phone_number=new_data['phone_number'])
        return u, profile
