from abc import ABC, abstractmethod

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaCircular(ABC):
    def __init__(self):
        self.head = None
        self.size = 0

    def agregar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.head is None:
            self.head = nuevo_nodo
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = nuevo_nodo
            nuevo_nodo.next = self.head
        self.size += 1

    def eliminar(self, elemento):
        if self.head is None:
            return
        
        current = self.head
        prev = None
        
        while True:
            if current.data == elemento:
                if prev is not None:
                    prev.next = current.next
                else:
                    if current.next == self.head:
                        self.head = None
                    else:
                        temp = self.head
                        while temp.next != self.head:
                            temp = temp.next
                        self.head = current.next
                        temp.next = self.head
                self.size -= 1
                return
            
            prev = current
            current = current.next
            if current == self.head:
                break

    def contiene(self, elemento):
        if self.head is None:
            return False
        
        temp = self.head
        while True:
            if temp.data == elemento:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def esta_vacia(self):
        return self.head is None

    def tamano(self):
        return self.size

    def display(self):
        if self.head is None:
            print("La lista está vacía.")
            return
        
        nodes = []
        temp = self.head
        while True:
            nodes.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(map(str, nodes)) + " -> (head)")

# Ejemplo de uso
if __name__ == "__main__":
    cll = ListaCircular()
    cll.agregar(1)
    cll.agregar(2)
    cll.agregar(3)
    cll.display() # Output: 1 -> 2 -> 3 -> (head)
    print(cll.contiene(2)) # Output: True
    print(cll.contiene(4)) # Output: False
    cll.eliminar(2)
    cll.display() # Output: 1 -> 3 -> (head)
    print(cll.tamano()) # Output: 2
    print(cll.esta_vacia()) # Output: False
    cll.eliminar(1)
    cll.eliminar(3)
    print(cll.esta_vacia()) # Output: True
