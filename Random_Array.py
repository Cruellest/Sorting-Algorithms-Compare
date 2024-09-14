import math
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy
import random
import time
import sys

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
    maior = max(array)
    counting = [0] * (maior + 1)
    output = [0] * len(array)
    
    # Contando as ocorrências de cada elemento
    for i in range(len(array)):
        counting[array[i]] += 1
    
    # Atualizando o array counting para armazenar as posições acumuladas
    for i in range(1, maior + 1):
        counting[i] += counting[i - 1]
    
    # Construindo o array de saída
    for j in range(len(array) - 1, -1, -1):  # Percorre de trás para frente para garantir estabilidade
        output[counting[array[j]] - 1] = array[j]
        counting[array[j]] -= 1  # Decrementa após a inserção
        
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
    
    # Loop sobre todos os elementos a partir do segundo
    for i in range(1, size):
        chave = array[i]
        j = i - 1
        
        # Mover os elementos de array[0..i-1] que são maiores que a chave
        # para uma posição à frente de sua posição atual
        while j >= 0 and chave < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        # Insere a chave na posição correta
        array[j + 1] = chave
    
    return array
    

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

#Tamanho inicial do vetor de entrada
inc = int(sys.argv[1])

#Tamanho final do vetor de entrada
fim = int(sys.argv[2])

#Intervalo entre os tamanhos
stp = int(sys.argv[3])

#Quantidade de testes no random
rtp = int(sys.argv[4])

#Salvar dados
n_valores = []
bubble_sortVec = []
insertion_sortVec = []
merge_sortVec = []
heap_sortVec = []
quick_sortVec = []
counting_sortVec = []

#Algoritmo

n = inc    #Valor Inicial

print(f"[[RANDOM]]")
print(f"{'n':8}\tBubble\t\tInsertion\tMerge\t\tHeap\t\tQuick\t\tCounting")
print("------------------------------------------------------------------------------------------------------------")

while n < fim+1: #Quantidade Total de Medias

    #Random
    tempo_bubble = []
    tempo_insertion = []
    tempo_merge = []
    tempo_heap = []
    tempo_quick = []
    tempo_counting = []

    for i in range(rtp): #Quantidade de Testes Por Algoritmo
        
        array = numpy.random.randint(0,random.randint(0,n**2),n)
        array2 = array.copy()
        array3 = array.copy()
        array4 = array.copy()
        array5 = array.copy()
        array6 = array.copy()
        
        tempo_inicio_bubble = time.perf_counter()
        bubble_sort(array)
        tempo_fim_bubble = time.perf_counter()
        tempo_bubble.append(tempo_fim_bubble - tempo_inicio_bubble)
        
        tempo_inicio_insertion = time.perf_counter()
        insertion_sort(array2)
        tempo_fim_insertion = time.perf_counter()
        tempo_insertion.append(tempo_fim_insertion - tempo_inicio_insertion)
        
        tempo_inicio_merge = time.perf_counter()
        merge_sort(array3)
        tempo_fim_merge = time.perf_counter()
        tempo_merge.append(tempo_fim_merge - tempo_inicio_merge)
        
        tempo_inicio_heap = time.perf_counter()
        heap_sort(array4)
        tempo_fim_heap = time.perf_counter()
        tempo_heap.append(tempo_fim_heap - tempo_inicio_heap)
        
        tempo_inicio_quick = time.perf_counter()
        quick_sort(array5)
        tempo_fim_quick = time.perf_counter()
        tempo_quick.append(tempo_fim_quick - tempo_inicio_quick)
        
        tempo_inicio_counting = time.perf_counter()
        array6 = counting_sort(array6)
        tempo_fim_counting = time.perf_counter()
        tempo_counting.append(tempo_fim_counting - tempo_inicio_counting)
        
        
    media_bubble = sum(tempo_bubble)/len(tempo_bubble)
    media_insertion = sum(tempo_insertion)/len(tempo_insertion)
    media_merge = sum(tempo_merge)/len(tempo_merge)
    media_heap = sum(tempo_heap)/len(tempo_heap)
    media_quick = sum(tempo_quick)/len(tempo_quick)
    media_counting = sum(tempo_counting)/len(tempo_counting)
    

    n_valores.append(n)
    bubble_sortVec.append(media_bubble)
    insertion_sortVec.append(media_insertion)
    merge_sortVec.append(media_merge)
    heap_sortVec.append(media_heap)
    quick_sortVec.append(media_quick)
    counting_sortVec.append(media_counting)
    
    print(f"{n_valores[len(n_valores)-1]:8}\t{media_bubble:.6f}\t{media_insertion:.6f}\t{media_merge:.6f}\t{media_heap:.6f}\t{media_quick:.6f}\t{media_counting:.6f}")
    
    #print(f"{n_valores[len(n_valores)-1]}\tMédia Bubble 1: {media_bubble:.5f}\t\tMédia Insertion 2: {media_insertion:.5f}\t\t Média Merge 3: {media_merge:.5f}\t\t Média Heap 4 :{media_heap:.5f}\t\t Média Quick 5 :{media_quick:.5f}\t\t Média Counting 6 :{media_counting:.5f}")
    
    #Step
    n = n+stp
    
#DataFrame do panda (Alterar nomes para fim de apresentação)
df = pd.DataFrame({
    'n' : n_valores,
    'Bubble Sort' : bubble_sortVec,
    'Insertion Sort': insertion_sortVec,
    'Merge Sort' : merge_sortVec,
    'Heap Sort' : heap_sortVec,
    'Quick Sort' : quick_sortVec,
    'Counting Sort' : counting_sortVec
})
    
#Linhas do seaborn
sns.lineplot(data=df,x='n',y='Bubble Sort',label='Bubble Sort')
sns.lineplot(data=df,x='n',y='Insertion Sort',label='Insertion Sort') 
sns.lineplot(data=df,x='n',y='Merge Sort',label='Merge Sort') 
sns.lineplot(data=df,x='n',y='Heap Sort',label='Heap Sort')
sns.lineplot(data=df,x='n',y='Quick Sort',label='Quick Sort')
sns.lineplot(data=df,x='n',y='Counting Sort',label='Counting Sort')
    

#Print Plot
plt.xticks(n_valores)

plt.title("Random Array")
plt.xlabel('n')
plt.ylabel('valor')

plt.show()



#Invertido
print(f"\n\n[[REVERSE]]")
print(f"{'n':8}\tBubble\t\tInsertion\tMerge\t\tHeap\t\tQuick\t\tCounting")
print("------------------------------------------------------------------------------------------------------------")

n = inc

n_valores.clear()
bubble_sortVec.clear()
insertion_sortVec.clear()
merge_sortVec.clear()
heap_sortVec.clear()
quick_sortVec.clear()
counting_sortVec.clear()

while n < fim+1:
    array = list(range(n,-1, -1))
    array2 = array.copy()
    array3 = array.copy()
    array4 = array.copy()
    array5 = array.copy()
    array6 = array.copy()

    tempo_inicio_bubble = time.perf_counter()
    bubble_sort(array)
    tempo_fim_bubble = time.perf_counter()
    tempo_bubble = (tempo_fim_bubble - tempo_inicio_bubble)
    
    tempo_inicio_insertion = time.perf_counter()
    insertion_sort(array2)
    tempo_fim_insertion = time.perf_counter()
    tempo_insertion = (tempo_fim_insertion - tempo_inicio_insertion)
        
    tempo_inicio_merge = time.perf_counter()
    merge_sort(array3)
    tempo_fim_merge = time.perf_counter()
    tempo_merge = (tempo_fim_merge - tempo_inicio_merge)
        
    tempo_inicio_heap = time.perf_counter()
    heap_sort(array4)
    tempo_fim_heap = time.perf_counter()
    tempo_heap = (tempo_fim_heap - tempo_inicio_heap)
        
    tempo_inicio_quick = time.perf_counter()
    quick_sort(array5)
    tempo_fim_quick = time.perf_counter()
    tempo_quick = (tempo_fim_quick - tempo_inicio_quick)
        
    tempo_inicio_counting = time.perf_counter()
    array6 = counting_sort(array6)
    tempo_fim_counting = time.perf_counter()
    tempo_counting = (tempo_fim_counting - tempo_inicio_counting)

    n_valores.append(n)
    bubble_sortVec.append(tempo_bubble)
    insertion_sortVec.append(tempo_insertion)
    merge_sortVec.append(tempo_merge)
    heap_sortVec.append(tempo_heap)
    quick_sortVec.append(tempo_quick)
    counting_sortVec.append(tempo_counting)
    
    print(f"{n_valores[len(n_valores)-1]:8}\t{tempo_bubble:.6f}\t{tempo_insertion:.6f}\t{tempo_merge:.6f}\t{tempo_heap:.6f}\t{tempo_quick:.6f}\t{tempo_counting:.6f}")

    n += stp

# print(len(n_valores) ,len(bubble_sortVec), len(insertion_sortVec),len(merge_sortVec),len(heap_sortVec),len(quick_sortVec),len(counting_sortVec))
    

df = pd.DataFrame({
    'n' : n_valores,
    'Bubble Sort' : bubble_sortVec,
    'Insertion Sort': insertion_sortVec,
    'Merge Sort' : merge_sortVec,
    'Heap Sort' : heap_sortVec,
    'Quick Sort' : quick_sortVec,
    'Counting Sort' : counting_sortVec
})


sns.lineplot(data=df,x='n',y='Bubble Sort',label='Bubble Sort')
sns.lineplot(data=df,x='n',y='Insertion Sort',label='Insertion Sort') 
sns.lineplot(data=df,x='n',y='Merge Sort',label='Merge Sort') 
sns.lineplot(data=df,x='n',y='Heap Sort',label='Heap Sort')
sns.lineplot(data=df,x='n',y='Quick Sort',label='Quick Sort')
sns.lineplot(data=df,x='n',y='Counting Sort',label='Counting Sort')
    

#Print Plot
plt.xticks(n_valores)

plt.title("Reverse Array")
plt.xlabel('n')
plt.ylabel('valor')

plt.show()



#Ordenado
print(f"\n\n[[SORTED]]")
print(f"{'n':8}\tBubble\t\tInsertion\tMerge\t\tHeap\t\tQuick\t\tCounting")
print("------------------------------------------------------------------------------------------------------------")


n = inc

n_valores.clear()
bubble_sortVec.clear()
insertion_sortVec.clear()
merge_sortVec.clear()
heap_sortVec.clear()
quick_sortVec.clear()
counting_sortVec.clear()

while n < fim+1:
    array = list(range(n+1))
    array2 = array.copy()
    array3 = array.copy()
    array4 = array.copy()
    array5 = array.copy()
    array6 = array.copy()

    tempo_inicio_bubble = time.perf_counter()
    bubble_sort(array)
    tempo_fim_bubble = time.perf_counter()
    tempo_bubble = (tempo_fim_bubble - tempo_inicio_bubble)
    
    tempo_inicio_insertion = time.perf_counter()
    insertion_sort(array2)
    tempo_fim_insertion = time.perf_counter()
    tempo_insertion = (tempo_fim_insertion - tempo_inicio_insertion)
        
    tempo_inicio_merge = time.perf_counter()
    merge_sort(array3)
    tempo_fim_merge = time.perf_counter()
    tempo_merge = (tempo_fim_merge - tempo_inicio_merge)
        
    tempo_inicio_heap = time.perf_counter()
    heap_sort(array4)
    tempo_fim_heap = time.perf_counter()
    tempo_heap = (tempo_fim_heap - tempo_inicio_heap)
        
    tempo_inicio_quick = time.perf_counter()
    quick_sort(array5)
    tempo_fim_quick = time.perf_counter()
    tempo_quick = (tempo_fim_quick - tempo_inicio_quick)
        
    tempo_inicio_counting = time.perf_counter()
    array6 = counting_sort(array6)
    tempo_fim_counting = time.perf_counter()
    tempo_counting = (tempo_fim_counting - tempo_inicio_counting)

    n_valores.append(n)
    bubble_sortVec.append(tempo_bubble)
    insertion_sortVec.append(tempo_insertion)
    merge_sortVec.append(tempo_merge)
    heap_sortVec.append(tempo_heap)
    quick_sortVec.append(tempo_quick)
    counting_sortVec.append(tempo_counting)
    
    print(f"{n_valores[len(n_valores)-1]:8}\t{tempo_bubble:.6f}\t{tempo_insertion:.6f}\t{tempo_merge:.6f}\t{tempo_heap:.6f}\t{tempo_quick:.6f}\t{tempo_counting:.6f}")

    n += stp

#print(len(n_valores) ,len(bubble_sortVec), len(insertion_sortVec),len(merge_sortVec),len(heap_sortVec),len(quick_sortVec),len(counting_sortVec))
    

df = pd.DataFrame({
    'n' : n_valores,
    'Bubble Sort' : bubble_sortVec,
    'Insertion Sort': insertion_sortVec,
    'Merge Sort' : merge_sortVec,
    'Heap Sort' : heap_sortVec,
    'Quick Sort' : quick_sortVec,
    'Counting Sort' : counting_sortVec
})


sns.lineplot(data=df,x='n',y='Bubble Sort',label='Bubble Sort')
sns.lineplot(data=df,x='n',y='Insertion Sort',label='Insertion Sort') 
sns.lineplot(data=df,x='n',y='Merge Sort',label='Merge Sort') 
sns.lineplot(data=df,x='n',y='Heap Sort',label='Heap Sort')
sns.lineplot(data=df,x='n',y='Quick Sort',label='Quick Sort')
sns.lineplot(data=df,x='n',y='Counting Sort',label='Counting Sort')
    

#Print Plot
plt.xticks(n_valores)

plt.title("Sorted Array")
plt.xlabel('n')
plt.ylabel('valor')

plt.show()