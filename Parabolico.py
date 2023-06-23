#Jorge Armando Garcia Cuevas
#Calcula la curva de un tiro parabolico y la recta tangente a su vertice
#Entradas: Coordenadas del impacto, altura maxima
#Salidas: Ecuaciones de la curva y la recta tangente, longitud de la curva, grafica de la curva y la recta tangente
#Restricciones: La altura maxima debe ser mayor a 0
#Fecha: 22/06/2023
#Version: 1.0
#Compilador: Python 3.9.5 64-bits

import matplotlib.pyplot as plt                     #Libreria para graficar
from mpl_toolkits.mplot3d import Axes3D             #Libreria para graficar en 3D
import numpy as np                                  #Libreria para operaciones matematicas
import sympy as sp                                  #Libreria para operaciones matematicas

#Declaración de variables
Impacto=[0,0,0]                                     #Coordenadas del impacto
X=np.linspace(0,1,101)
Y=np.linspace(0,1,101)
Z=np.linspace(0,1,101)

#Lectura de variables
print("\nEl siguiente programa calculara a traves de la altura maxima y punto de impacto, la curva del tiro parabolico y la recta tangente a su vertice.\n")
Impacto[0]=float(input("Ingrese la coordenada x del impacto : "))
Impacto[1]=float(input("Ingrese la coordenada y del impacto : "))
h=float(input("Ingrese la altura máxima alcanzada : "))

#Imprime Ecuaciones
print("\nEcuacion de curva(Parabola) :")
k=h*4
if k>=0:
    c='+'
else:
    c='-'
print("\tr(t) = ( {0}t , {1}t , {2}t² {3} {4}t )\n".format(Impacto[0],Impacto[1],-k,c,abs(k)))

print("Recta tangente en el vertice de la parabola :")
print("\tx = {0}t\n\ty = {1}t\n\tz = {2}\n".format(Impacto[0],Impacto[1],h))

#Imprimir longitud de cuerda
if h!=0:
  t=sp.symbols('t')
  Gama=sp.sqrt(Impacto[0]**2+Impacto[1]**2+(-8*h*t+4*h)**2)
  IGama=sp.integrate(Gama,(t,0,1))
  print("La longitud de la Curva desde t=0 hasta t=1 es : {0} u".format(IGama.round(3)))

#Puntos de las funciones para poder graficar
for i in range(101):
    X[i]=Impacto[0]*X[i]
    Y[i]=Impacto[1]*Y[i]
    Z[i]=(h*4*Z[i])-(h*4*Z[i]*Z[i])

#Crear Grafica
figura=plt.figure(figsize=(10,6))
figura.suptitle("Tiro parabolico")
ax = figura.add_subplot(111,projection='3d')
ax.view_init(elev=25, azim=40)
ax.set_xlabel("Eje x")
ax.set_ylabel("Eje y")
ax.set_zlabel("Eje z")
limite_X=[min(0,Impacto[0]),max(0,Impacto[0])]
limite_Y=[min(0,Impacto[1]),max(0,Impacto[1])]
limite_Z=[0,h]
if(limite_X[0]==limite_X[1]):
    limite_X[0]-=2
    limite_X[1]+=2
if(limite_Y[0]==limite_Y[1]):
    limite_Y[0]-=2
    limite_Y[1]+=2
if(limite_Z[0]==limite_Z[1]):
    limite_X[0]-=2
    limite_X[1]+=2
ax.set_xlim(limite_X[0],limite_X[1])
ax.set_ylim(limite_Y[0],limite_Y[1])
ax.set_zlim(limite_Z[0],limite_Z[1])

#Curva
if h!=0:
   ax.plot(X,Y,Z,label="Parabola",c="blue",lw=2)

#Recta
if h!=0:
  ax.plot(X,Y,h,label="Recta Tangente al Vertice",c="green",lw=2)

#Puntos
if h!=0:
  ax.scatter(Impacto[0],Impacto[1],Impacto[2],label="Impacto=({0},{1},{2})".format(Impacto[0],Impacto[1],Impacto[2]),c="blueviolet",s=30)
  ax.scatter(Impacto[0]/2,Impacto[1]/2,h,label="Vertice=({0},{1},{2})".format(Impacto[0]/2,Impacto[1]/2,h),c="red",s=30)
  ax.scatter(0,0,0,label="Origen=(0,0,0)",c="bluesky",s=30)
  ax.legend(bbox_to_anchor=(1.4,1))

#Muestra grafico
plt.show()