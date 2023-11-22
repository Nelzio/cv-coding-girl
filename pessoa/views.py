from django.shortcuts import render
from .models import Pessoa
from .serializers import PessoaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

def utilizadores(request):
    pessoas = Pessoa.objects.all()
    return render(request, "pessoa/index.html", {"pessoas": pessoas})


def utilizador_detalhes(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    return render(request, "pessoa/detalhes.html", {"pessoa": pessoa})


class PessoaView(APIView):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serilizer = PessoaSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)

class PessoaDetalhesView(APIView):
    def get(self, request, pk):
        pessoa = Pessoa.objects.get(pk=pk)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pessoa = Pessoa.objects.get(pk=pk)
        serilizer = PessoaSerializer(pessoa, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors)
    
    def delete(sel, request, pk):
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
