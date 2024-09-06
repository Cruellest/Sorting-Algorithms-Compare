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
    
              
array = [6,0,3,5,7,8,4,2,1,15,7,9,5]

array = insertion_sort(array)

print(array)