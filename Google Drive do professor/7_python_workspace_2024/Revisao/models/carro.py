
# from motor import Motor
# from models.motor import Motor
from .motor import Motor

class Carro:
    def __init__(self, cor, marca, modelo, veloc_atual, veloc_max, peso, motor):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.veloc_atual = veloc_atual
        self.veloc_max = veloc_max
        self.peso = peso
        self.motor = motor

    def acelerar(self, veloc):  # incrementando a veloc_atual
        self.veloc_atual += veloc  # self.veloc_atual = self.veloc_atual + veloc

    def desacelerar(self, veloc):
        self.veloc_atual -= veloc

    def pegar_marcha(self):
        if self.veloc_atual >= 0 and self.veloc_atual < 30:
            return 1
        elif self.veloc_atual >= 30 and self.veloc_atual < 60:
            return 2
        elif self.veloc_atual >= 60 and self.veloc_atual < 100:
            return 3
        elif self.veloc_atual >= 100 and self.veloc_atual < 160:
            return 4
        elif self.veloc_atual >= 160 and self.veloc_atual < 230:
            return 5
        else:
            return 6

    def __str__(self):
        return "Carro{" + "cor=" + str(self.cor) + " , marca=" + str(self.marca) + " ,modelo=" + str(
            self.modelo) + " ,veloc_atual=" + str(self.veloc_atual) + " ,veloc_max=" + str(
            self.veloc_max) + " ,peso=" + str(self.peso) + " motor=" + str(self.motor) + '}'



