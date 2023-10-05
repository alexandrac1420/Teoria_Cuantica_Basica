import unittest
import Teoria_cuantica_basica as lb
import math
import numpy as np

class TestLibMatrixComplex(unittest.TestCase):
    v1 = [complex(2,-1), complex(0, 2), complex(1, -1), complex(1,0), complex(1, -2), complex(2,0)]
    v2 = [complex(0,(math.sqrt(2)/2)), complex(-(math.sqrt(2)/2),0)]
    v3 = [complex((math.sqrt(2)/2),0), complex(0,-(math.sqrt(2)/2))]

    def test_probabilidad_posicion(self):
        prueba_1 = lb.probabilidad_posicion(self.v1,3)
        self.assertAlmostEqual(prueba_1, 0.04761905)

    def test_amplitud_transitar(self):
        prueba_1 = lb.amplitud_transicion(self.v2, self.v3)
        self.assertAlmostEqual(prueba_1, 0)

    def test_probabilidad_transitar(self):
        prueba_1 = lb.probabilidad_transicion(self.v2, self.v3)
        self.assertAlmostEqual(prueba_1, 0)

    m1 = np.array([[complex(3,0),complex(1,2)],[complex(1,-2), complex(-1,0)]])
    v4 = [(math.sqrt(2))/2,-(math.sqrt(2))/2 ]
    def test_valor_esperado(self):
        prueba_1 = lb.valor_esperado(self.m1, self.v4)
        self.assertAlmostEqual(prueba_1,0)

    m2 = np.array([[complex(1, 0), complex(0, -1)], [complex(0, 1), complex(2, 0)]])
    v5 = [complex((math.sqrt(2))) / 2, complex(0,(math.sqrt(2)) / 2)]
    def test_varianza(self):
        prueba_1 = lb.varianza(self.m2, self.v5)
        self.assertAlmostEqual(prueba_1,-0.25)

if __name__ == '__main__':
        unittest.main()


