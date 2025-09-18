# Simulando ponteiros com classes
class No:
    def __init__(self, valor):
      self.valor = valor
      self.proximo = None
head = No(1)
head.proximo = No(2)
head.proximo.proximo = No(3)
primeiro = head.valor
atual = head
while atual is not None:
  print(atual.valor)
  atual = atual.proximo