import unittest
from ler2 import dados
from datetime import datetime, timedelta

class IMCTest(unittest.TestCase):
    def test_meninas(self):
        # Teste para menina de 6 anos
        menina6 = dados("Menina", '2019-02-01', 'Femi', 12, 1.0)
        self.assertEqual(0, menina6.getTarget())
        
        menina6_2 = dados("Menina", '2019-02-01', 'Femi', 15, 1.0)
        self.assertEqual(1, menina6_2.getTarget())
        
        # Teste para menina de 7 anos
        birth_date = (datetime.now() - timedelta(days=7*365)).strftime('%Y-%m-%d')
        menina7 = dados("Menina7", birth_date, 'Femi', 16, 1.0)
        self.assertEqual(1, menina7.getTarget())
        
        # Teste para menina de 8 anos (ajustado para 18.5kg)
        birth_date = (datetime.now() - timedelta(days=8*365)).strftime('%Y-%m-%d')
        menina8 = dados("Menina8", birth_date, 'Femi', 18.5, 1.0)
        self.assertEqual(2, menina8.getTarget())

    def test_meninos(self):
        # Teste para menino de 6 anos
        menino6 = dados("Menino", '2019-02-01', 'Masc', 13, 1.0)
        self.assertEqual(0, menino6.getTarget())
        
        # Teste para menino de 7 anos
        birth_date = (datetime.now() - timedelta(days=7*365)).strftime('%Y-%m-%d')
        menino7 = dados("Menino7", birth_date, 'Masc', 16, 1.0)
        self.assertEqual(1, menino7.getTarget())
        
        # Teste para menino de 8 anos
        birth_date = (datetime.now() - timedelta(days=8*365)).strftime('%Y-%m-%d')
        menino8 = dados("Menino8", birth_date, 'Masc', 17, 1.0)
        self.assertEqual(2, menino8.getTarget())

    def test_idade_invalida(self):
        # Teste para idade fora da faixa
        adulta = dados("Adulta", "2006-11-12", 'Femi', 50, 1.65)
        with self.assertRaises(ValueError):
            adulta.getTarget()
            
        crianca_nova = dados("Bebê", "2023-01-01", 'Masc', 10, 0.8)
        with self.assertRaises(ValueError):
            crianca_nova.getTarget()

    def test_genero_invalido(self):
        # Teste para gênero inválido
        invalido = dados("Inválido", "2018-01-01", 'Outro', 15, 1.0)
        with self.assertRaises(ValueError):
            invalido.getTarget()

    def test_calc_idade(self):
        # Teste para cálculo de idade
        birth_date = (datetime.now() - timedelta(days=7*365)).strftime('%Y-%m-%d')
        pessoa = dados("Teste", birth_date, 'Masc', 15, 1.0)
        self.assertEqual(7, pessoa.calcIdade())

    def test_str_representation(self):
        # Teste para representação string
        pessoa = dados("Teste", "2018-01-01", 'Masc', 15, 1.0)
        self.assertIsInstance(str(pessoa), str)

if __name__ == '__main__':
    unittest.main()