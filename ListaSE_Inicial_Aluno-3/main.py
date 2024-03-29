# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



#from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import ListNode
#from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator

from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import *

# ================ Lista de Exercícios sobre TAD Lista Simplesmente Encadeada ============

""""
1) def print_lista(lista):   OK OK OK OK
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

# Printa lista simplesmente encadeada 

def print_ListaSE(lista:SinglyLinkedListIterator ):
    #lista vazia
    if lista.size == 0:
        print("a lista esta vazia")
    else: # lista cheia
        #por iterador sobre o primeiro elemento
        lista.first_Node() # lista.iterator = lista.firstNode
        while lista.iterator: #!lista.isUndefinedIterator()
            print(f'{lista.iterator.data}')
            lista.nextNode() # lista.iterator = lista.iterator.nextNode
            #lista.iterator = lista.iterator.nextNode


def print_ListaSE_Impares(lista:SinglyLinkedListIterator):
    if lista.size == 0:
        
    # inicializar o contador de numeros impares com zero
    #lista vazia
    # if verificar se a lista esta vazia:
    # else:
        # lista esta cheia
        # por o iterator sobre o primeiro noh da lista
        # loop while: enquanto o iterator nao ficar indefinido
            #if numero eh impar
                # imprimo o numero
                # incremento o contador de numeros impares
            #avanco o iterator para o proximo noh
    # retorno o numero de elementos impares
    pass



def maior_impar(lista:SinglyLinkedListIterator ):
    pass

    


def print_lista(lista):
    #verificar se a lista esta vazia ou cheia
    if lista.size == 0:
        print('A lista esta vazia \n')
    else:
        # lista esta cheia
        # por o iterador sobre o primeiro noh da lista
        lista.iterator = lista.firstNode # Ou lista.first_Node()
        #percorrer a lista
        while lista.iterator:
            # printar o atributo data
            print(f' {lista.iterator.data}')
            #avancar o iterador para o proximo noh
            lista.iterator = lista.iterator.nextNode # OU lista.nextNode()



def maior_elemento(lista:SinglyLinkedListIterator):
    # verificar se a lista tem elementos
    # caso a lista tenha elementos fazer:
    # declarar uma variavel: maior
    # atribuir para maior um elemento da sua lista: o primeiro elemento
    # por o iterador sobre o primeiro noh da lista
    # percorrer a lista verificando se o valor armazenado no noh corrente é maior do que o valor
    # armazeando na variavel "maior". Caso seja maior, atualizar a variavel "maior" com
    # o valor corrente do noh.
    # depois avancar o iterador para o proximo no.
    # ao sair do loop retornar o valor armazenado em maior.
    if lista.size == 0:
        print("lista esta vazia")
        return None
    else:
        lista.first_Node() #lista.iterator = lista.firstNode
        maior = lista.iterator.data
        # OU
        # maior = lista.firstNode.data
        #percorrer a lista Loop
        while lista.iterator:
            if lista.iterator.data > maior:
                maior = lista.iterator.data
            #avancar iterator para proximo No
            lista.nextNode() #lista.iterator = lista.iterator.nextNode
        return maior


    # < 1 -> 2 -> 4 -> 5 >
def maior_menor_elemento(lista: SinglyLinkedListIterator):
    if lista.size == 0:
        print("lista esta vazia")
        return None
    else:
        lista.first_Node()  # lista.iterator = lista.firstNode
        maior = menor = lista.iterator.data
        # OU
        # maior = menor = lista.firstNode.data
        # percorrer a lista Loop
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
    # lst1.last_Node()
    lst1.iterator = lst1.lastNode # OU  lst1.last_Node()
    lst1.addNode(data)



def insLista(lst1: SinglyLinkedListIterator, data): # insere um elemento no inicio da lista
    # por o iterador no primeiro noh da lista
    lst1.iterator = lst1.firstNode # OU lst1.first_Node()
    # adcionar o noh antes do iterador
    # e o iterador vai ficar sobre o noh inserido
    lst1.insNode(data)



def concatLista(lst1: SinglyLinkedListIterator, lst2: SinglyLinkedListIterator): # concatenar a lst2 no final da lst1
    # por o iterador da lista 1 no ultimo noh
    lst1.last_Node() # OU lst1.iterator = lst1.lastNode
    # por o iterador da lista 2 no primeiro noh
    lst2.first_Node() # OU lst2.iterator = lst2.firstNode
    # percorrer a lista 2:
    while lst2.iterator:
        # adicionar o elemento da lista 2 na lista 1
        lst1.addNode(lst2.iterator.data)
        # avancar o iterador da lista 2
        lst2.nextNode()
        # OU lst2.iterator = lst2.iterator.nextNode

# verificar se o elemento data esta presente na lista lst.
# se data estiver presente, retornar True,
# caso contrario, False
def esta_na_lista(lst:SinglyLinkedListIterator, data):
    # lista vazia: return False
    # se a lista estiver cheia, percorrer a lista
    # e verificar se elemento do iterador == data
    # se for igual retornar True
    # se for diferente, avançar o iterador p/ proximo node.
    # ao sair do while retornar false
    if lst.size == 0:
        return False
    else:
        lst.first_Node() # OU lst.iterator = lst.firstNode
        while lst.iterator:
            if lst.iterator.data == data:
                return True
            else:
                lst.nextNode()
                # OU lst.iterator = lst.iterator.nextNode
        # se sair do while quer dizer que o elemento
        # nao esta lista: retornar False
        return False


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

    # Criando listas e adicionando seus nos 
    lista1 = SinglyLinkedListIterator()
    lista1.addNode(10)
    lista1.addNode(20)
    lista1.addNode(30)
    lista1.addNode(40)
    lista1.addNode(15)
    lista1.addNode(25)
    lista1.addNode(1)


    print(f'=======Imprimindo Impares da lista1 ==================')
    cont_impar = print_ListaSE_Impares(lista1)
    print(f' quantidade de impares = {cont_impar} ')

    print(f'===================Maior Menor Elemento ================')
    maior, menor = maior_menor_elemento(lista1)
    print(f'maior elemento = {maior}  menor elemento={menor}')

    print(f'=================================================')
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

    print("===== print_listaSE ==========")

    print_ListaSE(lista1)
    print("===== fim da impressao ========")

    print("====== Maior elemento ===========")
    print(f"maior elemento lista 1= {maior_elemento(lista1)}")

    print("===== print_listaSE_IMpares ==========")
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

    # print("================ esta_ordenada ===========")
    # if estaOrdenada(lista1):
    #     print("lista1 esta ordenada")
    # else:
    #     print("lista1 NAO esta ordenada")
    #
    # if estaOrdenada(lista2):
    #     print("lista2 esta ordenada")
    # else:
    #     print("lista2 NAO esta ordenada")
    #
    #
    # print("============ Quinto elemento =============")
    # if verifica_quinto_elemento_igual_elem(lista1, 15):
    #     print("quinto elemento == 15")
    # else:
    #     print("quinto elemento != 15")
    #
    # print_lista(lista1)
    # maior = maior_elemento(lista1)
    # print(f'maior elemento = {maior}')
    #
    # maior, menor = maior_menor_elemento(lista1)
    # print(f'maior = {maior} menor = {menor}')
    #
    # iguais = iguais_listas(lista1, lista2)
    # if iguais:
    #     print("listas sao iguais")
    # else:
    #     print("listas sao difere3ntes")
    #
    #
    #
    #
    #
    #
    # adicionar 300 no final da lista1
    adicionar_final_lista(lista1, 300)
    print_lista(lista1)
    adicionar_final_lista(lista1, 400)
    print_lista(lista1)
    print("\n\n")
    adicionar_final_lista(lista1, 500)
    print_lista(lista1)
    print("\n\n")
    #
    #inserir -100 no inicio da lista1
    insLista(lista1, -100)
    print_lista(lista1)
    print("\n\n")

    print(f"concatenando lista 2 no final da lista 1")
    concatLista(lista1, lista2)
    print(f'concatLista')
    print_lista(lista1)
    print("\n\n")
    #
    print(f'esta na lista : ')
    if(esta_na_lista(lista1, 300)):
        print(f'o elemento {300} esta na lista 1')
    else:
        print(f'o elemento {300} NAO esta na lista 1')

    if (esta_na_lista(lista1, 5000)):
        print(f'o elemento {5000} esta na lista 1')
    else:
        print(f'o elemento {5000} NAO esta na lista 1')

    print("\n\n")
    #
    # if(estaOrdenada(lista2)):
    #     print('lista 2 esta ordenada')
    # else:
    #     print('lsita 2 nao esta ordenada')
    #
    # if (estaOrdenada(lista1)):
    #     print('lista 1 esta ordenada')
    # else:
    #     print('lsita 1 nao esta ordenada')
    #
    #
    #
