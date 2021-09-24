import abc
from unittest import TestCase, main

class CALCULADORA(object):

    def calcular(self, numero1, numero2, operador):
      operacaoCalc =OperacaoCalc()
      operacao = operacaoCalc.criar(operador)
      if(operacao == None):
        return 0
      else:
        resultado = operacao.executar(numero1, numero2)
        return resultado

'''------------------------------------------------------------'''


class OperacaoCalc(object):

    def criar(self, operador):
        if(operador == 'multiplicar'):
          return Multiplicar()
        elif(operador == 'dividir'):
          return Dividir()
        elif(operador == 'somar'):
          return Somar()
        elif(operador == 'subtrair'):
          return Subtrair()
      
        


'''------------------------------------------------------------'''



class Operacao(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def executar(self, numero1, numero2):
      pass

class Dividir(Operacao):
  
    def executar(self, numero1, numero2):
        resultado = numero1 /  numero2
        return resultado

class Multiplicar(Operacao):
  
    def executar(self, numero1, numero2):
        resultado = numero1 * numero2
        return resultado

class Somar(Operacao):
  
    def executar(self, numero1, numero2):
        resultado = numero1 + numero2
        return resultado

class Subtrair(Operacao):
  
    def executar(self, numero1, numero2):
        resultado = numero1 - numero2
        return resultado

'''------------------------------------------------------------'''

class Testes(TestCase):

    def test_dividir(self):
        calculator1 = CALCULADORA()
        self.assertEqual(calculator1.calcular(400,4, "dividir"), 100)

    def test_Multiplicar(self):
        calculator2 = CALCULADORA()
        result = (calculator2.calcular(5, 10, "multiplicar"))
        print(result)
        self.assertEqual(result, 50)
        
    def test_somar(self):
        calculator3 = CALCULADORA()
        self.assertEqual(calculator3.calcular(100, 150, "somar"), 250)
        
    def test_subtrair(self):
        calculator4 = CALCULADORA()
        self.assertEqual(calculator4.calcular(400,150, "subtrair"), 250)
        
    def test_multiplicar(self):
        calculatorX = CALCULADORA()
        self.assertEqual(calculatorX.calcular(5,50, "multiplicar"), 250)
       
  

'''-------------------------------------------------------------'''

calculador = CALCULADORA()
x = calculador.calcular(2,3, "somar")
print(x)

if __name__ == '__main__':

  main()
