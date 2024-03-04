from professor import Professor
class Departamento:

    def __init__(self, nome, codigo, max_prof=5, vet_prof=[]):
        self.n = nome
        self.c = codigo
        if len(vet_prof) > 5:
            print(f"Só é possivel adicionar {max_prof} professores a um departamento")
        else:      
            self.vet_prof = vet_prof


    def __str__(self):
        str_prof = ""
        return "Departamento = { " + self.nome + " , codigo: " + self.codigo + "\n" + str_prof + "\n }"

# Teste unitário
    
if __name__=='__main__':


    prof1 = Professor("Frederico","1212121212121","3434343434")
    print(f"Dados do professor : Nome {prof1.nome}")
    medicina = Departamento("Departamento","83918",["Max","Carlos", "José"])

    #instanciar 3 professores e exibir seus atributos

    #criar uma lista de professores

    #adicionar os professores na lista

    #instanciar um Departamento

    # exibir todos os atributos do objeto