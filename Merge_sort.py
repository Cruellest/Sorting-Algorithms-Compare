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