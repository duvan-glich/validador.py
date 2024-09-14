
def validar_contrasena(contrasena):
  """Valida una contraseña según los criterios establecidos.

  Args:
    contrasena: La contraseña a validar.

  Returns:
    bool: True si la contraseña es válida, False si no.
  """

  tiene_mayuscula = False
  tiene_minuscula = False
  tiene_numero = False
  tiene_especial = False

  if len(contrasena) < 8:
    return False

  for caracter in contrasena:
    if caracter.isupper():
      tiene_mayuscula = True
    elif caracter.islower():
      tiene_minuscula = True
    elif caracter.isdigit():
      tiene_numero = True
    elif caracter in "!@#$%^&*":
      tiene_especial = True

  return all([tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_especial])

if __name__ == "__main__":
  contrasena = input("Ingrese la contraseña: ")
  if validar_contrasena(contrasena):
    print("La contraseña es válida.")
  else:
    print("La contraseña no es válida.")

