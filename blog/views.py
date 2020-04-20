from django.shortcuts import render
from blog.models import Postagem

# Create your views here.


def home(request):
    postagens = Postagem.objects.all().order_by("-data_criacao")
    return render(request, 'home.html', {'postagens': postagens})


def detalhe_post(request, pk):
    postagem = Postagem.objects.get(pk=pk)
    return render(request, 'detalhe_postagem.html', {'postagem': postagem})




