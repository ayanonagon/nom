from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True) 

    class Meta:
        model = User
        fields = ("username", "first_name", "phone_number", "password1", "password2")
 
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        if commit:
            user.save()
        profile = UserProfile(user=user, first_name=user.first_name, phone_number = self.cleaned_data["phone_number"])
        if commit:
            profile.save()
        return profile
