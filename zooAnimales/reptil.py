from animal import Animal

class Reptil(Animal):

  def __init__(self,nombre,edad,habitat,genero,zona,listado,iguanas,serpientes,colorEscamas,largoCola):
     super().__init__(nombre,edad,habitat,genero,zona)
     self._listado = listado
     self._iguanas = iguanas
     self._serpientes = serpientes
     self._colorEscamas = colorEscamas
     self._largoCola = largoCola
    
  def cantidadReptiles():
      return ""

  def movimiento():
      return ""

  def crearIguana():
      return ""

  def crearSerpiente():
      return ""