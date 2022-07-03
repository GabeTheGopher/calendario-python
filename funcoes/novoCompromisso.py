from time import sleep


def novoCompromisso(calendario):
    sleep(0.5)
    mes = -1
    dia = -1
    while True:
        if (mes < 1 or mes > 12):
            mes = int(input('Digite o número do mês (ex: 1): '))

        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            while True:
                if dia < 1 or dia > 31:
                    dia = int(input('Digite o dia: '))
                else:
                    break
            break
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            while True:
                if dia < 1 or dia > 30:
                    dia = int(input('Digite o dia: '))
                else:
                    break
            break
        elif mes == 2:
            while True:
                if dia < 1 or dia > 28:
                    dia = int(input('Digite o dia: '))
                else:
                    break
            break

    compromisso = {
        'Dia': dia,
        'Horario': input('Digite o horário: '),
        'Compromisso': input('Digite um nome para o compromisso: '),
        'Local': input('Digite o Local do compromisso: ')
    }

    while True:
        opcao = input('Deseja adicionar observações (S/N)? ').upper()

        if opcao == 'S':
            compromisso.update({'Observações': input('Observações: ')})
            break
        elif opcao == 'N':
            break

    calendario[mes-1].append(compromisso)

    sleep(0.5)
    return calendario
