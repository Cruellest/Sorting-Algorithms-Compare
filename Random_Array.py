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