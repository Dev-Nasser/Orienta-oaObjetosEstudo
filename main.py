class Carro:

    def __init__ (self, modelo, cidade, cor, potencia, combustivel=False, motorista=False):
        self.modelo = modelo
        self.cidade = cidade
        self.cor = cor
        self.potencia = potencia
        self.combustivel = combustivel
        self.motorista = motorista

    def retornamodelo(self):
        return print ("O modelo do seu carro é {}".format(self.modelo))

    def retornacidade(self):
        return print("A cidade do seu veiculo é {} ".format(self.cidade))

    def abastecer(self):
            self.combustivel = True
            return print("Carro Abastecido")

    def desligarcarro(self):
        if self.combustivel == True:
            print("O seu carro ainda está ligado, desligue-o")
        else:
            print ("O seu carro está desligado")
            self.motorista = False

    def pilotar(self):
        if self.motorista == True:
            print ("O motorista está no carro")
        else:
            print ("O Motorista deve entrar no carro")


carro = Carro
carro1 = carro("celta", "Londrina", "verde", "1.6V")
carro1.retornacidade()
carro1.retornamodelo()
carro1.abastecer()
carro1.desligarcarro()
carro1.pilotar()
