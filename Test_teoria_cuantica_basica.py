import unittest
import Teoria_cuantica_basica as lb
import math
import numpy as np

class TestLibMatrixComplex(unittest.TestCase):
    num1 = math.sqrt(2)/2
    v1 = [complex(2,-1), complex(0, 2), complex(1, -1), complex(1,0), complex(1, -2), complex(2,0)]
    v2 = [complex(-3, -1), complex(0, -2), complex(0, 1), complex(2, 0)]
    v3 = [complex(num1,0), complex(0,num1)]
    v4 = [complex(0,num1), complex(-num1,0)]
    v5 = [complex(0, num1), complex(-num1, 0)]
    v6 = [complex(num1,0), complex(0,-num1)]

    def test_probabilidad_posicion(self):
        prueba_1 = lb.probabilidad_posicion(self.v1,3)
        self.assertAlmostEqual(prueba_1, 0.04761905)
        prueba_2 = lb.probabilidad_posicion(self.v2,2)
        self.assertAlmostEqual(prueba_2,0.05263157)

    def test_amplitud_transitar(self):
        prueba_1 = lb.amplitud_transicion(self.v3, self.v4)
        self.assertAlmostEqual(prueba_1, complex(0,-1))
        prueba_2 = lb.amplitud_transicion(self.v5, self.v6)
        self.assertAlmostEqual(prueba_2, 0)

    def test_probabilidad_transitar(self):
        prueba_1 = lb.probabilidad_transicion(self.v5, self.v6)
        self.assertAlmostEqual(prueba_1, 0)
        prueba_2 =lb.probabilidad_transicion(self.v3, self.v4)
        self.assertAlmostEqual(prueba_2, 1)

    m1 = np.array([[complex(1,0), complex(0,-1)],[complex(0,1), complex(2,0)]])
    v7 = [complex(num1,0), complex(0,num1)]
    m2 = np.array([[complex(3,0),complex(1,2)],[complex(1,-2), complex(-1,0)]])
    v8 = [complex(num1,0), complex(-num1,0)]
    def test_valor_esperado(self):
        prueba_1 = lb.valor_esperado(self.m1, self.v7)
        self.assertAlmostEqual(prueba_1,2.5)
        prueba_2 = lb.valor_esperado(self.m2, self.v8)
        self.assertAlmostEqual(prueba_2,0)

    m3 = np.array([[complex(1, 0), complex(0, -1)], [complex(0, 1), complex(2, 0)]])
    m4 = np.array([[complex(1, 0), complex(0, 0)], [complex(0, 0), complex(-1.0)]])
    v9 = [complex(num1, 0), complex(num1, 0)]

    def test_varianza(self):
        prueba_1 = lb.varianza(self.m3, self.v7)
        self.assertAlmostEqual(prueba_1,0.25)
        prueba_2 = lb.varianza(self.m4, self.v9)
        self.assertAlmostEqual(prueba_2,1)

    v10 = [complex(1,0), complex(-1,0)]
    v11 = [complex(1, 0), complex(1, 0)]
    def test_val_prop_probabilidades(self):
        prueba_1 = lb.val_propio_probabilidad(self.v10,self.m3)
        valores_propios = np.real(prueba_1[0])
        probabilidades = prueba_1[1]
        self.assertAlmostEqual(valores_propios[0],0.38196601)
        self.assertAlmostEqual(valores_propios[1],2.61803399)
        self.assertAlmostEqual(probabilidades[0],1)
        self.assertAlmostEqual(probabilidades[1],1)

        prueba_2 = lb.val_propio_probabilidad(self.v11, self.m4)
        valores_propios = np.real(prueba_2[0])
        probabilidades = prueba_2[1]
        self.assertAlmostEqual(valores_propios[0],1)
        self.assertAlmostEqual(valores_propios[1],-1)
        self.assertAlmostEqual(probabilidades[0],1)
        self.assertAlmostEqual(probabilidades[1],1)

    def test_dinamica_sist(self):
        prueba_1 = lb.dinamica_sist(self.v10,self.m3)
        self.assertAlmostEqual(prueba_1[0], complex(-1,1))
        self.assertAlmostEqual(prueba_1[1], complex(2,2))
        prueba_2 = lb.dinamica_sist(self.v11,self.m4)
        self.assertAlmostEqual(prueba_2[0], complex(0,0))
        self.assertAlmostEqual(prueba_2[1], complex(-1,0))

if __name__ == '__main__':
        unittest.main()



