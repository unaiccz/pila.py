class pila():
    def __init__(self,size):
        self.size = size
        self.lista = [] * self.size
    def ap(self, valor):
        print(f'adding... {valor}')
        if len(self.lista) == self.size:
            print('list is full')
            exit()
    
        self.lista.append(valor)
        print(self.lista)
    def pop(self):
        if (len(self.lista) > 0):
            print(f'removing... {self.lista[-1]}')
            self.lista.pop()
            print(self.lista)
        else:
            print('list is empty')
            exit()
#  create object
l1 = pila(5)
#  add values
l1.ap(2)
l1.ap(3)
l1.ap(4)
#  remove values
l1.pop()
l1.pop()
l1.pop()
l1.pop()

l1.pop()
l1.pop()