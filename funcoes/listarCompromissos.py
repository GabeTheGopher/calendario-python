from time import sleep


def listarCompromissos(calendario):
    while True:
        opcao = input('Deseja listar por dia (D) ou mês (M)? ').upper()
        if opcao == 'D':
            mes = int(input('Digite o número do mês (ex: 1): '))
            dia = int(input('Digite o dia: '))
            calendario = calendario[mes-1]
            if len(calendario) > 0:
                for c in calendario:
                    keys = list(c.keys())
                    values = list(c.values())

                    if values[0] == dia:
                        if len(keys) == 5:
                            print(f'\n{keys[1]}: {values[1]}\n{keys[2]}: {values[2]}\n{keys[3]}: {values[3]}\n{keys[4]}: {values[4]}\n')
                        else:
                            print(f'\n{keys[1]}: {values[1]}\n{keys[2]}: {values[2]}\n{keys[3]}: {values[3]}\n')
                    else:
                        print("Nenhum compromisso encontrado!")
            else:
                print('Nenhum compromisso encontrado')
            sleep(2)           
            break
        if opcao == 'M':
            mes = int(input('Digite o número do mês (ex: 1): '))
            calendario = calendario[mes-1]
            if len(calendario) > 0:
                for c in calendario:
                    keys = list(c.keys())
                    values = list(c.values())
                    if len(keys) == 5:
                        print(f'\n{keys[1]}: {values[1]}\n{keys[2]}: {values[2]}\n{keys[3]}: {values[3]}\n{keys[4]}: {values[4]}\n')
                    else:
                        print(f'\n{keys[1]}: {values[1]}\n{keys[2]}: {values[2]}\n{keys[3]}: {values[3]}\n')
            else:
                print('Nenhum compromisso encontrado!')
    
            sleep(2)
            break