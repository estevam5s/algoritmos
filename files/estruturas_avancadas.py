import time
import random
import sys
sys.setrecursionlimit(10000)

class No:
    """Classe para simular ponteiros em Python"""
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    """Lista ligada simples"""
    def __init__(self):
        self.head = None
    
    def inserir_inicio(self, valor):
        """Inserção no início - O(1)"""
        novo = No(valor)
        novo.proximo = self.head
        self.head = novo
    
    def percorrer(self):
        """Percorrer toda lista - O(n)"""
        elementos = []
        atual = self.head
        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo
        return elementos
    
    def buscar(self, valor):
        """Buscar elemento - O(n)"""
        atual = self.head
        posicao = 0
        
        while atual is not None:
            if atual.valor == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        
        return -1

def busca_binaria_iterativa(lista, valor):
    """Busca binária iterativa - O(log n)"""
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return -1

def busca_binaria_recursiva(lista, valor, inicio=0, fim=None):
    """Busca binária recursiva - O(log n)"""
    if fim is None:
        fim = len(lista) - 1
    
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == valor:
        return meio
    elif lista[meio] > valor:
        return busca_binaria_recursiva(lista, valor, inicio, meio - 1)
    else:
        return busca_binaria_recursiva(lista, valor, meio + 1, fim)

def fibonacci_com_memoizacao(n, memo={}):
    """Fibonacci com memoização - O(n)"""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_com_memoizacao(n-1, memo) + fibonacci_com_memoizacao(n-2, memo)
    return memo[n]

def torre_hanoi(n, origem='A', destino='C', auxiliar='B'):
    """Torre de Hanói - O(2^n)"""
    movimentos = []
    
    def mover(n, origem, destino, auxiliar):
        if n == 1:
            movimentos.append(f"Mover disco 1 de {origem} para {destino}")
            return
        
        mover(n-1, origem, auxiliar, destino)
        movimentos.append(f"Mover disco {n} de {origem} para {destino}")
        mover(n-1, auxiliar, destino, origem)
    
    mover(n, origem, destino, auxiliar)
    return movimentos

def bubble_sort(lista):
    """Bubble Sort - O(n²)"""
    n = len(lista)
    lista_copia = lista.copy()
    comparacoes = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia, comparacoes

def merge_sort(lista):
    """Merge Sort - O(n log n)"""
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    """Função auxiliar para merge sort"""
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

def percorrer_matriz(matriz):
    """Percorrer matriz - O(n²)"""
    linhas = len(matriz)
    colunas = len(matriz[0])
    elementos = []
    
    for i in range(linhas):
        for j in range(colunas):
            elementos.append(matriz[i][j])
    
    return elementos

def multiplicar_matrizes_otimizada(A, B):
    """Multiplicação de matrizes com verificação - O(n³)"""
    if len(A[0]) != len(B):
        raise ValueError("Dimensões incompatíveis para multiplicação")
    
    linhas_A = len(A)
    colunas_A = len(A[0])
    colunas_B = len(B[0])
    
    resultado = [[0] * colunas_B for _ in range(linhas_A)]
    
    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado

def gerar_subconjuntos(conjunto):
    """Gerar todos subconjuntos - O(2^n)"""
    if not conjunto:
        return [[]]
    
    primeiro = conjunto[0]
    resto = conjunto[1:]
    
    subconjuntos_resto = gerar_subconjuntos(resto)
    
    novos_subconjuntos = []
    for subconjunto in subconjuntos_resto:
        novos_subconjuntos.append([primeiro] + subconjunto)
    
    return subconjuntos_resto + novos_subconjuntos

def análise_performance():
    """Análise comparativa de performance"""
    print("=== ANÁLISE DE PERFORMANCE ===")
    print("Comparando algoritmos com diferentes complexidades:\n")
    
    tamanhos = [100, 1000, 5000]
    
    for n in tamanhos:
        print(f"Testando com n = {n}")
        print("-" * 30)
        
        # Gerar dados de teste
        dados_desordenados = [random.randint(1, 1000) for _ in range(n)]
        dados_ordenados = sorted(dados_desordenados)
        valor_busca = dados_ordenados[n//2]  # Buscar um valor no meio
        
        # Busca linear - O(n)
        inicio = time.time()
        pos_linear = dados_ordenados.index(valor_busca)
        tempo_linear = time.time() - inicio
        
        # Busca binária - O(log n)
        inicio = time.time()
        pos_binaria = busca_binaria_iterativa(dados_ordenados, valor_busca)
        tempo_binaria = time.time() - inicio
        
        # Ordenação Python (Timsort) - O(n log n)
        inicio = time.time()
        dados_ordenados_python = sorted(dados_desordenados)
        tempo_sort_python = time.time() - inicio
        
        # Merge Sort - O(n log n)
        inicio = time.time()
        dados_merge_sort = merge_sort(dados_desordenados.copy())
        tempo_merge_sort = time.time() - inicio
        
        print(f"Busca linear:     {tempo_linear:.8f}s")
        print(f"Busca binária:    {tempo_binaria:.8f}s")
        print(f"Sort Python:      {tempo_sort_python:.6f}s")
        print(f"Merge Sort:       {tempo_merge_sort:.6f}s")
        
        if tempo_binaria > 0:
            print(f"Speedup busca:    {tempo_linear/tempo_binaria:.1f}x")
        
        print()

def demonstrar_complexidades():
    """Demonstração das diferentes complexidades"""
    print("=== DEMONSTRAÇÃO DE COMPLEXIDADES ===\n")
    
    # 1. Lista Ligada
    print("1. LISTA LIGADA")
    print("================")
    
    lista = ListaLigada()
    lista.inserir_inicio(30)
    lista.inserir_inicio(20)
    lista.inserir_inicio(10)
    
    print(f"Lista: {lista.percorrer()}")
    print(f"Busca por 20: posição {lista.buscar(20)}")
    print()
    
    # 2. Busca Binária
    print("2. BUSCA BINÁRIA")
    print("================")
    
    array_ordenado = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    valor = 15
    
    print(f"Array: {array_ordenado}")
    
    pos_iter = busca_binaria_iterativa(array_ordenado, valor)
    pos_rec = busca_binaria_recursiva(array_ordenado, valor)
    
    print(f"Busca binária iterativa por {valor}: posição {pos_iter}")
    print(f"Busca binária recursiva por {valor}: posição {pos_rec}")
    print()
    
    # 3. Fibonacci com diferentes abordagens
    print("3. FIBONACCI - COMPARAÇÃO DE ABORDAGENS")
    print("=======================================")
    
    n = 30
    
    # Fibonacci com memoização
    inicio = time.time()
    fib_memo = fibonacci_com_memoizacao(n)
    tempo_memo = time.time() - inicio
    
    # Fibonacci iterativo (da implementação anterior)
    def fib_iter(n):
        if n <= 1: return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    inicio = time.time()
    fib_iterativo = fib_iter(n)
    tempo_iter = time.time() - inicio
    
    print(f"Fibonacci({n}):")
    print(f"Com memoização: {fib_memo} ({tempo_memo:.6f}s)")
    print(f"Iterativo:      {fib_iterativo} ({tempo_iter:.6f}s)")
    print()
    
    # 4. Torre de Hanói
    print("4. TORRE DE HANÓI")
    print("=================")
    
    discos = 4
    movimentos = torre_hanoi(discos)
    
    print(f"Solucionando Torre de Hanói com {discos} discos:")
    print(f"Total de movimentos: {len(movimentos)}")
    print(f"Fórmula teórica: 2^{discos} - 1 = {2**discos - 1}")
    print("Primeiros 5 movimentos:")
    for i, movimento in enumerate(movimentos[:5]):
        print(f"  {i+1}. {movimento}")
    print()
    
    # 5. Algoritmos de Ordenação
    print("5. ALGORITMOS DE ORDENAÇÃO")
    print("==========================")
    
    dados_pequenos = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
    print(f"Dados originais: {dados_pequenos}")
    
    # Bubble Sort
    dados_bubble, comparacoes = bubble_sort(dados_pequenos)
    print(f"Bubble Sort: {dados_bubble}")
    print(f"Comparações: {comparacoes}")
    
    # Merge Sort
    dados_merge = merge_sort(dados_pequenos)
    print(f"Merge Sort:  {dados_merge}")
    print()
    
    # 6. Operações com Matrizes
    print("6. OPERAÇÕES COM MATRIZES")
    print("=========================")
    
    matriz_3x3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    elementos = percorrer_matriz(matriz_3x3)
    print(f"Matriz 3x3: {matriz_3x3}")
    print(f"Elementos (percorrimento): {elementos}")
    
    # Multiplicação de matrizes
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    resultado = multiplicar_matrizes_otimizada(A, B)
    print(f"A × B = {resultado}")
    print()
    
    # 7. Subconjuntos
    print("7. GERAÇÃO DE SUBCONJUNTOS")
    print("==========================")
    
    conjunto_pequeno = [1, 2, 3]
    subconjuntos = gerar_subconjuntos(conjunto_pequeno)
    
    print(f"Conjunto: {conjunto_pequeno}")
    print(f"Subconjuntos ({len(subconjuntos)}):")
    for i, sub in enumerate(subconjuntos):
        print(f"  {i}: {sub}")
    print()

def main():
    print("=== ANÁLISE AVANÇADA DE COMPLEXIDADE - PYTHON ===\n")
    
    demonstrar_complexidades()
    análise_performance()
    
    print("=== RESUMO DAS COMPLEXIDADES ===")
    print("O(1)      - Inserção lista ligada, acesso array")
    print("O(log n)  - Busca binária")
    print("O(n)      - Busca linear, fibonacci iterativo/memoizado")
    print("O(n log n)- Merge sort, sort do Python")
    print("O(n²)     - Bubble sort, percorrer matriz")
    print("O(n³)     - Multiplicação de matrizes")
    print("O(2^n)    - Torre de Hanói, gerar subconjuntos")
    print("O(n!)     - Gerar todas permutações")

if __name__ == "__main__":
    main()
