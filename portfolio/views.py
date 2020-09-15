from django.shortcuts import render
from .models import Project

# Note: Fetching the 'projects' from the database & send them forward into the template.
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})