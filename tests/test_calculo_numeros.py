import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='200'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 200)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='300'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 300)

             #fin de los test de numeros validos

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='-100'
    )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='AAA'
    )
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main() 