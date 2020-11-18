class Notas:
  
  def __init__(self, list):
    self.set_ppractica(list[0])
    self.set_spractica(list[1])
    self.set_pparcial(list[2])
    self.set_sparcial(list[3])
    self.set_final(list[4])
  #end ctr

  def set_ppractica(self, value):
    self._ppractica = value
  #end method

  def set_spractica(self, value):
    self._spractica = value
  #end method

  def set_pparcial(self, value):
    self._pparcial = value
  #end method

  def set_sparcial(self, value):
    self._sparcial = value
  #end method

  def set_final(self, value):
    self._final = value
  #end method

  #getters
  def get_ppractica(self):
    return self._ppractica
  #end method

  def get_spractica(self):
    return self._spractica
  #end method

  def get_pparcial(self):
    return self._pparcial
  #end method

  def get_sparcial(self):
    return self._sparcial
  #end method

  def get_final(self):
    return self._final
  #end method
  
#end class