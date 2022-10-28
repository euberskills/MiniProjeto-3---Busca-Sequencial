#busca.py

def buscaSequencial(lista, pavavraChave):
    pos = 0
    encontrou = False
    parar = False
    tamanhodalista = len(lista)
    while pos < tamanhodalista and not encontrou and not parar:
        if lista[pos] == pavavraChave:
            encontrou = True
        else:
            if lista[pos] > pavavraChave:
                parar = True
            else:
                pos = pos+1
    return encontrou



def buscaBinaria(lista, pavavraChave):
    inicio = 0
    fim = len(lista)-1
    encontrou = False
    while inicio<=fim and not encontrou:
        meio = (inicio + fim)//2
        if lista[meio] == pavavraChave:
            encontrou = True
        else:
            if pavavraChave < lista[meio]:
                fim = meio-1
            else:
                inicio = meio+1
    return encontrou
#projeto.py

import timeit
import random

from busca import *

def printar():
    print("-------------------------")

def teste_desempenho_otimizado():
    if len(lista) < 128:
        buscaSequencial(lista, valor())
    else:
        buscaBinaria(lista, valor())


def teste_do_desempenho_sequencial():
    buscaSequencial(lista, valor())


def teste_do_desempenho_binario():
    buscaBinaria(lista, valor())


def valor():
    return random.randint(0, tamanho*2)
  

try:
    printar()
    tamanho = int(input("Digite o tamanho da lista: "))
    printar()
    quantidadeDeTestes = int(input("Digite quantas vezes deseja fazer o teste: "))
    printar()
    lista = list(range(tamanho))

    print()
    tempo_sequencial = timeit.timeit(stmt=teste_do_desempenho_sequencial, number=quantidadeDeTestes)
    print(f"Desempenho sequencial: {tempo_sequencial}, tempo médio de testes: {tempo_sequencial/quantidadeDeTestes}\n")

    tempo_binario = timeit.timeit(stmt=teste_do_desempenho_binario, number=quantidadeDeTestes)
    print(f"Desempenho binario: {tempo_binario}, tempo médio de testes: {tempo_binario/quantidadeDeTestes}\n")

    tempo_oti = timeit.timeit(stmt=teste_desempenho_otimizado, number=quantidadeDeTestes)
    print(f"Desempenho otimizado: {tempo_oti}, tempo médio de testes: {tempo_oti/quantidadeDeTestes}\n")


except:
    print("Os valores de tamanho e quantidade de teste devem ser inteiros positivos.")

    print("---------------------------------------------------------------------------------------------------------------------------------")
