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
        """
        Retorna pessoas da base de dados
        """
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(
            pessoas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)