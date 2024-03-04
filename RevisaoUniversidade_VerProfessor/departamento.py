
from professor import Professor

class Departamento:
    def __init__(self, nome, codigo, max_prof=5, vet_prof=[]):
        self.nome = nome
        self.codigo = codigo
        self.lista_prof = vet_prof
        self.max_prof = max_prof

    def add_prof(self, prof):
        if len(self.lista_prof) < self.max_prof:
            self.lista_prof.append(prof)
        else:
            print("a lista de professores ja tem " + str(self.max_prof) +" professores\n")

    def __str__(self):
        strprof = ""
        strprof = "\n".join(map(str, self.lista_prof))
        #for prof in self.lista_prof:
            #strprof += f" nome: {getattr(prof, 'nome')}  cpf: {getattr(prof, 'cpf')} \n"
            #strprof += f" nome: {prof.nome}  cpf: {getattr(prof, 'cpf')} \n"

        return "Departamento = { " + str(self.nome) + " , " + str(self.codigo) + "\n" + strprof + " }"


if __name__=='__main__':


    prof1 = Professor("Pedro","43438743434", "mat7777")
    prof2 = Professor("Ana", "2323232323232", "mat8888")

    vet_prof = []
    vet_prof.append(prof1)
    vet_prof.append(prof2)

    dept_mat = Departamento("Matematica", "MAT", 3, vet_prof)7
    print(dept_mat)

    prof3 = Professor("Arthur", "323432323232", "mat9999")
    prof4 = Professor("Igor", "43434343434", "mat22212")

    dept_mat.add_prof(prof3)
    dept_mat.add_prof(prof4)