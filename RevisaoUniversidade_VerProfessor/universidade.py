
from professor import Professor
from departamento import Departamento


PI = 3.14

class Universidade:


    def __init__(self, nome, endereco, cnpj, vet_depto=[]):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.lista_depto = vet_depto
        #self.__ativo="sim"

    def __str__(self):
        strdepto = ""
        for depto in self.lista_depto:
            strdepto += f" depto: {str(depto)} \n"

        return "Universidade " + str(self.nome) + " end = " + str(self.endereco) + " cnpj = " + str(self.cnpj) + "\n" + strdepto

if __name__ == '__main__':
        prof1 = Professor("Pedro", "43438743434", "mat7777")
        prof2 = Professor("Ana", "2323232323232", "mat8888")

        vet_prof = []
        vet_prof.append(prof1)
        vet_prof.append(prof2)

        prof3 = Professor("Arthur", "323432323232", "mat9999")
        prof4 = Professor("Igor", "43434343434", "mat22212")

        vet_prof2 = []
        vet_prof2.append(prof3)
        vet_prof2.append(prof4)

        dept_mat = Departamento("Matematica", "MAT", 3, vet_prof)
        dept_fis = Departamento("Fisica", "FIS", 3, vet_prof2)
        print(dept_mat)



        vet_depto = []
        vet_depto.append(dept_fis)
        vet_depto.append(dept_mat)

        uvv = Universidade("uvv", "rua...", "43434343434", vet_depto)
        #uvv.__ativo = 10
        #print("ativo = ", uvv.__ativo)
        #print("PI = ", PI)
        print(uvv)