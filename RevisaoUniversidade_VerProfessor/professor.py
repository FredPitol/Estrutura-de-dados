class Professor:

    def __init__(self, nome, cpf, matricula):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula

    def __str__(self):
        return "{ Professor " + self.nome + " cpf = " + self.cpf + " matricula = " + self.matricula + " }"


if __name__ == '__main__':
    prof = Professor("prof. Erlon", " 897.098.678-00", "9876")
    print(prof)