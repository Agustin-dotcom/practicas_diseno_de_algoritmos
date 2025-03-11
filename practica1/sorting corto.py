#######################################################
#######################################################
#                                                     #
#            Diseño de Algoritmos 2015-2017           #
#                                                     #
#            Práctica 1                               #
#                                                     #
#            sorting                                  #
#                                                     #
#######################################################

import matplotlib.pyplot as plt  ##HE COMENTADO ESTO PORQUE ME DICE QUE NO EXISTE

import random
from time import time
#import numpy as np             ##HE COMENTADO ESTO PORQUE ME DICE QUE NO EXISTE
#import numpy.polynomial as P


def Burbuja(a,n):
    for i in range(1,n):
        for j in range(0,n-i):
            if(a[j] > a[j+1]):
                k = a[j+1]
                a[j+1] = a[j]
                a[j] = k;

def Insercion(a,n):
    for i in range(1,n):
        v=a[i]
        j=i-1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j=j-1
        a[j+1]=v

def Seleccion(a,n):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min=j
        aux=a[min]
        a[min]=a[i]
        a[i]=aux

def QuickSort(a,iz,de):
    i=iz
    j=de
    #
    # Selección del pivote
    # Elegir uno a descomentar
    #
    # Pivote en la mediana
    #x=a[int((iz + de)/2)]
    # Pivote en el lado izquierdo
    x=a[iz]
 
    while( i <= j ):
        while a[i]<x and j<=de:
            i=i+1
        while x<a[j] and j>iz:
            j=j-1
        if i<=j:
            aux = a[i]; a[i] = a[j]; a[j] = aux;
            i=i+1;  j=j-1;
 
    if iz < j:
        QuickSort( a, iz, j );
    if i < de:
        QuickSort( a, i, de );

def MergeSort(a,n):
    if n>1:
        m = n//2;
        l = a[:m]
        r = a[m:]

        MergeSort(l,len(l))
        MergeSort(r,len(r))

        i=0; j=0; k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k]=l[i]
                i=i+1
            else:
                a[k]=r[j]
                j=j+1
            k=k+1

        while i < len(l):
            a[k]=l[i]
            i=i+1
            k=k+1

        while j < len(r):
            a[k]=r[j]
            j=j+1
            k=k+1

def GeneraR(n):
    a=[]
    for i in range(0,n):
        a.append(random.randrange(0, n, 1))
    return a
    
def GeneraD(n):
    a=[]
    for i in range(0,n):
        a.append(i)
    return a   

def GeneraI(n):
    a=[]
    for i in range(0,n):
        a.append(n-i)
    return a   
    
def imprime(a,n):
    for i in range(0,n):
        print (a[i])
        
def experimento(n):
    V1 =[] 
    V2 =[]  
    V3 =[] 

# Orden directo
    V2=GeneraD(n)
# Orden inverso
    V3=GeneraI(n)
# Experimento aleatorio
    tb = 0
    ti = 0
    ts = 0
    for i in range(1,10):
        V1=V1+GeneraR(n)  ##SUMAMOS EN CADA ITERACIÓN LOS VALORES GENERADOS ALEATORIAMENTE
    V1=V1/10                ##AL TENERLOS TODOS, LO DIVIDIMOS POR 10, PORQUE HAY 10 VALORES SUMADOS
# Aleatorio. 10 experimentos
# Realizar experimentos y completar las listas usando GeneraR(n)

# Experimento directo

# Experimento inverso
# Listas iniciales
X  =[]
TI1=[]
TS1=[]  
TB1=[]  
TI2=[]
TS2=[]  
TB2=[] 
TI3=[]
TS3=[]  
TB3=[]  

# Rellenar las listas con los experimentos


# Presentar resultados
# Lista de tamaños
Tam=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


#print(TI1,Tam)
prueba=[]
for e in Tam:
    t=time()
    Burbuja(GeneraD(e*100), e*100)  ##1,2,3,4
    t=time()-t
    TB1.append(t)
    print("Burbuja de Derecho tamaño ",e*100,": ",t)
    

    t=time()
    Insercion(GeneraD(e*100), e*100)  ## 4,3,2,1
    t=time()-t
    TI1.append(t)
    print("Inserción de Derecho tamaño ",e*100,": ",t)
    
    t=time()
    Seleccion(GeneraD(e*100), e*100)  ##6,3,2,9
    t=time()-t
    TS1.append(t)
    print("Selección de Derecho tamaño ",e*100,": ",t)
    
    t=time()
    Burbuja(GeneraI(e*100), e*100) ##1,2,3,
    t=time()-t
    TB2.append(t)
    print("Burbuja de Inverso tamaño ",e*100,": ",t)
    
    t=time()
    Insercion(GeneraI(e*100), e*100)  ## 4,3,2,1
    t=time()-t
    TI2.append(t)
    print("Insercion de Inverso tamaño ",e*100,": ",t)
    
    t=time()
    Seleccion(GeneraI(e*100), e*100)  ##6,3,2,9
    t=time()-t
    TS2.append(t)
    print("Seleccion de Inverso tamaño ",e*100,": ",t)
    
    t=time()
    Burbuja(GeneraR(e*100), e*100)  ##1,2,3,4
    t=time()-t
    TB3.append(t)
    print("Burbuja de Random tamaño ",e*100,": ",t)
    
    t=time()
    Insercion(GeneraR(e*100), e*100)  ## 4,3,2,1
    t=time()-t
    TI3.append(t)
    print("Insercion de Random tamaño ",e*100,": ",t)
    
    t=time()
    Seleccion(GeneraR(e*100), e*100)  ##6,3,2,9
    t=time()-t
    TS3.append(t)
    print("Seleccion de Random tamaño ",e*100,": ",t)

print("Tiempos para burbuja")
print("Burbuja Directo")
print(TB1)
print("Burbuja Inverso")
print(TB2)
print("Burbuja Random")
print(TB3)


print("Tiempos para insercion")
print("Insercion Directo")
print(TI1)
print("Insercion Inverso")
print(TI2)
print("Insercion Random")
print(TI3)

print("Tiempos para selección")
print("Seleccion Directo")
print(TS1)
print("Seleccion Inverso")
print(TS2)
print("Seleccion Random")
print(TS3)


# Se imprimen las respectivas listas con pyplot VOY A DEJAR COMENTADA ESTE PARTE HASTA QUE TERMINEMOS
#plt.plot(Tam,TI1,'r--',Tam,TS1,'bs',Tam,TB1,'g^')
# plt.title('Burbuja')
# plt.ylabel('Tiempo (s)')
# plt.xlabel('Nodos (x 100)')
# plt.show()

plt.plot(Tam,TI2,'r--',Tam,TS2,'bs',Tam,TB2,'g^')
plt.title('Inserción')
plt.xlabel('Nodos (x 100)')

plt.show()

plt.plot(Tam,TI3,'r--',Tam,TS3,'bs',Tam,TB3,'g^')
plt.title('Selección')
plt.ylabel('Tiempo (s)')
plt.xlabel('Nodos (x 100)')
plt.show()

t=time()
MergeSort(GeneraD(100), 1000)
t=time()-t
print("Mergesort Directo tamaño de 100")
print(t)

t=time()
MergeSort(GeneraI(100), 1000)
t=time()-t
print("Mergesort inverso tamaño de 100")
print(t)


t=time()
MergeSort(GeneraR(100), 1000)
t=time()-t
print("Mergesort Random tamaño de 100")
print(t)

t=time()
QuickSort(GeneraD(100), 0, 99) ##Si es mucho mayor, llega al límite
t=time()-t
print("Quicksort derecho tamaño de 10000")
print(t)

t=time()
QuickSort(GeneraI(100), 0, 99) ##Si es mucho mayor, llega al límite
t=time()-t
print("Quicksort inverso tamaño de 10000")
print(t)

t=time()
QuickSort(GeneraR(100), 0, 99) ##Si es mucho mayor, llega al límite
t=time()-t
print("Quicksort random tamaño de 10000")
print(t)