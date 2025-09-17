#include <stdio.h>  // O(1) - include de biblioteca
#include <stdlib.h>  // O(1) - include de biblioteca
#include <time.h>  // O(1) - include de biblioteca

// Função para inserção no início do array - O(n)
void inserir_inicio(int array[], int *tamanho, int valor, int capacidade) {
    if (*tamanho >= capacidade) {  // O(1) - comparação
        printf("Array cheio!\n");  // O(1) - operação de I/O
        return;  // O(1) - retorno
    }

    // Deslocar todos elementos para direita - O(n)
    for (int i = *tamanho; i > 0; i--) {  // O(n) - loop que percorre array
        array[i] = array[i-1];  // O(1) - atribuição e acesso
    }

    array[0] = valor;  // O(1) - atribuição direta
    (*tamanho)++;  // O(1) - incremento
}
// COMPLEXIDADE FINAL: O(n) - loop de deslocamento domina, O(1) desconsiderado

// Busca linear - O(n)
int busca_linear(int array[], int tamanho, int valor) {
    for (int i = 0; i < tamanho; i++) {  // O(n) - percorre array até encontrar
        if (array[i] == valor) {  // O(1) - comparação
            return i; // O(1) - retorno quando encontra
        }
    }
    return -1; // O(1) - retorno quando não encontra
}
// COMPLEXIDADE FINAL: O(n) - pior caso percorre todo array, O(1) desconsiderado

// Função auxiliar para ordenação QuickSort
int particionar(int array[], int inicio, int fim) {
    int pivot = array[fim];  // O(1) - escolha do pivô
    int i = inicio - 1;  // O(1) - inicialização

    for (int j = inicio; j < fim; j++) {  // O(n) - percorre subarray
        if (array[j] <= pivot) {  // O(1) - comparação
            i++;  // O(1) - incremento
            int temp = array[i];  // O(1) - troca de elementos
            array[i] = array[j];  // O(1) - atribuição
            array[j] = temp;  // O(1) - atribuição
        }
    }

    int temp = array[i + 1];  // O(1) - posicionar pivô
    array[i + 1] = array[fim];  // O(1) - atribuição
    array[fim] = temp;  // O(1) - atribuição

    return i + 1;  // O(1) - retorno da posição do pivô
}
// COMPLEXIDADE FINAL: O(n) - loop principal domina, operações O(1) desconsideradas

// QuickSort - O(n log n)
void quicksort(int array[], int inicio, int fim) {
    if (inicio < fim) {  // O(1) - condição de parada
        int pi = particionar(array, inicio, fim);  // O(n) - particionamento

        quicksort(array, inicio, pi - 1);  // O(log n) - recursão esquerda
        quicksort(array, pi + 1, fim);     // O(log n) - recursão direita
    }
}
// COMPLEXIDADE FINAL: O(n log n) - particionamento O(n) × níveis O(log n)

// Imprimir array
void imprimir_array(int array[], int tamanho) {
    printf("[");  // O(1) - operação de I/O
    for (int i = 0; i < tamanho; i++) {  // O(n) - percorre todo array
        printf("%d", array[i]);  // O(1) - operação de I/O
        if (i < tamanho - 1) printf(", ");  // O(1) - condição e I/O
    }
    printf("]\n");  // O(1) - operação de I/O
}
// COMPLEXIDADE FINAL: O(n) - loop percorre todo array, operações O(1) desconsideradas

int main() {
    printf("=== Análise de Complexidade - Arrays em C ===\n\n");  // O(1) - I/O

    // Teste com array pequeno
    int array[20] = {50, 10, 40, 20, 30, 15, 25, 35, 45, 5};  // O(1) - inicialização
    int tamanho = 10;  // O(1) - atribuição

    printf("Array inicial: ");  // O(1) - I/O
    imprimir_array(array, tamanho);  // O(n) - chama função que percorre array

    // 1. Acesso direto - O(1)
    printf("\n1. Acesso direto - O(1):\n");  // O(1) - I/O
    printf("Elemento no índice 3: %d\n", array[3]);  // O(1) - acesso direto e I/O
    
    // 2. Inserção no início - O(n)
    printf("\n2. Inserção no início - O(n):\n");  // O(1) - I/O
    inserir_inicio(array, &tamanho, 1, 20);  // O(n) - chama função que desloca elementos
    printf("Após inserir 1 no início: ");  // O(1) - I/O
    imprimir_array(array, tamanho);  // O(n) - percorre array
    
    // 3. Busca linear - O(n)
    printf("\n3. Busca linear - O(n):\n");  // O(1) - I/O
    int posicao = busca_linear(array, tamanho, 40);  // O(n) - busca elemento
    if (posicao != -1) {  // O(1) - comparação
        printf("Valor 40 encontrado na posição: %d\n", posicao);  // O(1) - I/O
    } else {
        printf("Valor 40 não encontrado\n");  // O(1) - I/O
    }
    
    // 4. Ordenação QuickSort - O(n log n)
    printf("\n4. Ordenação QuickSort - O(n log n):\n");  // O(1) - I/O
    quicksort(array, 0, tamanho - 1);  // O(n log n) - algoritmo de ordenação
    printf("Array ordenado: ");  // O(1) - I/O
    imprimir_array(array, tamanho);  // O(n) - percorre array
    
    // Teste de performance com array maior
    printf("\n=== Teste de Performance ===\n");  // O(1) - I/O

    const int N = 10000;  // O(1) - declaração de constante
    int *array_grande = malloc(N * sizeof(int));  // O(1) - alocação de memória
    
    // Preencher array com valores aleatórios
    srand(time(NULL));  // O(1) - inicialização do gerador aleatório
    for (int i = 0; i < N; i++) {  // O(n) - loop para preencher array
        array_grande[i] = rand() % 1000;  // O(1) - geração e atribuição
    }
    
    // Medir tempo de busca linear
    clock_t inicio = clock();  // O(1) - captura tempo inicial
    int encontrado = busca_linear(array_grande, N, 500);  // O(n) - busca linear
    clock_t fim = clock();  // O(1) - captura tempo final

    double tempo_busca = ((double)(fim - inicio)) / CLOCKS_PER_SEC;  // O(1) - cálculo
    printf("Busca linear em %d elementos: %.6f segundos\n", N, tempo_busca);  // O(1) - I/O
    
    // Medir tempo de ordenação
    inicio = clock();  // O(1) - captura tempo inicial
    quicksort(array_grande, 0, N - 1);  // O(n log n) - ordenação
    fim = clock();  // O(1) - captura tempo final

    double tempo_ordenacao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;  // O(1) - cálculo
    printf("Ordenação de %d elementos: %.6f segundos\n", N, tempo_ordenacao);  // O(1) - I/O
    
    free(array_grande);  // O(1) - liberação de memória

    printf("\n=== Complexidades Demonstradas ===\n");  // O(1) - I/O
    printf("O(1)     - Acesso direto: array[i]\n");  // O(1) - I/O
    printf("O(n)     - Busca linear, inserção no início\n");  // O(1) - I/O
    printf("O(n log n) - QuickSort\n");  // O(1) - I/O

    return 0;  // O(1) - retorno
}

/*
=== ANÁLISE COMPLETA DE COMPLEXIDADE BIG O ===

1. CONSTANTE - O(1):
   - Acesso direto a array: array[i]
   - Operações aritméticas: +, -, *, /, %
   - Comparações: ==, <, >, <=, >=, !=
   - Atribuições: x = y
   - Operações de I/O: printf(), scanf()
   - Chamadas de função com trabalho constante

2. LINEAR - O(n):
   - Busca linear: percorre array até encontrar elemento
   - Inserção no início: desloca todos os elementos
   - Impressão de array: percorre todos os elementos
   - Preenchimento de array: inicializa todos os elementos
   - Loops simples que percorrem estrutura uma vez

3. LINEARÍTMICA - O(n log n):
   - QuickSort (caso médio): divide array e conquista recursivamente
   - MergeSort: sempre divide pela metade e mescla
   - HeapSort: constrói heap e remove elementos
   - Algoritmos "divide e conquista" eficientes

4. QUADRÁTICA - O(n²):
   - Bubble Sort: compara cada elemento com todos os outros
   - Selection Sort: encontra mínimo em cada iteração
   - Insertion Sort: insere cada elemento na posição correta
   - Dois loops aninhados que percorrem a estrutura

5. CÚBICA - O(n³):
   - Multiplicação de matrizes (algoritmo ingênuo)
   - Três loops aninhados
   - Algoritmos que operam em estruturas tridimensionais

CARACTERÍSTICAS DO QUICKSORT:
- Melhor caso: O(n log n) - pivô sempre divide array pela metade
- Caso médio: O(n log n) - boa escolha de pivô na maioria das vezes
- Pior caso: O(n²) - pivô sempre é o menor ou maior elemento
- Espaço: O(log n) - devido às chamadas recursivas

PARTICIONAMENTO - ANÁLISE DETALHADA:
- Escolha do pivô: O(1)
- Loop principal: O(n) - percorre subarray uma vez
- Trocas de elementos: O(1) cada
- Posicionamento final do pivô: O(1)
- Total: O(n) para cada particionamento

RECURSÃO DO QUICKSORT:
- Cada nível de recursão: O(n) devido ao particionamento
- Número de níveis: O(log n) no caso médio
- Total: O(n) × O(log n) = O(n log n)

ORDEM DE CRESCIMENTO (melhor para pior):
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2^n) < O(n!)

EXEMPLOS PRÁTICOS COM n=1000:
- O(1): 1 operação
- O(log n): ~10 operações
- O(n): 1.000 operações
- O(n log n): ~10.000 operações
- O(n²): 1.000.000 operações
- O(n³): 1.000.000.000 operações

DICAS DE OTIMIZAÇÃO:
1. Use acesso direto (O(1)) sempre que possível
2. Prefira algoritmos O(n log n) para ordenação
3. Evite algoritmos O(n²) para grandes conjuntos de dados
4. Cache resultados para evitar recálculos
5. Use estruturas de dados apropriadas (hash tables, árvores balanceadas)

=== ANÁLISE DE COMPLEXIDADE: DETERMINANDO O TERMO DOMINANTE ===

REGRA FUNDAMENTAL: Considere apenas o termo de MAIOR CRESCIMENTO

EXEMPLOS DE ANÁLISE EM C:

1. FUNÇÃO inserir_inicio():
   - Verificação if: O(1)
   - Loop for deslocamento: O(n)
   - Atribuições: O(1)
   TOTAL: O(1) + O(n) + O(1) = O(n)
   RESULTADO: O(n) - termo linear domina

2. FUNÇÃO busca_linear():
   - Loop for: O(n) no pior caso
   - Comparações dentro do loop: O(1)
   - Retornos: O(1)
   TOTAL: O(n) × O(1) + O(1) = O(n)
   RESULTADO: O(n) - busca sequencial

3. FUNÇÃO particionar():
   - Inicializações: O(1)
   - Loop principal: O(n)
   - Trocas dentro do loop: O(1)
   - Posicionamento do pivô: O(1)
   TOTAL: O(1) + O(n) × O(1) + O(1) = O(n)
   RESULTADO: O(n) - percorre subarray uma vez

4. FUNÇÃO quicksort():
   - Particionamento: O(n)
   - Duas chamadas recursivas: 2 × T(n/2)
   - Relação de recorrência: T(n) = 2T(n/2) + O(n)
   RESULTADO: O(n log n) - caso médio

5. FUNÇÃO main() - ANÁLISE POR SEÇÕES:
   - Inicializações: O(1)
   - Acesso direto: O(1)
   - Inserção no início: O(n)
   - Busca linear: O(n)
   - QuickSort: O(n log n)
   - Loop de preenchimento: O(n)
   - Teste de busca: O(n)
   - Teste de ordenação: O(n log n)
   TOTAL: O(1) + O(1) + O(n) + O(n) + O(n log n) + O(n) + O(n) + O(n log n)
   RESULTADO: O(n log n) - ordenação domina

REGRAS PARA LOOPS:
- Loop simples até n: O(n)
- Dois loops aninhados até n: O(n²)
- Três loops aninhados até n: O(n³)
- Loop que divide n pela metade: O(log n)

REGRAS PARA RECURSÃO:
- Uma chamada por nível, n níveis: O(n)
- Duas chamadas por nível, log n níveis: O(n log n)
- Duas chamadas por nível, n níveis: O(2^n)

SIMPLIFICAÇÃO DE POLINÔMIOS:
- 5n + 3 → O(n)
- 2n² + 100n + 50 → O(n²)
- n³ + n² log n + n → O(n³)
- 2^n + n! → O(n!) [factorial domina exponencial]
*/
