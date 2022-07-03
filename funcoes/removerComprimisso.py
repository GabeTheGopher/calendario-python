from time import sleep


def removerCompromisso(calendario):
    while True:
        mes = int(input('Digite o número do mês (ex: 1): '))
        dia = int(input('Digite o dia: '))

        if len(calendario) > 0:
            for i in range(len(calendario[mes-1])):
                values = list(calendario[mes-1][i].values())
                if values[0] == dia:
                    while True:
                        opcao = input(
                            f'Deseja remover o compromisso: {values[2]} (S/N)? ').upper()
                        if opcao == 'S':
                            calendario[mes-1].pop(i)
                            print('Compromisso removido com successo!')
                            break
                        elif opcao == 'N':
                            break
        else:
            print('Nenhum compromisso encontrado!')
        sleep(2)
        break
    return calendario
