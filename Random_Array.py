import math
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy
import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        # Meio do array
        mid = len(arr) // 2
        
        # Divisão
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursivamente ordenando (conquista)
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        # Merge
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Check elementos esquerda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Check elementos direita
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def counting_sort(array):
    maior = max(array);
    counting = [0] * (maior + 1)
    output = [0] * len(array)
    
    for i in range(len(array)):
        counting[array[i]] += 1
        
    for i in range(1,maior + 1):
        counting[i] += counting[i-1]
        
    for j in range(len(array)):
        output[counting[array[j]]-1] = array[j]
        
    return output

def construir_maxheap(arr, n, i):
    # Encontrar maior dentre a raiz
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    # Troca e chama recursivamente se a raiz não for a maior
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        construir_maxheap(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # construir max heap
    for i in range(n // 2 - 1, -1, -1):
        construir_maxheap(arr, n, i)

    # Extrair elemntos da heap
    for i in range(n-1, 0, -1):
        # Mover raiz para o final
        arr[i], arr[0] = arr[0], arr[i]
        # Construir heap no array reduzido
        construir_maxheap(arr, i, 0)
        
def insertion_sort(array):
    size = len(array)
    ordenado = [array[0]]
    
    for i in range(1, size):
        chave = array[i]
        inserted = False
        
        for j in range(len(ordenado)):
            
            if(chave < ordenado[j]):
                ordenado.insert(j,chave)
                inserted = True
                break
        
        if not inserted:
            ordenado.append(chave)
    
    return ordenado  

def bubble_sort(array):
    size = len(array)
    
    for j in range(size):
        swapped = False
        
        for i in range(size - j - 1):
            
            if(array[i] > array[i+1]):
                swap = array[i]
                array[i] = array[i+1]
                array[i+1] = swap
                swapped = True
                
        if (swapped == False):
            break

#Main
numpy.random.seed(2208)
random.seed(2208)


#Salvar dados
n_valores = []
alg1 = []
alg2 = []

#Algoritmo

n= 0    #Valor Inicial
while n < 20000: #Quantidade Total de Medias

    tempo_alg1 = []
    tempo_alg2 = []

    for i in range(10): #Quantidade de Testes Por Algoritmo
        
        array = numpy.random.randint(0,random.randint(0,(n*2000)**2),n)
        array2 = array.copy()
        
        tempo_inicio_alg1 = time.perf_counter()
        merge_sort(array)
        tempo_fim_alg1 = time.perf_counter()
        tempo_alg1.append(tempo_fim_alg1 - tempo_inicio_alg1)
        
        tempo_inicio_alg2 = time.perf_counter()
        quick_sort(array2)
        tempo_fim_alg2 = time.perf_counter()
        tempo_alg2.append(tempo_fim_alg2 - tempo_inicio_alg2)
        
    media_alg1 = sum(tempo_alg1)/len(tempo_alg1)
    media_alg2 = sum(tempo_alg2)/len(tempo_alg2)

    n_valores.append(n)
    alg1.append(media_alg1)
    alg2.append(media_alg2)
    print(f"{n_valores[len(n_valores)-1]}\tMédia Alg 1: {media_alg1:.5f}\tMédia Alg 2: {media_alg2:.5f}")
    
    #Step
    n = n+2000
    
    
#DataFrame do panda (Alterar nomes para fim de apresentação)
df = pd.DataFrame({
    'n' : n_valores,
    'Merge Sort' : alg1,
    'Quick Sort': alg2
})
    
#Linhas do seaborn
sns.lineplot(data=df,x='n',y='Merge Sort',label='Merge Sort')
sns.lineplot(data=df,x='n',y='Quick Sort',label='Quick Sort') 
    

#Print Plot
plt.xticks(n_valores)

plt.title("Algs comparison")
plt.xlabel('n')
plt.ylabel('valor')

plt.show()