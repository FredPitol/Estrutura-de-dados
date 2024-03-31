from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import ListNode
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import *

# ================ Lista de Exercícios sobre TAD Lista Simplesmente Encadeada ============

""""
1) def print_Lista(lista):   OK OK OK OK
2) def maior_elemento(lista): OK
3) def maior_menor_elemento(lista): OK
4) Verificar se duas listas são iguais. 
Duas listas são iguais se ambas as estruturas têm o mesmo 
número de elementos, e estes são iguais um a um. 
Em particular, duas listas vazias são iguais. 
def iguais_listas(lst1, lst2): OK 
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

def maior_menor_elemento(lista: SinglyLinkedListIterator):
    if lista.size == 0:
        print("lista esta vazia")
        return None
    else:
        lista.first_Node()
        maior = menor = lista.iterator.data
        while lista.iterator:
            if lista.iterator.data > maior:
                maior = lista.iterator.data
            elif lista.iterator.data < menor:
                menor = lista.iterator.data
            # avancar iterator para proximo No
            lista.nextNode()  # lista.iterator = lista.iterator.nextNode
        return maior, menor


def iguais_listas(lst1: SinglyLinkedListIterator, lst2: SinglyLinkedListIterator):
    if lst1.size == 0 and lst2.size == 0:
        return True
    elif lst1.size != lst2.size:
        return False
    else:
        lst1.first_Node() #lst1.iterator = lst1.firstNode
        lst2.first_Node() #lst2.iterator = lst2.firstNode
        while lst1.iterator: # ou lst2.iterator
            if lst1.iterator.data != lst2.iterator.data:
                return False
            lst1.nextNode() #lst1.iterator = lst1.iterator.nextNode
            lst2.nextNode() #lst2.iterator = lst2.iterator.nextNode
        return True




def adicionar_final_lista(lst1: SinglyLinkedListIterator, data):
    # por o iterador no ultimo noh da lista

    # adcionar o noh depois do iterador
    # e o iterador vai ficar sobre o noh adicionado
    pass



def insLista(lst1: SinglyLinkedListIterator, data): # insere um elemento no inicio da lista
    # por o iterador no primeiro noh da lista

    # adcionar o noh antes do iterador
    # e o iterador vai ficar sobre o noh inserido
    pass



def concatLista(lst1: SinglyLinkedListIterator, lst2: SinglyLinkedListIterator): # concatenar a lst2 no final da lst1
    # por o iterador da lista 1 no ultimo noh

    # por o iterador da lista 2 no primeiro noh

    # percorrer a lista 2:
    while lst2.iterator:
        pass
    

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

    

    print(f'\n=== Imprimir maior e menor elemento ===\n')

    maior, menor = maior_menor_elemento(lista1)
    print(f'maior elemento = {maior}  menor elemento={menor}')

    print(f'\n===  ===\n') 
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

    print("===== print_ListaSE ==========")


    print("===== fim da impressao ========")

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

   