from animal import Animal

class Mamifero(Animal):

  def __init__(self,nombre,edad,habitat,genero,zona,listado,caballos,leones,pelaje,patas):
     super().__init__(nombre,edad,habitat,genero,zona)
     self._listado = listado
     self._caballos = caballos
     self._leones = leones
     self._pelaje = pelaje
     self._patas = patas
    
  def cantidadMamiferos():
      return ""

  def crearCaballo():
      return ""

  def crearLeon():
      return ""