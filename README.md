# Teoria Cuantica Basica
El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.

2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
## Operaciones disponibles 
Dentro del programa se pueden realizar las siguientes operaciones:
* Calcular la probabilidad de encontrar la particula en una posición en particular.
* Calcular la probabilidad de transitar de un vector a otro

## ¿Cómo obtener una copia del repositorio?
### Pre-requisitos
Antes de comenzar con la ejecución de este proyecto, es necesario asegurarse de que se tiene instalado Python en su computador, debido a que este es el lenguaje de programación utilizado para desarrollar este proyecto. 
En caso de no tenerlo siga los siguientes pasos:
1. Dirigirse a la página https://www.python.org/downloads/
2. Dar click en la opción de descarga
   ![image](https://github.com/alexandrac1420/CNYT/assets/138069735/03d02dfb-a346-4bc8-8e9c-066816e2f80e)
3. Ejecutar el programa que se descarga automáticamente.

### Instalación 
Para instalar la librería debe tener en cuenta estos pasos:
1. Abra la carpeta en donde desea guardar la librería.
2. De click derecho y seleccione la opción "Git Bash"
3. Clone el repositorio utilizando el comando 'https://github.com/alexandrac1420/Simulacion_Clasico_Cuantico.git'
4. Importe el modulo de la libreria en el programa que vaya a utilizar.
   
Completado el proceso anterior podrá trabajar con la librería proporcionada.

Ademas se recomienda descargar la libreria de phyton numpy. Esta se puede descargar de la siguiente manera:
1. Abre una terminal o línea de comandos en tu sistema.
2. Ejecuta el siguiente comando: 'pip install numpy'
3. Una vez que la instalación se complete con éxito, abre el intérprete de Python y ejecuta 'import numpy as np'. Si no se produce ningún error, significa que NumPy se ha instalado correctamente.

## Modo de uso
Para utilizar esta librería es necesario conocer la estructura de entrada de las operaciones disponibles junto con la sintaxis adecuada de cada una de las operaciones.

### Representación 
El programa reconoce de entrada de numero complejo una parte real y una imaginaria representadas en tuplas. Por ejemplo, si quiero realizar alguna operación con el numero 5 + 2i, este se ingresará al programa de la siguiente manera complex(5,2).

Para ingresar un vector de números complejos se debe seguir la siguiente estructura __vector = [complex(numero1), complex(numero2)]__


### Sintaxis operaciones 
A continuación se presenta la sintaxis correcta para el uso de las operaciones disponibles:
* __Calcular la probabilidad de encontrar la particula en una posición en particular__:probabilidad_posicion (_vector, posicion_)
* __Calcular la probabilidad de transitar de un vector a otro__:probabilidad_posicion (_vector 1, vector 2_)

Tenga en cuenta que es necesario utilizar la representacion de los numeros mencionada anteriormente.

### Ejemplo de uso 
~~~python
import Teoria_cuantica_basica as lb
import numpy as np

#Calcular la probabilidad de encontrar la particula en una posición en particular
#Ingrese el vector que desea estudiar junto con la posicion
v1 = [complex(2,-1), complex(0, 2), complex(1, -1), complex(1,0), complex(1, -2), complex(2,0)]
posicion = 3

#Realice la simulacion
resultado = lb.probabilidad_posicion(v1,posicion)
print(resultado)

#Calcular la probabilidad de transitar de un vector a otro
#Ingrese los dos vectores 
v2 = [complex(0,(math.sqrt(2)/2)), complex(-(math.sqrt(2)/2),0)]
v3 = [complex((math.sqrt(2)/2),0), complex(0,-(math.sqrt(2)/2))]

#Realice la simulacion
resultado = lb.probabilidad_transicion(v2,v3)
print(resultado)
~~~


## Construido con
* Phyton 3.11.4
  
## Autor 
__Alexandra Cortes Tovar__ 