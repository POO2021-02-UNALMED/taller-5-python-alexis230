from animal import Animal

class Ave(Animal):

  def __init__(self,nombre,edad,habitat,genero,zona,listado,halcones,aguila,colorPlumas):
     super().__init__(nombre,edad,habitat,genero,zona)
     self._listado = listado
     self._halcones = halcones
     self._aguila = aguila
     self._colorPlumas = colorPlumas
    
  def cantidadAves():
      return ""

  def movimiento():
      return ""

  def crearHalcon():
      return ""

  def crearAguila():
      return ""