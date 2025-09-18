def busca_binaria(lista, alvo, inicio=0, fim=None):
  if fim is None:
    fim = len(lista) - 1
    if inicio > fim:
      return -1
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
      return meio
    elif lista[meio] > alvo:
      return busca_binaria(lista, alvo, inicio, meio-1)
    else:
        return busca_binaria(lista, alvo, meio+1, fim)
    
lista_ordenada = [1, 3, 5, 7, 9, 11, 13]
posicao = busca_binaria(lista_ordenada, 7)
