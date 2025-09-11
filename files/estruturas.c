#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Estrutura para nó da lista ligada
typedef struct No {
    int valor;
    struct No* proximo;
} No;

// Criar novo nó - O(1)
No* criar_no(int valor) {
    No* novo = malloc(sizeof(No));
    novo->valor = valor;
    novo->proximo = NULL;
    return novo;
}

// Inserir no início da lista - O(1)
No* inserir_inicio(No* head, int valor) {
    No* novo = criar_no(valor);
    novo->proximo = head;
    return novo;
}

// Percorrer lista - O(n)
void percorrer_lista(No* head) {
    No* atual = head;
    printf("[");
    while (atual != NULL) {
        printf("%d", atual->valor);
        if (atual->proximo != NULL) printf(", ");
        atual = atual->proximo;
    }
    printf("]\n");
}

// Buscar elemento na lista - O(n)
int buscar_lista(No* head, int valor) {
    No* atual = head;
    int posicao = 0;
    
    while (atual != NULL) {
        if (atual->valor == valor) {
            return posicao;
        }
        atual = atual->proximo;
        posicao++;
    }
    return -1;
}

// Liberar memória da lista
void liberar_lista(No* head) {
    while (head != NULL) {
        No* temp = head;
        head = head->proximo;
        free(temp);
    }
}

// Busca binária recursiva - O(log n)
int busca_binaria(int array[], int valor, int inicio, int fim) {
    if (inicio > fim) {
        return -1;
    }
    
    int meio = (inicio + fim) / 2;
    
    if (array[meio] == valor) {
        return meio;
    } else if (array[meio] > valor) {
        return busca_binaria(array, valor, inicio, meio - 1);
    } else {
        return busca_binaria(array, valor, meio + 1, fim);
    }
}

// Fibonacci recursivo - O(2^n)
long long fibonacci_recursivo(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2);
}

// Fibonacci iterativo - O(n)
long long fibonacci_iterativo(int n) {
    if (n <= 1) return n;
    
    long long a = 0, b = 1, temp;
    
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    
    return b;
}

// Factorial recursivo - O(n)
long long factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Percorrer matriz - O(n²)
void percorrer_matriz(int matriz[][3], int tamanho) {
    printf("Matriz %dx%d:\n", tamanho, tamanho);
    for (int i = 0; i < tamanho; i++) {
        for (int j = 0; j < tamanho; j++) {
            printf("%3d ", matriz[i][j]);
        }
        printf("\n");
    }
}

// Multiplicação de matrizes - O(n³)
void multiplicar_matrizes(int A[][3], int B[][3], int resultado[][3], int n) {
    // Inicializar resultado
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            resultado[i][j] = 0;
        }
    }
    
    // Multiplicação
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                resultado[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Torre de Hanoi - O(2^n)
void hanoi(int n, char origem, char destino, char auxiliar, int* contador) {
    if (n == 1) {
        printf("Mover disco 1 de %c para %c\n", origem, destino);
        (*contador)++;
        return;
    }
    
    hanoi(n-1, origem, auxiliar, destino, contador);
    printf("Mover disco %d de %c para %c\n", n, origem, destino);
    (*contador)++;
    hanoi(n-1, auxiliar, destino, origem, contador);
}

int main() {
    printf("=== Análise Avançada de Complexidade em C ===\n\n");
    
    // 1. Listas Ligadas - O(1) vs O(n)
    printf("1. LISTAS LIGADAS\n");
    printf("==================\n");
    
    No* lista = NULL;
    
    // Inserções O(1)
    lista = inserir_inicio(lista, 30);
    lista = inserir_inicio(lista, 20);
    lista = inserir_inicio(lista, 10);
    
    printf("Lista criada: ");
    percorrer_lista(lista);
    
    // Busca O(n)
    int posicao = buscar_lista(lista, 20);
    printf("Busca por valor 20: posição %d\n", posicao);
    
    // 2. Busca Binária - O(log n)
    printf("\n2. BUSCA BINÁRIA - O(log n)\n");
    printf("============================\n");
    
    int array_ordenado[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int tamanho = 10;
    
    printf("Array ordenado: ");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", array_ordenado[i]);
    }
    printf("\n");
    
    int pos_binaria = busca_binaria(array_ordenado, 7, 0, tamanho - 1);
    printf("Busca binária por 7: posição %d\n", pos_binaria);
    
    // 3. Fibonacci - Comparação O(2^n) vs O(n)
    printf("\n3. FIBONACCI - O(2^n) vs O(n)\n");
    printf("==============================\n");
    
    int n = 30;
    
    clock_t inicio = clock();
    long long fib_rec = fibonacci_recursivo(n);
    clock_t fim = clock();
    double tempo_rec = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    
    inicio = clock();
    long long fib_iter = fibonacci_iterativo(n);
    fim = clock();
    double tempo_iter = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    
    printf("Fibonacci(%d):\n", n);
    printf("Recursivo: %lld (%.6f segundos)\n", fib_rec, tempo_rec);
    printf("Iterativo: %lld (%.6f segundos)\n", fib_iter, tempo_iter);
    printf("Speedup: %.0fx mais rápido\n", tempo_rec / tempo_iter);
    
    // 4. Factorial - O(n)
    printf("\n4. FACTORIAL - O(n)\n");
    printf("===================\n");
    
    int num_fact = 12;
    long long resultado_fact = factorial(num_fact);
    printf("Factorial de %d: %lld\n", num_fact, resultado_fact);
    
    // 5. Matrizes - O(n²) e O(n³)
    printf("\n5. OPERAÇÕES COM MATRIZES\n");
    printf("=========================\n");
    
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[3][3] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int resultado[3][3];
    
    printf("Matriz A:\n");
    percorrer_matriz(A, 3);
    
    printf("\nMatriz B:\n");
    percorrer_matriz(B, 3);
    
    multiplicar_matrizes(A, B, resultado, 3);
    
    printf("\nResultado A × B:\n");
    percorrer_matriz(resultado, 3);
    
    // 6. Torre de Hanoi - O(2^n)
    printf("\n6. TORRE DE HANÓI - O(2^n)\n");
    printf("===========================\n");
    
    int discos = 3;
    int contador = 0;
    
    printf("Resolvendo Torre de Hanói com %d discos:\n", discos);
    hanoi(discos, 'A', 'C', 'B', &contador);
    printf("Total de movimentos: %d\n", contador);
    printf("Fórmula teórica: 2^%d - 1 = %d\n", discos, (1 << discos) - 1);
    
    // Análise de performance
    printf("\n=== ANÁLISE DE PERFORMANCE ===\n");
    printf("Testando com diferentes tamanhos de entrada:\n\n");
    
    // Teste busca linear vs binária
    const int sizes[] = {1000, 10000, 100000};
    const int num_sizes = 3;
    
    for (int s = 0; s < num_sizes; s++) {
        int size = sizes[s];
        int* test_array = malloc(size * sizeof(int));
        
        // Preencher array ordenado
        for (int i = 0; i < size; i++) {
            test_array[i] = i * 2;
        }
        
        int target = size - 10; // Buscar um valor próximo ao final
        
        // Busca linear
        inicio = clock();
        int found_linear = -1;
        for (int i = 0; i < size; i++) {
            if (test_array[i] == target) {
                found_linear = i;
                break;
            }
        }
        fim = clock();
        double tempo_linear = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        
        // Busca binária
        inicio = clock();
        int found_binary = busca_binaria(test_array, target, 0, size - 1);
        fim = clock();
        double tempo_binary = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        
        printf("Array tamanho %d:\n", size);
        printf("  Busca linear:  %.8f segundos\n", tempo_linear);
        printf("  Busca binária: %.8f segundos\n", tempo_binary);
        if (tempo_binary > 0) {
            printf("  Speedup: %.0fx\n", tempo_linear / tempo_binary);
        }
        printf("\n");
        
        free(test_array);
    }
    
    // Limpeza
    liberar_lista(lista);
    
    printf("=== RESUMO DAS COMPLEXIDADES ===\n");
    printf("O(1)      - Inserção no início da lista ligada\n");
    printf("O(log n)  - Busca binária\n");
    printf("O(n)      - Percorrer lista, fibonacci iterativo, factorial\n");
    printf("O(n²)     - Percorrer matriz\n");
    printf("O(n³)     - Multiplicação de matrizes\n");
    printf("O(2^n)    - Fibonacci recursivo, Torre de Hanói\n");
    
    return 0;
}
