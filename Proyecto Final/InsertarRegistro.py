class InsertarRegistro:
    def __init__(self):
        self.nombre = ""

    def insertar(self,varios,buscartabla,n):
        if exist(varios[0][0], buscartabla):
            print('existe')
            #update(varios, buscartabla)
        else:
            try:
                query=f"INSERT INTO {buscartabla} VALUES ({limit(n)})"
                CursorSql.executemany(query, varios)
                cConnect.commit()
                print('insertado')
            except:
                print('Error')   

    def validarEstudiante(self,mat, nom, sex):
        valido=True
        if mat=='' or len(mat)!=8:
            valido=False
        if nom=='':
            valido=False
        if sex=='':
            valido=False
        return valido     

    def insertarE(self,mat, nom, sex):
        if(self.validarEstudiante(mat,nom,sex)):
            self.insertar([(mat,mat,nom,sex)],'ESTUDIANTE',4)
        else:
            print('No valido')

    def insertarM(self,codigo, nombre):
        if nombre!="" and codigo!="":
            self.insertar([(codigo, nombre)], 'MATERIA',2)
        else:
            print('Materia No valida')

    def validarCalificacion(self,idEstudiante, idMateria, practica1, practica2, foro1, foro2, primerParcial, segundoParcial, examenFinal):
        valido=True
        if idEstudiante=='':
            valido=False
        if idMateria=='':
            valido=False
        if practica1==''or int(practica1) < 0 or int(practica1) > 100:
            valido=False
        if practica2=='' or int(practica2) < 0 or int(practica2) > 100:
            valido=False
        if foro1=='' or int(foro1) < 0 or int(foro1) > 100:
            valido=False
        if foro2=='' or int(foro2) < 0 or int(foro2) > 100:
            valido=False
        if primerParcial=='' or int(primerParcial) < 0 or int(primerParcial) > 100:
            valido=False
        if segundoParcial=='' or int(segundoParcial) < 0 or int(segundoParcial) > 100:
            valido=False
        if examenFinal=='' or int(examenFinal) < 0 or int(examenFinal) > 100:
            valido=False
        return valido

    def insertarC(self,idEstudiante, idMateria, practica1, practica2, foro1, foro2, primerParcial, segundoParcial, examenFinal):
        if(self.validarCalificacion(idEstudiante, idMateria, practica1, practica2, foro1, foro2, primerParcial, segundoParcial, examenFinal)):
            self.insertar([(idEstudiante,idEstudiante, idMateria, practica1, practica2, foro1, foro2, primerParcial, segundoParcial, examenFinal)],'CALIFICACIONES',10)
        else:
            print('No valido')