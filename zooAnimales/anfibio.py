from animal import Animal

class Anfibio(Animal):

  def __init__(self,nombre,edad,habitat,genero,zona,listado,ranas,salamandras,colorPiel,venenoso):
     super().__init__(nombre,edad,habitat,genero,zona)
     self._listado = listado
     self._ranas = ranas
     self._salamandras = salamandras
     self._colorPiel = colorPiel
     self._venenoso = venenoso
    
  def cantidadAnfibios():
      return ""

  def movimiento():
      return ""

  def crearRana():
      return ""

  def crearSalamandra():
     return ""