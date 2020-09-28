from datetime import date, time, datetime

def trabalhando_com_dateTime():
    data_atual = datetime.now()
    print(data_atual)
    print("Data atual: {}".format(data_atual.strftime("%d/%m/%Y")))
    print("Horário atual: {}".format(data_atual.strftime("%H:%M:%S")))
    print(data_atual.strftime("%c"))
    print("Dia: {}".format(data_atual.day))
    diaSemana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo")
    print("Dia atual: {}".format(diaSemana[data_atual.weekday()]))

    data_criada = datetime(2021, 7, 16, 12, 45, 15)
    print(data_criada) # SAIDA: 2021-07-16 12:45:15

    #Convertendo uma string para data
    data_string = "01/01/2018 13:15:02"
    data_convertida = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
    print(data_convertida)

def trabalhando_com_date():

    # EXIBINDO A DATA ATUAL:
    data_atual = date.today()
    print(data_atual)
    #Exibindo a data no padrão brasileiro:
    print(data_atual.strftime("%d/%m/%y"))
    # print(data_atual.strftime("%A/%B/%Y"))

    print(type(data_atual))

    data_atual_str = (data_atual.strftime("%A/%B/%Y"))
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=22, minute=19, second=00)
    print(horario.strftime("%H:%M:%S"))


if __name__ == '__main__':
    trabalhando_com_time()
    trabalhando_com_dateTime()