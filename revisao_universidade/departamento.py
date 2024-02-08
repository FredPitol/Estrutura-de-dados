
from professor import Professor
class Departamento:

    def __init__(self, nome, codigo, max_prof=5, vet_prof=[]):
        self.nome = nome
        self.codigo = codigo
        if len(vet_prof) > max_prof:
            print(f"Só é possivel adicionar {max_prof} professores a um departamento")
        else:      
            self.vet_prof = vet_prof

    def __str__(self):
        str_prof = ""
        #for prof in self.???????
            # completar
        return "Departamento = { " + self.nome + " , codigo: " + self.codigo + "\n" + str_prof + "\n }"

if __name__=='__main__':

    medicina = Departamento("Departamento")

    #instanciar 3 professores e exibir seus atributos

    #criar uma lista de professores

    #adicionar os professores na lista

    #instanciar um Departamento

    # exibir todos os atributos do objeto