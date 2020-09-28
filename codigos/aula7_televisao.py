class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 4

    def power(self):
        if self.ligada:  # Se estiver ligada execute o codigo abaixo
            self.ligada = False  # Desligue
        else:
            self.ligada = True  # Senão ligue a televisão.

    def aumenta_canal(self):
        if self.ligada: # Se a tv estiver ligada aumente o canal
            self.canal += 1
        else:
            print("Operação invalida a tv está desligada!")

    def diminuicanal(self):
        if self.ligada:  # Se a tv estiver ligada diminua o canal
            self.canal -= 1
        else:
            print("Operação invalida a tv está desligada!")

if __name__ == '__main__':  # Só execute esse trecho se for chaado pelo proprio arquivo. Se for importado por outra classe essa parte não será exibida
    tv = Televisao()
    print("Televisão está ligada?: {}".format(tv.ligada))  # False
    tv.power()  # false
    print("Televisão está ligada?: {}".format(tv.ligada))  #True

    print("A tv esa ligada em que canal ?: {}".format(tv.canal))  # canal 4
    tv.aumenta_canal()  # canal 5
    print("Aumentando para o canal: {}".format(tv.canal))  # canal já valendo 5

    tv.power() # ligando tv

    print("Televisão está ligada?: {}".format(tv.ligada))
    tv.diminuicanal()
    print("Diminuindo o canal: {}".format(tv.canal)) # canal 4
    tv.diminuicanal()
    print("Diminuindo o canal: {}".format(tv.canal)) # canal 3

    tv.aumenta_canal()
    print("Aumentando o Canal: {}".format(tv.canal)) # canal 4
