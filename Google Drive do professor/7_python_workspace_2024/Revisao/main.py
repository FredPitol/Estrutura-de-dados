# from models.user import User
from models.motor import Motor
from models.carro import Carro
from models.ponto import Ponto
from copy import copy


def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    #max_num = 1
    for num in nums:
        if (num > max_num):
            max_num = num
    return max_num

if __name__ == "__main__":

    vet=[1,2,3,4,5]
    max = find_max(vet)
    print(max)
    max_num = float("-inf")  # smaller than all other numbers
    print(max_num)

    pA = Ponto(3,4)
    print(pA)

    motor_turbo = Motor("12 valvulas", 12, 400)
    motor_turbo.potencia = 500
    carro = Carro("vermelho", "BMW", "X5", 0, 300, 2000, motor_turbo)
    print(motor_turbo)
    print(carro)
    carro.acelerar(100)
    print(carro.veloc_atual)

    # vetor de Motores
    vet_motor = []
    vet_motor.append(Motor("8 valvulas", 8, 300))
    vet_motor.append(Motor("6 valvulas", 6, 200))

    print("enderecos \n")
    print(id(vet_motor[0])) #endereco de memoria
    print(f"endereco inteiro do Motor 0: {id(vet_motor[0])}")
    print(f'endereco hexadecimal do Motor 0: {hex(id(vet_motor[0]))}')
    print(f'Atibutos do Motor 0: {vet_motor[0]}')

    #fazendo uma copia de um objeto: os objetos apontam para posicoes diferentes de memoria
    motor_copia = copy(vet_motor[0])
    print(f'endereco do Motor copia: {id(motor_copia)}')
    print(f'Atibutos do Motor copia: {motor_copia}')


    i = 0
    for item in vet_motor:  # "item in vet" e' um iterador, item comeca em vet[0], depois vet[1] e assim por diante
        print(vet_motor[i]);
        i += 1;
        # print(); # quebre a linha

    # outra forma de loop
    print()
    for item in vet_motor:
        print(f'{item}\n')




