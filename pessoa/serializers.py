from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pessoa
        fields = '__all__'