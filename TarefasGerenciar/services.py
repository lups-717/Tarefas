from .models import Tarefas

def lista_tarefas_sevices():
    return Tarefas.objects.all().order_by('ordem_apresentacao')

def criar_tarefa_services(nome_tarefa, custo, data_limite, ordem_apresentacao):

    if ordem_apresentacao is None:
        ultima_ordem = Tarefas.objects.order_by('ordem_apresentacao').last()
        ordem_apresentacao =ultima_ordem.ordem_apresentacao+1 if ultima_ordem else 1
    
    tarefas = Tarefas.objects.create(nome_tarefa = nome_tarefa,custo = custo,data_limite = data_limite, ordem_apresentacao = ordem_apresentacao)
    return tarefas


def editar_tarefa_services(nome_tarefa, custo, data_limite, ordem_apresentacao):
    Tarefas.nome_tarefa = nome_tarefa
    Tarefas.custo = custo
    Tarefas.data_limite = data_limite
    Tarefas.ordem_apresentacao = ordem_apresentacao
    Tarefas.save() 
    return Tarefas

def deletar_tarefa_services(tarefas_id):
    tarefas = Tarefas.objects.get(id=tarefas_id)
    tarefas.delete()


"""
def lista_tarefas():
    return Tarefa.objects.all().order_by('ordem_apresentacao')
"""


'''
def criar_tarefa(nome_tarefa, custo, data_limite, ordem_apresentacao):
    
    if ordem_apresentacao is None:
        ultima_ordem = Tarefa.objects.order_by('ordem_apresentacao').last()
        ordem_apresentacao = ultima_ordem.ordem_apresentacao + 1 if ultima_ordem else 1
    
    tarefa = Tarefa.objects.create(
        nome_tarefa=nome_tarefa,
        custo=custo,
        data_limite=data_limite,
        ordem_apresentacao=ordem_apresentacao
    )
    return tarefa
'''