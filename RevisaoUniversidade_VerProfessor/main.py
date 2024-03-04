# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from professor import Professor
from departamento import Departamento
from universidade import Universidade

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

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
    # uvv.__ativo = 10
    # print("ativo = ", uvv.__ativo)
    # print("PI = ", PI)
    print(uvv)