from django.shortcuts import render
from app.models import UserProfile

def index(request):
    userprofiles = UserProfile.objects.all()
    return render(request, 'index.html', {'userprofiles': userprofiles})
