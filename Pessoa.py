class Pessoa():
    def __init__(self, nome):
        self.__nome = nome

    def andar(self):
        print(f"{self.__nome} está andando.")
