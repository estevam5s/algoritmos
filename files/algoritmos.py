import time
import random

def inserir_inicio(lista, valor):
    """Inserção no início - O(n)"""
    lista.insert(0, valor)

def busca_linear(lista, valor):
    """Busca linear - O(n)"""
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return -1

def busca_binaria(lista, valor, inicio=0, fim=None):
    """Busca binária recursiva - O(log n)"""
    if fim is None:
        fim = len(lista) - 1
    
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == valor:
        return meio
    elif lista[meio] > valor:
        return busca_binaria(lista, valor, inicio, meio - 1)
    else:
        return busca_binaria(lista, valor, meio + 1, fim)

def fibonacci_recursivo(n):
    """Fibonacci recursivo ingênuo - O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_iterativo(n):
    """Fibonacci iterativo - O(n)"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def factorial(n):
    """Factorial recursivo - O(n)"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def permutacoes(lista):
    """Gerar todas permutações - O(n!)"""
    if len(lista) <= 1:
        return [lista]
    
    resultado = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]
        for p in permutacoes(resto):
            resultado.append([lista[i]] + p)
    
    return resultado

def multiplicar_matrizes(A, B):
    """Multiplicação de matrizes - O(n³)"""
    n = len(A)
    resultado = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado

def medir_tempo(func, *args):
    """Função auxiliar para medir tempo de execução"""
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

def main():
    print("=== Análise de Complexidade - Python ===\n")
    
    # Array inicial para testes
    lista = [50, 10, 40, 20, 30, 15, 25, 35, 45, 5]
    print(f"Lista inicial: {lista}")
    
    # 1. Acesso direto - O(1)
    print("\n1. Acesso direto - O(1):")
    print(f"Elemento no índice 3: {lista[3]}")
    
    # 2. Inserção no início - O(n)
    print("\n2. Inserção no início - O(n):")
    lista_copia = lista.copy()
    inserir_inicio(lista_copia, 1)
    print(f"Após inserir 1 no início: {lista_copia}")
    
    # 3. Busca linear - O(n)
    print("\n3. Busca linear - O(n):")
    posicao = busca_linear(lista, 40)
    if posicao != -1:
        print(f"Valor 40 encontrado na posição: {posicao}")
    else:
        print("Valor 40 não encontrado")
    
    # 4. Ordenação - O(n log n)
    print("\n4. Ordenação - O(n log n):")
    lista_ordenada = sorted(lista)
    print(f"Lista ordenada: {lista_ordenada}")
    
    # 5. Busca binária - O(log n)
    print("\n5. Busca binária - O(log n):")
    posicao_bin = busca_binaria(lista_ordenada, 40)
    print(f"Busca binária - valor 40 na posição: {posicao_bin}")
    
    # 6. Fibonacci - comparação O(2^n) vs O(n)
    print("\n6. Fibonacci - O(2^n) vs O(n):")
    n_fib = 30
    
    # Fibonacci recursivo (cuidado - muito lento!)
    print(f"Calculando fibonacci({n_fib}) recursivo (pode demorar...):")
    resultado_rec, tempo_rec = medir_tempo(fibonacci_recursivo, n_fib)
    print(f"Resultado: {resultado_rec}, Tempo: {tempo_rec:.6f}s")
    
    # Fibonacci iterativo
    resultado_iter, tempo_iter = medir_tempo(fibonacci_iterativo, n_fib)
    print(f"Fibonacci iterativo: {resultado_iter}, Tempo: {tempo_iter:.6f}s")
    print(f"Speedup: {tempo_rec/tempo_iter:.0f}x mais rápido!")
    
    # 7. Factorial - O(n)
    print("\n7. Factorial - O(n):")
    n_fact = 10
    resultado_fact = factorial(n_fact)
    print(f"Factorial de {n_fact}: {resultado_fact}")
    
    # 8. Permutações - O(n!)
    print("\n8. Permutações - O(n!):")
    lista_pequena = [1, 2, 3, 4]
    perms = permutacoes(lista_pequena)
    print(f"Permutações de {lista_pequena}: {len(perms)} combinações")
    print("Primeiras 6 permutações:", perms[:6])
    
    # 9. Multiplicação de matrizes - O(n³)
    print("\n9. Multiplicação de matrizes - O(n³):")
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    resultado_matriz, tempo_matriz = medir_tempo(multiplicar_matrizes, A, B)
    print("Matriz A × B =")
    for linha in resultado_matriz:
        print(linha)
    print(f"Tempo: {tempo_matriz:.6f}s")
    
    # Teste de performance com dados maiores
    print("\n=== Teste de Performance ===")
    N = 10000
    lista_grande = [random.randint(1, 1000) for _ in range(N)]
    
    # Busca linear
    _, tempo_busca = medir_tempo(busca_linear, lista_grande, 500)
    print(f"Busca linear em {N} elementos: {tempo_busca:.6f}s")
    
    # Ordenação
    _, tempo_ordenacao = medir_tempo(sorted, lista_grande)
    print(f"Ordenação de {N} elementos: {tempo_ordenacao:.6f}s")
    
    print("\n=== Resumo das Complexidades ===")
    print("O(1)      - Acesso direto: lista[i]")
    print("O(log n)  - Busca binária")
    print("O(n)      - Busca linear, fibonacci iterativo, factorial")
    print("O(n log n)- Ordenação (sorted)")
    print("O(n²)     - Percorrer matriz")
    print("O(n³)     - Multiplicação de matrizes")
    print("O(2^n)    - Fibonacci recursivo")
    print("O(n!)     - Todas permutações")

if __name__ == "__main__":
    main()
