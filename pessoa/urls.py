from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.utilizadores),
    path('<int:pk>/', view=views.utilizador_detalhes),
    path('pessoas/', view=views.PessoaView.as_view()),
    path('pessoas/<int:pk>/', view=views.PessoaDetalhesView.as_view()),
]
