def gravarAgenda(calendario):
    nome = input('digite o nome da agenda: ')
    agenda = open(nome, "w+")
    embelezador = '=-' * 20

    contador = 0
    for mes in calendario:
        for compromisso in mes:
            contador += 1
            agenda.write(f"{contador}º compromisso\n")
            agenda.write(f"""Compromisso no dia: {compromisso['Dia']}
Horário: {compromisso['Horario']}
Compromisso: {compromisso['Compromisso']}
Local: {compromisso['Local']}\n""")
            if len(compromisso) == 5:
                agenda.write(f"Observações: {compromisso['Observações']}\n")
            agenda.write(f'{embelezador} \n')
    agenda.close()
