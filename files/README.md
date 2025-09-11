# Arquivos de Análise de Complexidade - Big O Notation

Este diretório contém implementações práticas dos conceitos apresentados nos slides sobre Big O Notation, comparando Python e C.

## Arquivos Criados

### 📁 Arquivos C

#### `arrays.c`
- **Foco**: Operações básicas com arrays
- **Complexidades demonstradas**:
  - O(1): Acesso direto por índice
  - O(n): Busca linear, inserção no início
  - O(n log n): QuickSort
- **Características**:
  - Gerenciamento manual de memória
  - Implementação completa do QuickSort
  - Testes de performance com 10.000 elementos

#### `estruturas.c`
- **Foco**: Estruturas de dados avançadas e algoritmos recursivos
- **Complexidades demonstradas**:
  - O(1): Inserção em lista ligada
  - O(log n): Busca binária recursiva
  - O(n): Percorrer lista, factorial, fibonacci iterativo
  - O(n²): Percorrer matriz
  - O(n³): Multiplicação de matrizes
  - O(2^n): Fibonacci recursivo, Torre de Hanói
- **Características**:
  - Estruturas de dados com ponteiros
  - Comparação fibonacci recursivo vs iterativo
  - Implementação completa da Torre de Hanói
  - Análise de performance escalável

### 📁 Arquivos Python

#### `algoritmos.py`
- **Foco**: Algoritmos fundamentais e comparações de complexidade
- **Complexidades demonstradas**:
  - O(1): Acesso direto
  - O(log n): Busca binária
  - O(n): Busca linear, fibonacci iterativo, factorial
  - O(n log n): Ordenação (sorted)
  - O(n²): Percorrer matriz
  - O(n³): Multiplicação de matrizes
  - O(2^n): Fibonacci recursivo
  - O(n!): Geração de permutações
- **Características**:
  - Sintaxe Python limpa e legível
  - Medição precisa de tempo de execução
  - Demonstração clara do speedup entre abordagens

#### `estruturas_avancadas.py`
- **Foco**: Estruturas de dados avançadas e algoritmos de ordenação
- **Complexidades demonstradas**:
  - O(1): Operações de lista ligada
  - O(log n): Busca binária (iterativa e recursiva)
  - O(n): Fibonacci com memoização
  - O(n log n): Merge Sort
  - O(n²): Bubble Sort
  - O(n³): Multiplicação de matrizes
  - O(2^n): Torre de Hanói, geração de subconjuntos
  - O(n!): Permutações
- **Características**:
  - Implementação de classes para estruturas de dados
  - Comparação detalhada de algoritmos de ordenação
  - Análise de performance com diferentes tamanhos de entrada

### 📁 Utilitários

#### `executar.sh`
- Script para compilar e executar todos os programas
- Automatiza o processo de teste

## Como Executar

### Opção 1: Script Automático
```bash
chmod +x executar.sh
./executar.sh
```

### Opção 2: Manual

#### Programas C:
```bash
# Arrays
gcc -o arrays arrays.c
./arrays

# Estruturas
gcc -o estruturas estruturas.c
./estruturas
```

#### Programas Python:
```bash
python3 algoritmos.py
python3 estruturas_avancadas.py
```

## Resultados de Performance Observados

### Comparação Python vs C

| Operação | Python | C | Observações |
|----------|--------|---|-------------|
| Busca Linear (10k elementos) | ~0.0002s | ~0.000002s | C é ~100x mais rápido |
| Ordenação (10k elementos) | ~0.001s | ~0.001s | Ambos usam algoritmos otimizados |
| Fibonacci(30) Recursivo | ~0.23s | ~0.006s | C é ~38x mais rápido |
| Fibonacci(30) Iterativo | ~0.000009s | ~0.000000s | Ambos extremamente rápidos |

### Speedup Observado

| Algoritmo | Recursivo | Iterativo | Speedup |
|-----------|-----------|-----------|---------|
| Fibonacci Python | 0.23s | 0.000009s | ~26.000x |
| Fibonacci C | 0.006s | 0.000000s | ∞ (não mensurável) |

## Lições Importantes

1. **Big O é universal**: A mesma complexidade se aplica em ambas as linguagens
2. **Constantes importam**: C é geralmente mais rápido devido à compilação
3. **Algoritmo > Linguagem**: Escolher O(n) vs O(2^n) é mais importante que C vs Python
4. **Otimização**: Fibonacci iterativo vs recursivo mostra a importância da escolha algorítmica

## Complexidades Demonstradas

- ✅ **O(1)** - Acesso direto, inserção em lista ligada
- ✅ **O(log n)** - Busca binária (iterativa e recursiva)
- ✅ **O(n)** - Busca linear, percorrer estruturas, algorithms iterativos
- ✅ **O(n log n)** - QuickSort, MergeSort, Timsort
- ✅ **O(n²)** - Bubble Sort, percorrer matrizes, loops aninhados
- ✅ **O(n³)** - Multiplicação de matrizes (algoritmo ingênuo)
- ✅ **O(2^n)** - Fibonacci recursivo, Torre de Hanói, subconjuntos
- ✅ **O(n!)** - Geração de todas as permutações

## Conclusão

Os arquivos demonstram na prática como diferentes algoritmos escalam com o tamanho da entrada, validando a teoria apresentada nos slides sobre Big O Notation. A comparação entre Python e C mostra que, embora a linguagem afete as constantes de performance, a complexidade algorítmica é o fator dominante para a escalabilidade.
