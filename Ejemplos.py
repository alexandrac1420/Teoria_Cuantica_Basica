import vec_matrix_complex as lb
import numpy as np
from scipy.constants import hbar
import math

if __name__ == '__main__':
    constante = hbar/2

    print("---------------------- Problema 4.3.1 -----------------------------")
    matriz = np.array([[complex(0,0), complex(constante,0)],[complex(constante,0),complex(0,0)]])
    print("Los posibles estados del estado del ejercicio descrito en el ejercicio 4.2.2 son:")
    print(lb.val_prop_matrix(matriz)[1])
    print()

    print("---------------------- Problema 4.3.2 -----------------------------")
    vector = [complex(1,0), complex(0,0)]
    valor_propio_1 = lb.val_prop_matrix(matriz)[0][0]
    valor_propio_2 = lb.val_prop_matrix(matriz)[0][1]
    p1 = lb.val_prop_matrix(matriz)[1][0]
    p2 = lb.val_prop_matrix(matriz)[1][1]
    resultado = (valor_propio_1*p1)+(valor_propio_2*p2)
    print("La probabilidad de distribución de los valores propios es de:")
    resultado_redondeado = round(np.real(resultado[0]))
    print(resultado_redondeado)
    print()

    print("---------------------- Problema 4.4.1 -----------------------------")
    constante_2 = math.sqrt(2)/2
    u1 = np.array([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]])
    u2 = np.array([[complex(constante_2,0), complex(constante_2,0)], [complex(constante_2,0), complex(-constante_2,0)]])
    print("Verificamos si la matriz U1 dada en el ejercicio, es unitaria.")
    print(lb.unit_matrix(u1))
    print("Verificamos si la matriz U2 dada en el ejercicio, es unitaria.")
    print(lb.unit_matrix(u2))
    print("Como se determino que ambas son unitarias se procede a determianr si la multiplicación de ellas tambien lo es")
    u3 = lb.mult_matrix(u1, u2)
    print(lb.unit_matrix(u3))
    print()

    print("---------------------- Problema 4.4.2 -----------------------------")
    constante_3 = 1/math.sqrt(2)
    estado = [complex(1,0),complex(0,0),complex(0,0),complex(0,0)]
    u = np.array([[complex(0,0),complex(constante_3,0),complex(constante_3,0),complex(0,0)],[complex(0,constante_3),complex(0,0),complex(0,0),complex(constante_3,0)],[complex(constante_3,0),complex(0,0),complex(0,0),complex(0,constante_3)],[complex(0,0),complex(constante_3,0),complex(-constante_3,0),complex(0,0)]])
    for i in range(3):
        estado=lb.act_matrix_vec(u,estado)
    probabilidad = abs(estado[3]**2)
    print("El estado resultante despues de 3 pasos es:")
    print(estado)
    print("La probabilidad de que la bola cuantica se encuentre en el punto 3 es de:")
    print(probabilidad)
