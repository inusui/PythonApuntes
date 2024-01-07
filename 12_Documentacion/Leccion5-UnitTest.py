import unittest

def doblar(a): return a*2
def sumar(a,b): return a+b
def es_par(a): return True if a%2 == 0 else False
class PruebasFunciones (unittest.TestCase):
    
    def testDoblar(self):
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'),'AbAb')
    def testUpper(self):
        self.assertEqual('hola'.upper(), 'HOLA')
        self.assertTrue('hola'.isupper())
    

if __name__ == "__main__":
    unittest.main()