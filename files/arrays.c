#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Função para inserção no início do array - O(n)
void inserir_inicio(int array[], int *tamanho, int valor, int capacidade) {
    if (*tamanho >= capacidade) {
        printf("Array cheio!\n");
        return;
    }
    
    // Deslocar todos elementos para direita - O(n)
    for (int i = *tamanho; i > 0; i--) {
        array[i] = array[i-1];
    }
    
    array[0] = valor;
    (*tamanho)++;
}

// Busca linear - O(n)
int busca_linear(int array[], int tamanho, int valor) {
    for (int i = 0; i < tamanho; i++) {
        if (array[i] == valor) {
            return i; // Encontrou
        }
    }
    return -1; // Não encontrou
}

// Função auxiliar para ordenação QuickSort
int particionar(int array[], int inicio, int fim) {
    int pivot = array[fim];
    int i = inicio - 1;
    
    for (int j = inicio; j < fim; j++) {
        if (array[j] <= pivot) {
            i++;
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }
    
    int temp = array[i + 1];
    array[i + 1] = array[fim];
    array[fim] = temp;
    
    return i + 1;
}

// QuickSort - O(n log n)
void quicksort(int array[], int inicio, int fim) {
    if (inicio < fim) {
        int pi = particionar(array, inicio, fim);
        
        quicksort(array, inicio, pi - 1);
        quicksort(array, pi + 1, fim);
    }
}

// Imprimir array
void imprimir_array(int array[], int tamanho) {
    printf("[");
    for (int i = 0; i < tamanho; i++) {
        printf("%d", array[i]);
        if (i < tamanho - 1) printf(", ");
    }
    printf("]\n");
}

int main() {
    printf("=== Análise de Complexidade - Arrays em C ===\n\n");
    
    // Teste com array pequeno
    int array[20] = {50, 10, 40, 20, 30, 15, 25, 35, 45, 5};
    int tamanho = 10;
    
    printf("Array inicial: ");
    imprimir_array(array, tamanho);
    
    // 1. Acesso direto - O(1)
    printf("\n1. Acesso direto - O(1):\n");
    printf("Elemento no índice 3: %d\n", array[3]);
    
    // 2. Inserção no início - O(n)
    printf("\n2. Inserção no início - O(n):\n");
    inserir_inicio(array, &tamanho, 1, 20);
    printf("Após inserir 1 no início: ");
    imprimir_array(array, tamanho);
    
    // 3. Busca linear - O(n)
    printf("\n3. Busca linear - O(n):\n");
    int posicao = busca_linear(array, tamanho, 40);
    if (posicao != -1) {
        printf("Valor 40 encontrado na posição: %d\n", posicao);
    } else {
        printf("Valor 40 não encontrado\n");
    }
    
    // 4. Ordenação QuickSort - O(n log n)
    printf("\n4. Ordenação QuickSort - O(n log n):\n");
    quicksort(array, 0, tamanho - 1);
    printf("Array ordenado: ");
    imprimir_array(array, tamanho);
    
    // Teste de performance com array maior
    printf("\n=== Teste de Performance ===\n");
    
    const int N = 10000;
    int *array_grande = malloc(N * sizeof(int));
    
    // Preencher array com valores aleatórios
    srand(time(NULL));
    for (int i = 0; i < N; i++) {
        array_grande[i] = rand() % 1000;
    }
    
    // Medir tempo de busca linear
    clock_t inicio = clock();
    int encontrado = busca_linear(array_grande, N, 500);
    clock_t fim = clock();
    
    double tempo_busca = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Busca linear em %d elementos: %.6f segundos\n", N, tempo_busca);
    
    // Medir tempo de ordenação
    inicio = clock();
    quicksort(array_grande, 0, N - 1);
    fim = clock();
    
    double tempo_ordenacao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
    printf("Ordenação de %d elementos: %.6f segundos\n", N, tempo_ordenacao);
    
    free(array_grande);
    
    printf("\n=== Complexidades Demonstradas ===\n");
    printf("O(1)     - Acesso direto: array[i]\n");
    printf("O(n)     - Busca linear, inserção no início\n");
    printf("O(n log n) - QuickSort\n");
    
    return 0;
}
