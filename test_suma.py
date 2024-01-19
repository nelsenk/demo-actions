import unittest
from suma import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        # Pruebas adicionales
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(0, 5), 5)
        self.assertEqual(sumar(-5, 5), 0)

    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)
        # Pruebas adicionales
        self.assertEqual(restar(0, 0), 0)
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(-5, -2), -3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
        # Pruebas adicionales
        self.assertEqual(multiplicar(0, 5), 0)
        self.assertEqual(multiplicar(5, 2), 10)
        self.assertEqual(multiplicar(-5, -2), 10)

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-6, 2), -3)
        self.assertEqual(dividir(0, 5), 0)
        # Pruebas adicionales
        self.assertEqual(dividir(5, 1), 5)
        self.assertEqual(dividir(-10, -2), 5)

        # Prueba para dividir por cero
        with self.assertRaises(ValueError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
