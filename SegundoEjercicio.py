from abc import ABC, abstractmethod
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato del nodo
        self.siguiente = None  # Inicialmente, el puntero al siguiente nodo es None

class ColaEnlazada(ABC):
    def __init__(self):
        self._frente = None  # El puntero al frente de la cola es None al inicio
        self._final = None   # El puntero al final de la cola es None al inicio
        self._tamano = 0     # Inicializa el tamaño de la cola en 0

    def encolar(self, elemento):
        nuevo_nodo = Nodo(elemento)  # Crea un nuevo nodo con el dato proporcionado
        if self._final is None:  # Si la cola está vacía
            self._frente = nuevo_nodo  # El puntero frente apunta al nuevo nodo
        else:  # Si la cola no está vacía
            self._final.siguiente = nuevo_nodo  # El nodo al final de la cola apunta al nuevo nodo
        self._final = nuevo_nodo  # El puntero final ahora apunta al nuevo nodo
        self._tamano += 1  # Incrementa el tamaño de la cola

    def desencolar(self):
        if self.esta_vacia():  # Si la cola está vacía
            raise IndexError("desencolar desde una cola vacía")  # Lanza una excepción
        dato = self._frente.dato  # Almacena el dato del nodo al frente de la cola
        self._frente = self._frente.siguiente  # Mueve el puntero frente al siguiente nodo
        if self._frente is None:  # Si la cola está vacía después de la eliminación
            self._final = None  # El puntero final también debe ser None
        self._tamano -= 1  # Decrementa el tamaño de la cola
        return dato  # Retorna el dato del nodo eliminado

    def frente(self):
        if self.esta_vacia():  # Si la cola está vacía
            raise IndexError("mirar desde una cola vacía")  # Lanza una excepción
        return self._frente.dato  # Retorna el dato del nodo al frente de la cola sin eliminarlo

    def esta_vacia(self):
        return self._frente is None  # Retorna True si la cola está vacía

    def tamano(self):
        return self._tamano  # Retorna el tamaño actual de la cola

    def mostrar(self):
        actual = self._frente  # Comienza desde el nodo al frente de la cola
        while actual:  # Mientras existan nodos en la cola
            print(actual.dato, end=" -> ")  # Imprime el dato del nodo actual
            actual = actual.siguiente  # Mueve al siguiente nodo
        print("None")  # Imprime None al final para indicar el final de la cola

# Ejemplo detallado de uso de la cola
if __name__ == "__main__":
    # Crear una instancia de la cola
    c = ColaEnlazada()
    
    # Mostrar el estado inicial de la cola
    print("Estado inicial de la cola:")
    c.mostrar()
    
    # Añadir elementos a la cola
    print("\nEncolando elementos...")
    c.encolar(50)
    c.encolar(80)
    c.encolar(40)
    
    # Mostrar el estado de la cola después de encolar elementos
    print("Estado de la cola después de encolar 10, 20 y 30:")
    c.mostrar()
    
    # Mostrar el tamaño de la cola
    print("\nTamaño de la cola:", c.tamano())
    
    # Mostrar el elemento al frente de la cola
    print("\nElemento al frente de la cola:", c.frente())
    
    # Desencolar un elemento y mostrar el estado de la cola
    print("\nDesencolando un elemento...")
    desencolado = c.desencolar()
    print("Elemento desencolado:", desencolado)
    print("Estado de la cola después de desencolar un elemento:")
    c.mostrar()
    
    # Desencolar otro elemento y mostrar el estado de la cola
    print("\nDesencolando otro elemento...")
    desencolado = c.desencolar()
    print("Elemento desencolado:", desencolado)
    print("Estado de la cola después de desencolar otro elemento:")
    c.mostrar()
    
    # Añadir más elementos a la cola
    print("\nEncolando más elementos...")
    c.encolar(40)
    c.encolar(50)
    
    # Mostrar el estado final de la cola
    print("Estado final de la cola después de encolar 40 y 50:")
    c.mostrar()
    
    # Mostrar el tamaño final de la cola
    print("\nTamaño final de la cola:", c.tamano())
    
    # Mostrar el elemento al frente de la cola
    print("\nElemento al frente de la cola:", c.frente())
