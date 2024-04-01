from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import ListNode
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import *

# ================ Lista de Exercícios sobre TAD Lista Simplesmente Encadeada ============

""""
1) def print_Lista(lista):   OK 
2) def maior_elemento(lista): OK
3) def maior_menor_elemento(lista): OK
4) Verificar se duas listas são iguais. def iguais_listas(lst1, lst2): OK 
5) def adicionar_final_lista(lst1, data): OK
6) def insLista(lst1, data): # insere um elemento no inicio da lista OK
7) def concatLista(lst1, lst2): # concatenar a lst2 no final da lst1
8) def esta_na_lista(lst:SinglyLinkedListIterator, data):
9) def estaOrdenada(lst:SinglyLinkedListIterator): # ordem crescente
10) Verificar se uma lista lst2 está contida numa lista lst1. 
    def contidaLista(lst1, lst2):
11) def invLista(lst:SinglyLinkedListIterator): # inverter uma lista lst, destruindo a lista original
"""

def print_Lista_SE(lista:SinglyLinkedListIterator):
    if lista.size == 0:
        print("a lista esta vazia")
    else: 
        lista.first_Node() 
        while lista.iterator: 
            print(f"{lista.iterator.data}")
            lista.nextNode() 

def print_Impares_Conta(lista:SinglyLinkedListIterator):
    contagem = 0
    if lista.size == 0:
        print("Lista vazia")
    else:
        lista.first_Node()
        while lista.iterator:
            if (lista.iterator.data % 2) != 0:
                print(f"Numero impar: {lista.iterator.data}")
                contagem += 1 
            lista.nextNode()
        print(f"Quantidade de numero impares da lista: {contagem}")

def maior_Impar(lista:SinglyLinkedListIterator):
    maior = 0 
    lista.first_Node()
    while lista.iterator:
        if (lista.iterator.data % 2) != 0:
            if lista.iterator.data > maior:
                maior = lista.iterator.data
        lista.nextNode()
    print (f"O maior numero impar da lista: {maior}")

def print_Lista(lista):
    if lista.size == 0:
        print('A lista está vazia \n')
    else:
        lista.iterator = lista.firstNode # Ou lista.first_Node()
        while lista.iterator:
            print(f"{lista.iterator.data}")
            lista.iterator = lista.iterator.nextNode # OU lista.nextNode()

def maior_elemento(lista:SinglyLinkedListIterator):
    if lista.size == 0:
        print("lista esta vazia")
        return None
    else:
        lista.first_Node()
        maior = lista.iterator.data # ou maior = lista.firstNode.data
        # maior = lista.firstNode.data
        while lista.iterator:
            if lista.iterator.data > maior:
                maior = lista.iterator.data
            #avancar iterator para proximo No
            lista.nextNode() #lista.iterator = lista.iterator.nextNode
        return maior


def recebe_Menor_Maior(lista: SinglyLinkedListIterator):
    if lista.size == 0:
        print("Lista vazia\n")
        return None
    else:
        lista.first_Node()
        maior = menor = lista.iterator.data
        while lista.iterator:
            if lista.iterator.data > maior:
                maior = lista.iterator.data
            elif lista.iterator.data < menor:
                menor = lista.iterator.data
            lista.nextNode()
    return menor, maior

def verifica_Listas_Iguais(lista1: SinglyLinkedListIterator, lista2: SinglyLinkedListIterator):
    if lista1.size == 0 and lista2.size == 0:
        print("Ambas as listas estão vazias")
        return True
    elif lista1.size != lista2.size:
        print("As listas são diferentes")
        return False
    else:
        lista1.first_Node()
        lista2.first_Node()
        while lista1.iterator:
            if lista1.iterator.data != lista2.iterator.data:
                return False
            lista1.nextNode()
            lista2.nextNode()
        print("As listas são iguais")
        return True

def adiciona_Elemen_Final(lista: SinglyLinkedListIterator, dado):
    lista.last_Node()
    lista.addNode(dado)
    lista.last_Node()

def adiciona_Elemen_Inicio(lista: SinglyLinkedListIterator, dado): 
    lista.first_Node()
    lista.insNode(dado)
    lista.first_Node()

def concat_Lista(lista1: SinglyLinkedListIterator, lista2: SinglyLinkedListIterator): 
    # concatenar a lst2 no final da lst1
    # por o iterador da lista 1 no ultimo noh
    # por o iterador da lista 2 no primeiro noh
    # percorrer a lista 2:

    print_Lista_SE(lista1)
    print_Lista_SE(lista2)

    while lista2.iterator:
        adiciona_Elemen_Final(lista1, lista2.iterator.data)
        lista2.nextNode()

    


# verificar se o elemento data esta presente na lista lst.
# se data estiver presente, retornar True, caso contrario, False
def esta_na_lista(lst:SinglyLinkedListIterator, data):
    # lista vazia: return False
    pass
    


def estaOrdenada(lst:SinglyLinkedListIterator): # ordem crescente
    # se a lista esta vazia ou com soh um elemento: return True
    pass

def verifica_quinto_elemento_igual_elem(lst:SinglyLinkedListIterator, elem):
    pass
    
def inverte_lista(lst:SinglyLinkedListIterator):
    pass

if __name__ == '__main__':


    #novo_noh = ListNode(5)
    #novo_noh.data = 10
    #lista22 = SinglyLinkedListIterator(novo_noh)

    lista1 = SinglyLinkedListIterator()
    lista1.addNode(10)
    lista1.addNode(20)
    lista1.addNode(30)
    lista1.addNode(40)
    lista1.addNode(15)
    lista1.addNode(25)
    lista1.addNode(1)

    print("\n=== Imprimindo lista1 ===\n")
    print_Lista_SE(lista1)

    print(f'\n=== Imprimindo Impares da lista1 ===\n')
    print_Impares_Conta(lista1)

    print(f'\n=== Imprimindo maior numero impar da lista ===\n')
    maior_Impar(lista1)

    print(f'\n=== Recebendo maior e menor numero como retorno ===\n')
    
    menor, maior = recebe_Menor_Maior(lista1)
    
    print(f"Menor numero da lista: {menor}\nMaior numero da lista: {maior}")

    lista2 = SinglyLinkedListIterator()
    lista2.addNode(10)
    lista2.addNode(20)
    lista2.addNode(30)
    lista2.addNode(40)

    lista3 = SinglyLinkedListIterator()
    lista3.addNode(10)
    lista3.addNode(20)
    lista3.addNode(30)
    lista3.addNode(40)

    print(f'\n=== 4) Verifica se duas listas são iguais ===\n')

    resultado = verifica_Listas_Iguais(lista2, lista3)

    if resultado:
        print("As listas são iguais(Usando retorno booleano)\n")
    else:   
        print("As listas são diferentes(Usando retorno booleano)\n")
    
    resultado = verifica_Listas_Iguais(lista1, lista3)

    if resultado:
        print("As listas são iguais(Usando retorno booleano)\n")
    else:   
        print("As listas são diferentes(Usando retorno booleano)\n")

    print(f'\n=== 5) Adiciona elemento no final da lista deixando iterador nele ===\n') 
    adiciona_Elemen_Final(lista1, 99)
    print_Lista_SE(lista1)
  
    print(f'\n=== 6) Insere elemento no inicio da lista deixando iterador nele ===\n') 
    adiciona_Elemen_Inicio(lista1, 98)
    print_Lista_SE(lista1)

    print(f'\n=== 7) Concatena lista2 no final da lista1 ===\n') 
      
    print(f"Lista 1: {lista1.last_Node()}\n Lista 2{lista2.first_Node()}")
    concat_Lista(lista1, lista2)
    print_Lista_SE(lista1)


    print(f'\n=== 8) Verifica se um dado está na lista ===\n') 
    print(f'\n=== 9) Ordenar lista de forma crescente ===\n') 
    print(f'\n=== 10) Verifica se uma lista está contida em outra ===\n') 
    print(f'\n=== 11) Retorna lista invertida destruindo a lista inicial ===\n') 

    """
    print("====== Maior elemento ===========")
    print(f"maior elemento lista 1= {maior_elemento(lista1)}")

    print("===== print_ListaSE_IMpares ==========")
    #print_ListaSE_Impares(lista1)
    print("===== fim da impressao ========")

    #print("====== maior impar () =====")
    #maior_num_impar = maior_impar(lista1)
    #print(f"maior impar:  {maior_num_impar}")
    #print("====== fim maior impar =====")

    print("=======iguais_lista lista1 e lista2 sao dif ===")
    if iguais_listas(lista1,lista2):
        print("lista 1 e lista 2 sao iguais")
    else:
        print("lista 1 e lista 2 sao diferentes")
    print("fim iguais listas")

    print("=======iguais_lista lista2 e lista3 sao iguais ===")
    if iguais_listas(lista2, lista3):
        print("lista 2 e lista 3 sao iguais")
    else:
        print("lista 2 e lista 3 sao diferentes")
    print("fim iguais listas")

    print(f'\n===  ===\n') 
    """