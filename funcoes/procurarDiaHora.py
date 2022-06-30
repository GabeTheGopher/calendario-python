from time import sleep


def procurarDiaHora(calendario):
    while True:
        mes = int(input('Digite o número do mês (ex: 1): '))
        dia = int(input('Digite o dia: '))
        hora = int(input('Digite o horário exata (ex: 19:00): ').split(':')[0])
        calendario = calendario[mes-1]
        if len(calendario) > 0:
            for c in calendario:
                keys = list(c.keys())
                values = list(c.values())
                horaValue = int(values[1].split(':')[0])
                contador = 0
                if values[0] == dia:
                    if len(keys) == 5:
                        if hora <= horaValue:
                            print(f'\n{keys[1]}: {values[1]}\n{keys[2]}: {values[2]}\n{keys[3]}: {values[3]}\n{keys[4]}: {values[4]}\n')
                            contador+=1
                    elif len(keys) == 4:
                        if hora <= horaValue:
                            print(f'\n{keys[1]}: {values[1]}\n{keys[2]}: {values[2]}\n{keys[3]}: {values[3]}\n')
                            contador+=1
                    if contador == 1:
                        print("Nenhum compromisso encontrado!")
        else:
            print('Nenhum compromisso encontrado!')

        sleep(2)
        break