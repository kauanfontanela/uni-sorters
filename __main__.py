import time
from Sorter import *

# Gera vetor não ordenado com 10 mil elementos para comparação
sample = np.random.randint(0, 10000, 10000)

# Ordena o vetor previamente para teste de precisão
probe_array = np.sort(sample)

# Para cada método de ordenação
for sort_method in (bubble_sort, insertion_sort, merge_sort, quick_sort):
    print(f"Ordenando com o método \033[0;1m{sort_method.__name__}\033[0m...")

    # Cria uma cópia do vetor para não alterar o original
    sorting_array = sample.copy()

    # Registrar o tempo de inicio da ordenação
    start_time = time.time()
    # Ordena o vetor
    sorted_array = sort_method(sorting_array)
    # Calcula o tempo de execução
    elapsed_time = time.time() - start_time

    if sorted_array is not np.ndarray:
        sorted_array = np.array(sorted_array)

    # Verifica se o vetor foi ordenado corretamente
    is_correct = np.array_equal(sorted_array, probe_array)
    print("\033[92;2mO vetor foi ordenado corretamente\033[0m" if is_correct
          else "\033[91;2mO vetor não foi ordenado corretamente\033[0m")

    print(f"{sorted_array}")
    print(f"Tempo de execução: \033[0;4;1m{elapsed_time}s\033[0m\n")
