from animal import Animal

class Pez(Animal):

  def __init__(self,nombre,edad,habitat,genero,zona,listado,salmones,bacalaos,colorEscamas,cantidadAletas):
     super().__init__(nombre,edad,habitat,genero,zona)
     self._listado = listado
     self._salmones = salmones
     self._bacalaos = bacalaos
     self._colorEscamas = colorEscamas
     self._cantidadAletas = cantidadAletas
    
  def cantidadPeces():
      return ""

  def movimiento():
      return ""

  def crearIguana():
      return ""

  def crearSerpiente():
      return ""