from Notas import Notas
from Calculo import Calculo

class Alumno:

  def __init__(self, dic):
    # formato del diccionario
    # dic ={'data':['20190506','juan','M'],'notas':[99,99,99,99,99,99,99]}
    self._matricula=dic['data'][0]
    self._nombre=dic['data'][1]
    self._sexo=dic['data'][2]
    self._nota= Notas(dic['notas'])
    self._calculo= Calculo(self._nota)
    #TO DO
    # add method of api +plus
  #end ctr

  def get_nombre(self):
    return self._nombre
  #end method

  def get_matricula(self):
    return self._matricula
  #end method

  def get_nombre(self):
    return self._nombre
  #end method

  def get_sexo(self):
    return self._sexo
  #end method

  def is_valid(self):
    valido= True
    if self._matricula=='' or len(self._matricula)!=8:
      valido=False
    if self._nombre=='':
      valido=False
    if self._sexo=='':
      valido=False
    return valido
  #end method

  def __str__(self):
    return f"""
    Matricula : {self.get_matricula()}
    Nombre : {self.get_nombre()}
    Calificaciones
    =================================
    Practica 1 : {self._nota.get_pparcial()}
    Practica 2 : {self._nota.get_spractica()}
    Promedio Practicas :{self._calculo.get_pr_practicas()}
    Parcial 1 : {self._nota.get_pparcial()}
    Parcial 2 : {self._nota.get_sparcial()}
    Promedio Parciales : {self._calculo.get_pr_parciales()}
    Examen Final : {self._nota.get_final()}
    Promedio Final : {self._calculo.get_pr_final()}
    Literal : {self._calculo.get_literal()}\n"""
  #end method

#end class
