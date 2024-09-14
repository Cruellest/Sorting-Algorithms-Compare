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

array = [6, 0, 3, 5, 7, 8, 4, 2, 1, 15, 7, 9, 5]
array = counting_sort(array)
print(array)
