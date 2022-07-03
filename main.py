from time import sleep
from funcoes.novoCompromisso import novoCompromisso
from funcoes.listarCompromissos import listarCompromissos
from funcoes.procurarDiaHora import procurarDiaHora
from funcoes.numeroCompromissos import numeroCompromissos
from funcoes.gravarAgenda import gravarAgenda
from funcoes.removerComprimisso import removerCompromisso

calendario = [[],[],[],[],[],[],[],[],[],[],[],[]]

while True:
    opcoes = int(input(("""
    Digite a sua opção
    1 - Novo Compromisso
    2 - Listagem de compromisso
    3 - Procurar por dia e hora
    4 - Número de compromissos
    5 - Gravar agenda
    6 - Remoção de compromissos
    7 - Sair do Programa
    """)))

    if opcoes == 1:
        calendario = novoCompromisso(calendario)

    if opcoes == 2:
        listarCompromissos(calendario)
    
    if opcoes == 3:
        procurarDiaHora(calendario)
    
    if opcoes == 4:
        numeroCompromissos(calendario)
    
    if opcoes == 5:
        gravarAgenda(calendario)

    if opcoes == 6:
        calendario = removerCompromisso(calendario)

    if opcoes == 7:
        print('Tenha um bom dia :)')
        sleep(1)
        break