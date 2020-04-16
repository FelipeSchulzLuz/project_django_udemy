from django.shortcuts import render
from blog.models import Postagem

# Create your views here.

def home(request):
    postagens = Postagem.objects.all().order_by('-data_criacao')

    return render(request, 'home.html', {'postagens':postagens})
    
