from Notas import Notas
from Calculo import Calculo

class Alumno:

  def __init__(self,dic, matricula):
    self._matricula=matricula
    self._nombre=dic[matricula][0]
    self._nota= Notas(dic[matricula])
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
