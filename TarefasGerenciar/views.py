import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarefas
from .services import lista_tarefas_sevices, editar_tarefa_services, criar_tarefa_services, deletar_tarefa_services

def criar_tarefa_view(request):

    if request.method == "POST":
        nome_tarefa = request.POST.get('nome_tarefa'),
        custo = request.POST.get('custo')
        data_limite = request.POST.get('data_limite')
        ultima_ordem = Tarefas.objects.order_by('ordem_apresentacao').last()
        ordem_apresentacao = ultima_ordem.ordem_apresentacao + 1 if ultima_ordem else 1
        criar_tarefa_services(nome_tarefa, custo, data_limite,ordem_apresentacao)
        return redirect('listar_tarefa')  
    return render(request, 'criar.html')



def editar_tarefa_view(request, tarefa_id):

    tarefas = get_object_or_404(Tarefas,id=tarefa_id)

    if request.method == "POST":
        nome_tarefa = request.POST.get('nome_tarefa')
        custo = request.POST.get('custo')
        data_limite = request.POST.get('data_limite')

        editar_tarefa_services(tarefa_id, nome_tarefa, custo, data_limite)

        return redirect('listar_tarefas')

    return render(request, 'editar.html', {'tarefa': tarefas})

def listar_tarefa_view(request):
    tarefas = lista_tarefas_sevices()
    return render(request, 'tarefas.html', {'tarefas': tarefas})

def salvar_ordem_tarefas_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ordem_ids = data.get('ordem', [])  

            Tarefas.objects.all().update(ordem_apresentacao=None)

            for posicao, tarefa_id in enumerate(ordem_ids, start=1):
                tarefa = Tarefas.objects.get(id=tarefa_id)
                tarefa.ordem_apresentacao = posicao  # Atribui a nova ordem
                tarefa.save()

            return JsonResponse({'status': 'success', 'message': 'Ordem salva com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método inválido.'}, status=405)

def delete_tarefa_view(request,tarefa_id):
    # if request.method == "POST":
    #     tarefas = deletar_tarefa_services()
    #     return render(request, 'delete.html', {'tarefas': tarefas})
    if request.method == "POST":
        deletar_tarefa_services(tarefa_id)
        return redirect('listar_tarefa')
    
    tarefa = Tarefas.objects.get(id=tarefa_id)  
    return render(request, 'deletar.html', {'tarefa': tarefa})

