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

array = [6,0,3,5,7,8,4,2,1,15,7,9,5]
heap_sort(array)

print(array)