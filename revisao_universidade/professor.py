
class Professor:
    def __init__(self, nome, cpf, matricula):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula

    def __str__(self):
        return "{ Professor: " + self.nome + " cpf: " + str(self.cpf) + " matricula: " + str(self.matricula) + " }"

if __name__ == '__main__':

    prof = Professor("prof Erlon", "098766543322f3", "8765")
    print("prof: ", prof)
    print(f"prof: [ {prof} ]")