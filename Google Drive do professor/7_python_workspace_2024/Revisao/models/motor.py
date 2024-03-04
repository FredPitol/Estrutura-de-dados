class Motor:
    def __init__(self, tipo, qtdePistoes, potencia):
        self.tipo = tipo
        self.qtdePistoes = qtdePistoes
        self.potencia = potencia

    def __str__(self):
        return "Motor{" + "tipo=" + str(self.tipo) + ", qtdePistoes=" + str(self.qtdePistoes) + ", potencia=" + str(self.potencia) + '}'



