#include <stdio.h>
#include <stdlib.h>

int* prepara_vetor(int tamanho);
int fibonacci_memoization(int elemento);
int fibonacci(int elemento, int *memo);
int fibo_calc(int elemento, int *memo);
void imprimir_analise_big_o(int n, int resultado);

int main(int argc, char const *argv[])
{
    int elemento = 20;
    int resultado = fibonacci_memoization(elemento);

    imprimir_analise_big_o(elemento, resultado);

    return 0;
}

/**
 * @brief Aloca e inicializa um vetor para ser usado na memoization.
 * @param tamanho_vetor O tamanho do vetor a ser criado.
 * @return int* Um ponteiro para o vetor recém-alocado e inicializado, ou NULL em caso de falha.
 */
int* prepara_vetor(int tamanho_vetor)
{
    int *vetor = malloc(tamanho_vetor * sizeof(int));

    if (vetor == NULL) {
        printf("Erro ao alocar memoria\n");
        return NULL;
    }

    for (int i = 0; i < tamanho_vetor; i++) {
        vetor[i] = -1;
    }

    return vetor;
}

/**
 * @brief Função orchestrator para calcular elemento fibonacci usando memoization.
 * @param elemento O número da sequência de Fibonacci a ser calculado
 * @return int O valor do elemento correspondente na sequência de Fibonacci
 */
int fibonacci_memoization(int elemento)
{
    if (elemento < 0) {
        printf("Elemento invalido\n");
        return -1;
    }

    int tamanho_elementos = elemento == 0 ? 1 : (elemento + 1);
    int *memo = prepara_vetor(tamanho_elementos);

    if (memo == NULL) {
        printf("Erro ao alocar memoria\n");
        return -1;
    }

    int resultado = fibonacci(elemento, memo);

    free(memo);
    return resultado;
}

/**
 * @brief Função recursiva que verifica o vetor de memoization antes de calcular.
 * @param elemento O elemento da sequência a ser verificado/calculado.
 * @param memo Um ponteiro para o vetor de memoization.
 * @return int O valor do elemento na sequência de Fibonacci.
 */
int fibonacci(int elemento, int *memo)
{
    if (memo[elemento] != -1) {
        return memo[elemento];
    } else if (elemento < 2) {
        return elemento;
    }

    memo[elemento] = fibo_calc(elemento, memo);

    return memo[elemento];
}

/**
 * @brief Realiza o cálculo recursivo da fórmula de Fibonacci.
 * @param elemento O elemento a ser calculado.
 * @param memo Um ponteiro para o vetor de memoization, a ser passado para as chamadas recursivas.
 * @return int O resultado do cálculo f(n-1) + f(n-2).
 */
int fibo_calc(int elemento, int *memo)
{
    return fibonacci(elemento - 1, memo) + fibonacci(elemento - 2, memo);
}

/**
 * @brief Imprime na tela uma análise de complexidade do algoritmo de Fibonacci com memoization.
 * @param n O elemento 'n' que foi usado como base para a análise.
 */
void imprimir_analise_big_o(int elemento, int resultado)
{
    printf("Para o elemento %d, o valor de Fibonacci é: %d\n", elemento, resultado);

    printf("\n--- Análise de Complexidade (Big O) para n = %d ---\n", elemento);
    printf("1. Complexidade de Tempo: O(n)\n");
    printf("   - Motivo: Graças à 'memoization' (o vetor 'memo'), cada número da sequência de Fibonacci (de 0 a n) é calculado apenas UMA VEZ.\n");
    printf("   - Quando um valor é necessário novamente, ele é lido do vetor em tempo constante O(1), em vez de ser recalculado.\n");
    printf("   - Sem a memoization, a complexidade seria O(2^n), que é exponencial e muito mais lenta.\n\n");

    printf("2. Complexidade de Espaço: O(n)\n");
    printf("   - Motivo: Para armazenar os resultados dos cálculos, precisamos alocar um vetor ('memo') de tamanho n + 1.\n");
    printf("   - O espaço de memória necessário cresce de forma linear com o valor de 'n'.\n");
}