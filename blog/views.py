from django.shortcuts import render
from blog.models import Flower

# Create your views here.
def index(request):
    flower=Flower.objects.all()
    return render(request, 'base.html', {'flower':flower})