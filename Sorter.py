import numpy as np


def bubble_sort(array: np.ndarray):
    # Armazena o número de itens no array
    n = len(array)

    # Para cada elemento no array
    for i in range(n - 1):
        # Indicador para avaliar se houve troca de elementos nesta iteração
        swapped = False

        # Para cada elemento no array até o elemento atual
        for j in range(n - i - 1):
            # Se o elemento atual for maior que o próximo
            if array[j] > array[j+1]:
                # Troca os elementos de lugar
                array[j], array[j+1] = array[j+1], array[j]
                # Indica que houve troca de elementos nesta iteração
                swapped = True

        # Se não houve troca de elementos nesta iteração, o array está ordenado
        if not swapped:
            break

    # Retorna o array ordenado
    return array


def insertion_sort(array: np.ndarray):
    # Começando do segundo elemento do array
    for i in range(1, len(array)):
        # O 'key' é o elemento que estamos atualmente tentando posicionar corretamente no array
        key = array[i]
        # 'j' é o índice do elemento anterior ao 'key'
        j = i - 1

        # Enquanto 'j' for maior ou igual a 0 e o 'key' for menor que o elemento em 'j'
        while j >= 0 and key < array[j]:
            # Move o elemento em 'j' uma posição para frente
            array[j+1] = array[j]
            # Decrementa 'j' para continuar a comparação com o próximo elemento
            j -= 1

        # Insere o 'key' na posição correta
        array[j+1] = key

    # Retorna o array ordenado
    return array


def merge_sort(array: np.ndarray):
    # Se o array tiver um ou nenhum elemento, retorna o próprio array
    if len(array) <= 1:
        return array

    # Divide o array em duas partes
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    # Ordena recursivamente as duas partes
    left = merge_sort(left)
    right = merge_sort(right)

    # Junta as duas partes ordenadas
    return __merge(left, right)


def __merge(left: np.ndarray, right: np.ndarray):
    # Cria um array vazio com o tamanho da soma dos tamanhos dos arrays recebidos
    result = np.empty(len(left) + len(right), dtype=left.dtype)
    n_left = n_right = n_result = 0

    # Enquanto houver elementos em ambos os arrays
    while n_left < len(left) and n_right < len(right):
        # Se o elemento em 'left' for menor ou igual ao elemento em 'right'
        if left[n_left] <= right[n_right]:
            # Insere o elemento em 'left' no array de resultado
            result[n_result] = left[n_left]

            # Incrementa o índice de 'left'
            n_left += 1
        else:
            # Insere o elemento em 'right' no array de resultado
            result[n_result] = right[n_right]

            # Incrementa o índice de 'right'
            n_right += 1

        # Incrementa o índice de 'result'
        n_result += 1

    # Enquanto houver elementos em 'left'
    while n_left < len(left):
        # Insere o elemento em 'left' no array de resultado
        result[n_result] = left[n_left]

        # Incrementa o índice de 'left' e 'result'
        n_left += 1
        n_result += 1

    # Enquanto houver elementos em 'right'
    while n_right < len(right):
        # Insere o elemento em 'right' no array de resultado
        result[n_result] = right[n_right]

        # Incrementa o índice de 'right' e 'result'
        n_right += 1
        n_result += 1

    # Retorna o array ordenado
    return result


def quick_sort(array: np.ndarray):
    # Se o array tiver um ou nenhum elemento, retorna o próprio array
    if len(array) <= 1:
        return array

    # Escolhe um elemento do array para ser o pivô (neste caso, o elemento do meio)
    pivot = array[len(array) // 2]

    # Cria três listas: uma para elementos menores que o pivô, uma para elementos iguais ao pivô e uma para elementos maiores
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]

    # Retorna a concatenação do quicksort aplicado à lista dos menores, a lista dos iguais e o quicksort aplicado à lista dos maiores
    return quick_sort(less) + equal + quick_sort(greater)
