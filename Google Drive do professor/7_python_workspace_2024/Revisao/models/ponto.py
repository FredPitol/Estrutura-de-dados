

import math
class Ponto:


    def __init__(self, initX, initY):
        self.cx = initX
        self.cy = initY

    def getX(self):
        return self.cx

    def getY(self):
        return self.cy

    def distanciaOrigem(self):
        return math.sqrt(self.cx **2 + self.cy**2)

    def pontoMedio(self, ponto):
        ptomedio = Ponto((self.cx + ponto.cx) / 2, (self.cy + ponto.cy) / 2)
        return ptomedio

    def refleteX(self):
        return (Ponto(self.cx, -1 * self.cy))

    def refleteY(self):
        return (Ponto(-1 * self.cx, self.cy))

    def __str__(self):
        return "ponto = (" + str(self.cx) + " , " + str(self.cy) + ")"

if __name__ == '__main__':
    pA = Ponto(3, 4)
    print(pA)
    dist_pA_ate_origem = pA.distanciaOrigem()
    print(f"distancia = {dist_pA_ate_origem}")

    pB = Ponto(3,10)
    print(pB)

    pto_medio = pA.pontoMedio(pB)
    print(f"pto_medio = {pto_medio}")