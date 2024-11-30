from django.urls import path
from .views import editar_tarefa_view, criar_tarefa_view, delete_tarefa_view,listar_tarefa_view,salvar_ordem_tarefas_view

urlpatterns = [
    path('salvar_ordem/', salvar_ordem_tarefas_view, name='salvar_ordem'),
    path('', listar_tarefa_view, name='listar_tarefa'),
    path('criar/',criar_tarefa_view, name='criar_tarefa'),
    path('editar/<int:tarefa_id>/', editar_tarefa_view, name= 'editar_tarefa'),
    path('deletar/<int:tarefa_id>/',delete_tarefa_view, name = 'deletar_tarefa')
]

