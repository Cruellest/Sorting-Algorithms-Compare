import math
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

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


#Salvar dados
n_valores = []
alg1 = []
alg2 = []

#Algoritmo
n= 2 
while n < 100:

    n_valores.append(n)
    alg1.append(100*n**2)
    alg2.append(2**n)
    print(f"{n}\t{alg1[n-2]}\t{alg2[n-2]}")
    n = n+1
    
    
#DataFrame do panda (Alterar nomes para fim de apresentação)
df = pd.DataFrame({
    'n' : n_valores,
    '100n^2' : alg1,
    '2^n': alg2
})
    
#Linhas do seaborn
sns.lineplot(data=df,x='n',y='100n^2',label='100n^2')
sns.lineplot(data=df,x='n',y='2^n',label='2^n') 
    

#Print Plot
plt.title("Algs comparison")
plt.xlabel('n')
plt.ylabel('valor')

plt.show()