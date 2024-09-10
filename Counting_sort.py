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


array = [6,0,3,5,7,8,4,2,1,15,7,9,5]

array = counting_sort(array)

print(array)