import random
import numpy as np

def gerar_vetor_quase_ordenado(n):
    # Gerar vetor com números no intervalo [0, n^2]
    vetor = [random.randint(0, n**2) for _ in range(n)]
    
    # Ordenar o vetor
    vetor.sort()
    # Embaralhar 10% dos elementos
    num_embaralhar = max(1, n // 10)  # Garantir que pelo menos um elemento seja embaralhado
    indices = random.sample(range(n), num_embaralhar)
    
    # Obter os elementos a serem embaralhados
    elementos_embaralhados = [vetor[i] for i in indices]
    print(f"Elementos antes de embaralhar: {elementos_embaralhados}")
    
    # Embaralhar os elementos selecionados
    np.random.shuffle(elementos_embaralhados)
    print(f"Elementos depois de embaralhar: {elementos_embaralhados}")
    
    # Substituir os elementos originais pelos embaralhados
    for i, idx in enumerate(indices):
        vetor[idx] = elementos_embaralhados[i]
    
    return vetor

# Exemplo de uso
inc = 10
fim = 100
stp = 10

#for n in range(inc, fim + 1, stp):
#    vetor = gerar_vetor_quase_ordenado(n)
#    print(f"Vetor de tamanho {n}: {vetor}")
vetor = gerar_vetor_quase_ordenado(n)
print(f"Vetor de tamanho {inc}: {vetor}")