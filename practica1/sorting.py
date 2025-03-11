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

import matplotlib.pyplot as plt

import random
from time import time
import numpy as np
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
        V_random_burbuja =[]  # RANDOM
        V_random_seleccion = []
        V_random_insercion = []
        V_directo_burbuja =[]  # DIRECTO
        V_directo_seleccion = []
        V_directo_insercion = []
        V_inverso_burbuja = []
        V_inverso_seleccion = []
        V_inverso_insercion = []
        V1 =[]  # INVERSO
        
    # Orden directo
        V2=GeneraD(n)
    # Orden inverso
        V3=GeneraI(n)
    # Experimento aleatorio
        tb = 0 # BURBUJA
        ti = 0 # INSERCION
        ts = 0 # SELECCION

        

        for _ in range(10):
# Aleatorio. 10 experimentos
# Realizar experimentos y completar las listas usando GeneraR(n)
            V1 = GeneraR(n)
            # BURBURJA
            tb = time()
            Burbuja(V1,n)
            tb = time() - tb
            V_random_burbuja.append(tb)
            # INSERCION
            ti = time()
            Insercion(V1,n)
            ti = time() - ti
            V_random_insercion.append(ti)
            # SELECCION
            ts = time()
            Seleccion(V1,n)
            ts = time() - ts
            V_random_seleccion.append(ts)
        np.mean(np.array(V_random_burbuja))
        np.mean(np.array(V_random_insercion))
        np.mean(np.array(V_random_seleccion))

# Experimento directo
        # BURBURJA
        tb = time()
        Burbuja(V2,n)
        tb = time() - tb
        V_directo_burbuja.append(tb)
        # INSERCION
        ti = time()
        Insercion(V2,n)
        ti = time() - ti
        V_directo_insercion.append(ti)
        # SELECCION
        ts = time()
        Seleccion(V2,n)
        ts = time() - ts
        V_directo_seleccion.append(ts)

# Experimento inverso
        # BURBURJA
        tb = time()
        Burbuja(V3,n)
        tb = time() - tb
        V_inverso_burbuja.append(tb)
        # INSERCION
        ti = time()
        Insercion(V3,n)
        ti = time() - ti
        V_inverso_insercion.append(ti)
        # SELECCION
        ts = time()
        Seleccion(V3,n)
        ts = time() - ts
        V_inverso_seleccion.append(ts)

        return np.mean(np.array(V_random_burbuja)),np.mean(np.array(V_random_seleccion)),np.mean(np.array(V_random_insercion)),V_directo_burbuja,V_directo_seleccion,V_directo_insercion,V_inverso_burbuja,V_inverso_seleccion,V_inverso_insercion
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
# Lista de tamaños
Tam=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Rellenar las listas con los experimentos

for i in Tam:
    k = i*100
    a,b,c,d,e,f,g,h,j = experimento(k)
    TB1.append(a)
    TS1.append(b)
    TI1.append(c)
    TB2.append(d)
    TS2.append(e)
    TI2.append(f)
    TB3.append(g)
    TS3.append(h)
    TI3.append(j)
# Presentar resultados


# Se imprimen las respectivas listas con pyplot
plt.plot(Tam,TI1,'r--',Tam,TS1,'bs',Tam,TB1,'g^')
plt.title('Burbuja')
plt.ylabel('Tiempo (s)')
plt.xlabel('Nodos (x 100)')
plt.show()

plt.plot(Tam,TI2,'r--',Tam,TS2,'bs',Tam,TB2,'g^')
plt.title('Inserción')
plt.xlabel('Nodos (x 100)')
plt.show()

plt.plot(Tam,TI3,'r--',Tam,TS3,'bs',Tam,TB3,'g^')
plt.title('Selección')
plt.ylabel('Tiempo (s)')
plt.xlabel('Nodos (x 100)')
plt.show()

print(TI1,Tam)