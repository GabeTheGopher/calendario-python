from time import sleep


def numeroCompromissos(calendario):
        while True:
            mes = int(input('Digite o número do mês (ex: 1): '))
            dia = int(input('Digite o dia: '))
            calendario = calendario[mes-1]
            if len(calendario) > 0:
                contador = 0
                for c in calendario:
                    values = list(c.values())
                    if values[0] == dia:
                       contador += 1
                if contador > 0:
                    print(f'{contador} compromissos encontrados!')
                elif contador == 0:
                    print('Nenhum compromisso encontrado!')
            else:
                print('Nenhum compromisso encontrado!')
            sleep(2)           
            break