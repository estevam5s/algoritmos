import time  # O(1) - importação de módulo
import random  # O(1) - importação de módulo

def inserir_inicio(lista, valor):
    """Inserção no início - O(n)"""
    lista.insert(0, valor)  # O(n) - desloca todos os elementos
# COMPLEXIDADE FINAL: O(n) - termo dominante é o deslocamento de elementos

def busca_linear(lista, valor):
    """Busca linear - O(n)"""
    for i, elemento in enumerate(lista):  # O(n) - percorre lista até encontrar
        if elemento == valor:  # O(1) - comparação
            return i  # O(1) - retorno
    return -1  # O(1) - retorno quando não encontra
# COMPLEXIDADE FINAL: O(n) - pior caso percorre toda a lista, O(1) desconsiderado

def busca_binaria(lista, valor, inicio=0, fim=None):
    """Busca binária recursiva - O(log n)"""
    if fim is None:  # O(1) - verificação condicional
        fim = len(lista) - 1  # O(1) - operação aritmética

    if inicio > fim:  # O(1) - comparação
        return -1  # O(1) - retorno base

    meio = (inicio + fim) // 2  # O(1) - cálculo do meio

    if lista[meio] == valor:  # O(1) - acesso e comparação
        return meio  # O(1) - retorno
    elif lista[meio] > valor:  # O(1) - comparação
        return busca_binaria(lista, valor, inicio, meio - 1)  # O(log n) - recursão
    else:
        return busca_binaria(lista, valor, meio + 1, fim)  # O(log n) - recursão
# COMPLEXIDADE FINAL: O(log n) - divide espaço de busca pela metade a cada chamada

def fibonacci_recursivo(n):
    """Fibonacci recursivo ingênuo - O(2^n)"""
    if n <= 1:  # O(1) - caso base
        return n  # O(1) - retorno
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)  # O(2^n) - duas chamadas recursivas
# COMPLEXIDADE FINAL: O(2^n) - cada chamada gera 2 novas chamadas, criando árvore exponencial

def fibonacci_iterativo(n):
    """Fibonacci iterativo - O(n)"""
    if n <= 1:  # O(1) - caso base
        return n  # O(1) - retorno

    a, b = 0, 1  # O(1) - inicialização
    for _ in range(2, n + 1):  # O(n) - loop de 2 até n
        a, b = b, a + b  # O(1) - operações aritméticas

    return b  # O(1) - retorno
# COMPLEXIDADE FINAL: O(n) - loop executa n-2 vezes, operações O(1) desconsideradas

def factorial(n):
    """Factorial recursivo - O(n)"""
    if n <= 1:  # O(1) - caso base
        return 1  # O(1) - retorno
    return n * factorial(n - 1)  # O(n) - uma chamada recursiva por nível
# COMPLEXIDADE FINAL: O(n) - faz n chamadas recursivas em sequência

def permutacoes(lista):
    """Gerar todas permutações - O(n!)"""
    if len(lista) <= 1:  # O(1) - caso base
        return [lista]  # O(1) - retorno

    resultado = []  # O(1) - inicialização
    for i in range(len(lista)):  # O(n) - para cada elemento
        resto = lista[:i] + lista[i+1:]  # O(n) - criação de sublista
        for p in permutacoes(resto):  # O((n-1)!) - recursão para sublista
            resultado.append([lista[i]] + p)  # O(n) - concatenação de listas

    return resultado  # O(1) - retorno
# COMPLEXIDADE FINAL: O(n!) - para cada elemento gera (n-1)! permutações recursivamente

def multiplicar_matrizes(A, B):
    """Multiplicação de matrizes - O(n³)"""
    n = len(A)  # O(1) - obter tamanho
    resultado = [[0] * n for _ in range(n)]  # O(n²) - criar matriz n×n

    for i in range(n):  # O(n) - primeiro loop
        for j in range(n):  # O(n) - segundo loop
            for k in range(n):  # O(n) - terceiro loop aninhado
                resultado[i][j] += A[i][k] * B[k][j]  # O(1) - operação aritmética

    return resultado  # O(1) - retorno
# COMPLEXIDADE FINAL: O(n³) - três loops aninhados dominam, O(n²) e O(1) desconsiderados

def medir_tempo(func, *args):
    """Função auxiliar para medir tempo de execução"""
    inicio = time.time()  # O(1) - captura tempo inicial
    resultado = func(*args)  # O(f(n)) - executa função com complexidade f(n)
    fim = time.time()  # O(1) - captura tempo final
    return resultado, fim - inicio  # O(1) - retorno de tupla
# COMPLEXIDADE FINAL: O(f(n)) - dominada pela função passada como parâmetro

def main():
    print("=== Análise de Complexidade - Python ===\n")  # O(1) - I/O

    # Array inicial para testes
    lista = [50, 10, 40, 20, 30, 15, 25, 35, 45, 5]  # O(1) - inicialização
    print(f"Lista inicial: {lista}")  # O(1) - I/O

    # 1. Acesso direto - O(1)
    print("\n1. Acesso direto - O(1):")  # O(1) - I/O
    print(f"Elemento no índice 3: {lista[3]}")  # O(1) - acesso + I/O

    # 2. Inserção no início - O(n)
    print("\n2. Inserção no início - O(n):")  # O(1) - I/O
    lista_copia = lista.copy()  # O(n) - cópia de lista
    inserir_inicio(lista_copia, 1)  # O(n) - inserção
    print(f"Após inserir 1 no início: {lista_copia}")  # O(1) - I/O
    
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

"""
=== ANÁLISE COMPLETA DE COMPLEXIDADE BIG O ===

1. CONSTANTE - O(1):
   - Acesso direto a array/lista: lista[i]
   - Operações aritméticas básicas: +, -, *, /, %
   - Comparações simples: ==, <, >, <=, >=
   - Atribuições de variáveis
   - Retornos de função

2. LOGARÍTMICA - O(log n):
   - Busca binária: divide o espaço de busca pela metade a cada iteração
   - Árvores balanceadas (busca, inserção, remoção)
   - Algoritmos "divide e conquista" que reduzem o problema pela metade

3. LINEAR - O(n):
   - Busca linear: percorre todo o array no pior caso
   - Fibonacci iterativo: executa n-2 iterações
   - Factorial recursivo: faz n chamadas recursivas
   - Percorrer array/lista uma vez

4. LINEARÍTMICA - O(n log n):
   - Algoritmos de ordenação eficientes: quicksort, mergesort, heapsort
   - Operação sorted() do Python
   - Algoritmos "divide e conquista" que processam todos os elementos

5. QUADRÁTICA - O(n²):
   - Loops aninhados duplos
   - Algoritmos de ordenação ingênuos: bubble sort, selection sort
   - Criação de matriz n×n

6. CÚBICA - O(n³):
   - Três loops aninhados (como multiplicação de matrizes)
   - Algoritmos que operam em estruturas tridimensionais

7. EXPONENCIAL - O(2^n):
   - Fibonacci recursivo ingênuo: cada chamada gera duas novas chamadas
   - Problemas de força bruta que testam todas as combinações
   - Algoritmos que geram conjuntos potência

8. FATORIAL - O(n!):
   - Geração de todas as permutações
   - Problema do caixeiro viajante (força bruta)
   - Algoritmos que testam todas as ordenações possíveis

ORDEM DE CRESCIMENTO (do melhor para o pior):
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2^n) < O(n!)

EXEMPLOS PRÁTICOS COM n=10:
- O(1): 1 operação
- O(log n): ~3 operações
- O(n): 10 operações
- O(n log n): ~33 operações
- O(n²): 100 operações
- O(n³): 1.000 operações
- O(2^n): 1.024 operações
- O(n!): 3.628.800 operações

=== COMO DETERMINAR A COMPLEXIDADE FINAL DE UMA FUNÇÃO ===

REGRA FUNDAMENTAL: Na análise Big O, consideramos apenas o TERMO DE MAIOR CRESCIMENTO
e desconsideramos constantes e termos de menor ordem.

EXEMPLOS PRÁTICOS:

1. FUNÇÃO COM MÚLTIPLAS OPERAÇÕES:
   def exemplo1(lista):
       x = lista[0]           # O(1)
       for i in lista:        # O(n)
           print(i)           # O(1)
       for i in lista:        # O(n)
           for j in lista:    # O(n)
               print(i, j)    # O(1)

   ANÁLISE: O(1) + O(n) + O(n²) = O(n²)
   RESULTADO: O(n²) - termo quadrático domina

2. FUNÇÃO COM OPERAÇÕES SEQUENCIAIS:
   def exemplo2(lista):
       lista.sort()           # O(n log n)
       busca_linear(lista, x) # O(n)
       print(lista[0])        # O(1)

   ANÁLISE: O(n log n) + O(n) + O(1) = O(n log n)
   RESULTADO: O(n log n) - termo linearítmico domina

3. FUNÇÃO COM LOOPS ANINHADOS:
   def exemplo3(n):
       for i in range(n):     # O(n)
           for j in range(n): # O(n)
               for k in range(n): # O(n)
                   operacao() # O(1)

   ANÁLISE: O(n) × O(n) × O(n) × O(1) = O(n³)
   RESULTADO: O(n³) - três loops multiplicam complexidades

4. FUNÇÃO RECURSIVA:
   def fibonacci_recursivo(n):
       if n <= 1: return n    # O(1)
       return fib(n-1) + fib(n-2)  # T(n) = T(n-1) + T(n-2) + O(1)

   ANÁLISE: Árvore binária de altura n
   RESULTADO: O(2^n) - crescimento exponencial

REGRAS PARA ANÁLISE:
1. Loops sequenciais: SOMAR as complexidades
2. Loops aninhados: MULTIPLICAR as complexidades
3. Recursão: Resolver relação de recorrência
4. Condicionais: Considerar o PIOR CASO
5. Termo dominante: Manter apenas o de MAIOR CRESCIMENTO

ORDEM DE DOMINÂNCIA:
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2^n) < O(n!)

EXEMPLOS DE SIMPLIFICAÇÃO:
- 3n² + 2n + 1 → O(n²)
- 5n log n + 10n → O(n log n)
- 2^n + n³ + 1000 → O(2^n)
- n! + 2^n + n³ → O(n!)
"""
