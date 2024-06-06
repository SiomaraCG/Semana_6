# Se importa ABC para definir clases
from abc import ABC
class Nodo:
    def __init__(self, dato):
        # Almacena el dato del nodo
        self.dato = dato
        self.siguiente = None

# Definimos la clase Nodo, que representa un nodo en la lista enlazada
class PilaConListaEnlazada(ABC):
    def __init__(self):
        # Inicializa el tope de la pila como None
        self.tope = None
        # Inicializa el tamaño de la pila como 0
        self._tamano = 0

    # Método para apilar un elemento en la pila
    def apilar(self, elemento):
        # Se crea un nuevo nodo con el elemento
        nuevo_nodo = Nodo(elemento)
        nuevo_nodo.siguiente = self.tope
        # El nuevo nodo se convierte en el tope de la pila
        self.tope = nuevo_nodo
        # Se incrementa el tamaño de la pila
        self._tamano += 1
        # Se imprime el elemento apilado
        print(f"Apilado {elemento} en la pila")

    # Método para desapilar un elemento de la pila
    def desapilar(self):
        # Verifica si la pila está vacía
        if self.esta_vacia():
            # Se imprime el mensaje si la pila está vacía
            print("La pila está vacía. No se puede desapilar.")
            # Devuelve None si la pila está vacía
            return None
        # Guarda el nodo del tope actual
        nodo_desapilado = self.tope
        # El tope se convierte en el siguiente nodo
        self.tope = self.tope.siguiente
        # Decrementa el tamaño de la pila
        self._tamano -= 1
        # Se imprime el elemento desapilado
        print(f"Desapilado {nodo_desapilado.dato} de la pila")
        # Devuelve el dato del nodo desapilado
        return nodo_desapilado.dato

    # Método para obtener el elemento en la cima de la pila
    def cima(self):
        # Verifica si la pila está vacía
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        # Se imprime el elemento en la cima
        print(f"El elemento en la cima es {self.tope.dato}")
        return self.tope.dato

    # Método para verificar si la pila está vacía
    def esta_vacia(self):
        # Devuelve True si el tope es None, indicando que la pila está vacía
        return self.tope is None

    # Método para obtener el tamaño de la pila
    def tamano(self):
        print(f"El tamaño de la pila es {self._tamano}")
        # Devuelve el tamaño de la pila
        return self._tamano

    # Método para mostrar todos los elementos de la pila
    def mostrar(self):
        # Comienza en el tope de la pila
        actual = self.tope
        print("Los elementos en la pila son:")
        # Recorre mientras haya nodos
        while actual:
            # Se imprime el dato del nodo actual
            print(actual.dato)
            # Avanza al siguiente nodo
            actual = actual.siguiente

# Ejemplo de ejecución 
if __name__ == "__main__":
    # Se crea una instancia de PilaConListaEnlazada
    pila = PilaConListaEnlazada()
    # Se imprime el mensaje
    print("Apilando elementos en la pila...")
    # Se apila los elementos 10,20,30,40,50
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)
    pila.apilar(40)
    pila.apilar(50)

    print("\nEstado actual de la pila:")
    # Muestra el estado actual de la pila
    pila.mostrar()

    print("\nElemento en la cima de la pila:")
    # Muestra el elemento en la cima de la pila
    pila.cima()

    print("\nDesapilando elementos de la pila...")
    # Desapilamos dos elementos
    pila.desapilar()
    pila.desapilar()

    print("\nEstado actual de la pila después de desapilar dos elementos:")
    # Muestra el estado actual de la pila después de desapilar
    pila.mostrar()

    print("\nElemento en la cima de la pila:")
    # Muestra el elemento en la cima de la pila
    pila.cima()

    print("\nApilando más elementos en la pila...")
    # Se apila los elementos
    pila.apilar(60)
    pila.apilar(70)

    print("\nEstado final de la pila:")
    # Muestra el estado final de la pila
    pila.mostrar()

    print("\nTamaño final de la pila:")
    # Muestra el tamaño final de la pila
    pila.tamano()
