import unittest
from validador import validar_contrasena

class TestValidadorContrasena(unittest.TestCase):
  def test_contrasena_valida(self):
    self.assertTrue(validar_contrasena("MiContraseña123!"))

  def test_contrasena_corta(self):
    self.assertFalse(validar_contrasena("1234567"))

  def test_falta_mayuscula(self):
    self.assertFalse(validar_contrasena("micontraseña123!"))

  # Agrega más casos de prueba para cubrir diferentes escenarios

if __name__ == '__main__':
  unittest.main()