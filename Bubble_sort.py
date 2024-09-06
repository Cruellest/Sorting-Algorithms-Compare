
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

array = [6,0,3,5,7,8,4,2,1,15,7,9,5]

bubble_sort(array)

print(array)