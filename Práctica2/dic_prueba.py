#
# Esta clase implementa un diccionario de prioridad
#
class dicPrioridad:
    
    # Constructor. Opcionalmente toma una lista de pares
    # (elemento,valor)
    def __init__(self,objetos=[]):
        self.diccionario = {}
        self.vector = [ ]
        self.tamano = -1 # Realmente es el índice del último elemento.
        # Se insertan de uno en uno los objetos.
        for (elemento,valor) in objetos:
            item = (elemento, valor)
            self.inserta(item)
 
     # Inserta un elemento
    def inserta(self, item):
        # Lo añade al final
        self.vector.append(item)
        self.tamano += 1
        
        #
        #  COMPLETAR
        #
        if len(self.diccionario) == 0:
            self.diccionario[item[0]] = self.tamano # item ('C',1) --> {'C':1,..}
        else:
            aux = []
            while len(self.diccionario)!=0:
                copia = list(self.diccionario.items()).pop()
                index = copia[1]
                if self.vector[index][1] >= item[1]:
                    break
                aux.append(copia)
                nombre = copia[0]
                del(self.diccionario[nombre])
            self.diccionario[item[0]] = self.tamano
            while len(aux) != 0:
                copia = aux.pop()
                nombre = copia[0]
                val = copia[1]
                self.diccionario[nombre] = val
            

    
    # Extrae el elemento mínimo del diccionario de prioridad
    def extrae_min(self):
        # Si el tamaño es -1, no devuelve nada
        if self.tamano == -1:
            return None
        #
        #  COMPLETAR
        #
        #return self.diccionario[self.tamano]
        #for i in self.diccionario.keys():
        #    return i
        #return self.vector.pop()
        key = list(self.diccionario).pop()
        index = self.diccionario[key]
        return self.vector[index]

    # Actualiza el valor de un elemento 
    def actualiza(self, item):
        # Posición del elemento que se va a modificar
        indice = self.diccionario[item[0]]
        # Se actualiza el elemento        
        self.vector[indice] = item

        #
        #  COMPLETAR
        #

        if self.vector[indice-1]<self.vector[indice]:
            indice_otro = self.vector[indice-1][0]
            temp = self.diccionario[indice_otro]
            self.diccionario[indice_otro] = indice
            indice_ = self.vector[indice][0]
            self.diccionario[indice_] = temp

            temp = self.vector[indice-1]
            self.vector[indice-1] = self.vector[indice]
            self.vector[indice] = temp
        if self.vector[indice] < self.vector[indice+1]:
            indice_otro = self.vector[indice+1][0]
            temp = self.diccionario[indice_otro]
            self.diccionario[indice_otro] = indice
            indice_ = self.vector[indice][0]
            self.diccionario[indice_] = temp

            temp = self.vector[indice+1]
            self.vector[indice+1] = self.vector[indice]
            self.vector[indice] = temp
        

    # Borra un elemento de la cola
    # No haremos uso de esta función
    def borra(self, elemento):
        # Si el elemento no está en el diccionario, vuelve
        if elemento not in self.diccionario:
            return
        # Índice del elemento
        indice = self.diccionario[elemento]
        # Lo intercambiamos con el último
        self.cambia_elementos(indice, self.tamano)
  
        # Borra el diccionario y del vector
        del(self.diccionario[elemento])
        del(self.vector[self.tamano])
        # Decrece el tamaño
        self.tamano -= 1        
        # Se arregla el heap
        # Se saca la posición del padre
        padre = self.nodopadre(indice)
        # Si el nodo tiene padre, y su valor es menor que el del padre
        if padre>0 and self.vector[indice][1]<self.vector[padre][1]:
            # Hace intercambio para arriba
            self.up_heapify(indice)
        # Si no
        else:
            # Hace intercambio para abajo
            self.down_heapify(indice)        
        
    # Reordena el diccionario de prioridad hacia arriba a partir del elemento
    # almacenado en la posicion indice
    def up_heapify(self,indice):
        # Si es la raíz del árbol, no hace nada.
        if indice == 0: 
            return
        # Saca el padre
        padre = self.nodopadre(indice)
        # Si el valor del índice es mayor que el del padre
        # se cumple la propiedad.  
        if (self.vector[indice][1]>=self.vector[padre][1]): 
            return 
        # Si no, hace el intercambio, y llama a la función 
        # recursiva con el padre.     
        else: 
            self.cambia_elementos(padre, indice)
            self.up_heapify(padre)
            return
    
    # Reordena el diccionario de prioridad hacia abajo a partir del elemento
    # almacenado en la posicion indice
    def down_heapify(self,indice):
        # Extrae los índices de los hijos.
        hijoIz = self.hijo_izquierdo(indice)
        hijoDe = self.hijo_derecho(indice)
        
        # Si el índice del hijo izquierdo es mayor que el tamaño es que
        # no tiene hijos, y vuelve.
        if hijoIz>self.tamano:
            return
        # Si no tiene hijo derecho, o el valor del hijo izquierdo es menor, entonces
        # el hijo a considerar es el izquierdo
        if hijoDe>self.tamano or (self.vector[hijoIz][1] < self.vector[hijoDe][1]):
            hijo = hijoIz
        # Si tiene hijo derecho y el hijo izquierdo no es menor, entonces utiliza el
        # derecho.    
        else:
            hijo = hijoDe
        
        # Si el valor del hijo es menor que el del padre
        # intercambia y llama a la función recursiva con el hijo.
        if self.vector[hijo][1] < self.vector[indice][1]:
            self.cambia_elementos(indice, hijo)
            self.down_heapify(hijo)
            return
   
    
    # Intercambia dos elementos (han de ser padre e hijo)
    def cambia_elementos(self, nodo1, nodo2):
        # Cambia los valores en el diccionario. 
        self.diccionario[self.vector[nodo1][0]] = nodo2
        self.diccionario[self.vector[nodo2][0]] = nodo1
        # Cambia los valores en el vector
        self.vector[nodo2],self.vector[nodo1] = self.vector[nodo1],self.vector[nodo2]        
       
         
    # Devuelve la posición del padre del elemento almacenado en la posición
    # indice del vector    
    def nodopadre(self,indice):    
        if (indice%2==0):  
            return int((indice-2) / 2) # Hijo derecho
        else:  
            return int((indice-1) / 2) # Hijo izquierdo
    
    # Devuelve la posición del hijo izquierdo del elemento almacenado en la 
    # posición indice del vector        
    def hijo_izquierdo(self,indice): 
        return 2*indice+1
    
    # Devuelve la posición del hijo izquierdo del elemento almacenado en la 
    # posición indice del vector        
    def hijo_derecho(self,indice): 
        return 2*indice+2  
      
    # Devuelve True si el elemento almacenado en la posición indice es una 
    # hoja del árbol.  
    def es_hoja(self,indice): 
        return (self.__hijo_izquierdo(indice) >= self.tamano) and (self.__hijo_derecho(indice) >= self.tamano)
    
    # Devuelve True si el elemento almacenado en la posición indice tiene
    # solamente un hijo.
    
    def un_hijo(self,indice): 
        return (self.__hijo_izquierdo(indice) < self.tamano) and (self.__hijo_derecho(indice) >= self.tamano)
        
        
    # Con estas funciones se premite llamar al diccionario de prioridad como a cualquier
    # otra secuencia    
        
    # Devuelve el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede utilizar 'dp[elemento]'
    def __getitem__(self,elemento):
        indice = self.diccionario[elemento]
        return self.vector[indice][1]   
    
    # Devuelve True si el diccionario contiene el elemento.
    # Si dp es un diccionario de prioridad, se puede usar 'elemento in dp'
    def __contains__(self,elemento):  
        return elemento in self.diccionario   
    
    # Esta función permite actualizar directamente el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede hacer 'dp[elemento]=valor'
    def __setitem__(self, elemento, valor):
        if elemento in self.diccionario:
            self.actualiza((elemento, valor))  
        else:
            self.inserta((elemento, valor))
        
    # Esta función permite actualizar directamente el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede hacer 'del dp[elemento]'        
    def __delitem__(self,elemento):      
        self.borra(elemento)  
                
# Esta función permite comprobar el funcionamiento del diccionario de prioridad.        
def test():
        L = [('A',6.5), ('B',4.3), ('C',3.7), ('D',5.8), ('E',9.1), ('F',7.2), ('G',7)]       
        # Creamos el diccionario de prioridad con la lista
        dp = dicPrioridad(L)
        print(dp.extrae_min())
        dp.inserta(('H', 1))
        print(dp['F'])
        dp.actualiza(('F',3))
        print(dp['F'])
        print('F' in dp)
        del dp['F']
        print('F' in dp)
        print(dp.extrae_min())
        dp['X'] = 3.14
        print(dp['X'])

test()   