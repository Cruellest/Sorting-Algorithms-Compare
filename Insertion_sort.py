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
    
              
array = [6,0,3,5,7,8,4,2,1,15,7,9,5]

insertion_sort(array)

print(array)