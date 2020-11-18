import sqlite3


class Data:
    def __init__(self):
        self.cConnect = sqlite3.connect("ESTUDIO")
        self.cCursorSql = self.cConnect.cursor()
        self.sentencia=""
    #end _init

    def seek(self):
        #table 1
        self.sentencia = "CREATE TABLE IF NOT EXISTS ESTUDIANTE (ID_ESTUDIANTE INTEGER PRIMARY KEY AUTOINCREMENT, MATRICULA INT NOT NULL, NOMBRE VARCHAR(15), SEXO NCHAR(1))"
        self.cCursorSql.execute(self.sentencia)
        #table 2
        self.sentencia = "CREATE TABLE IF NOT EXISTS MATERIA (CODIGO VARCHAR(6), NOMBRE_MATERIA VARCHAR(15))"
        self.cCursorSql.execute(self.sentencia)
        #table 3
        self.sentencia = '''CREATE TABLE IF NOT EXISTS CALIFICACIONES (ID_CALIFICACION INTEGER PRIMARY KEY AUTOINCREMENT, ID_ESTUDIANTE INTEGER, 
        ID_MATERIA VARCHAR(6), PRACTICA1 INT, PRACTICA2 INT, FORO1 INT, FORO2 INT, PRIMER_PARCIAL INT, SEGUNDO_PARCIAL INT, EXAMEN_FINAL INT,
        FOREIGN KEY(ID_ESTUDIANTE) REFERENCES ESTUDIANTE(ID_ESTUDIANTE),
        FOREIGN KEY(ID_MATERIA) REFERENCES MATERIA(CODIGO))'''
        self.cCursorSql.execute(self.sentencia)
    #end method

    def insert(self, varios, tabla, n):
        if self.exist(varios[0][0], tabla):
            self.update(varios, tabla) #pending
        else:
            try:
                self.sentencia=f"INSERT INTO {tabla} VALUES ({self.limit(n)})"
                self.cCursorSql.executemany(self.sentencia, varios)
                self.cConnect.commit()
                return 'insertado'
            except:
                return 'Error'
        #end condition
    #end methhod

    def update(self, varios, tabla):
        if tabla =="ESTUDIANTE":
            self.sentencia=f'''UPDATE {tabla}
                    SET MATRICULA = {varios[0][0]} ,
                        NOMBRE = '{varios[0][2]}' 
                    WHERE ID_ESTUDIANTE = {varios[0][0]}'''
        elif tabla=="MATERIA":
            self.sentencia=f'''UPDATE {tabla}
                    SET  NOMBRE_MATERIA = '{varios[0][1]}'
                    WHERE CODIGO = "{varios[0][0]}"'''
        elif tabla=="CALIFICACIONES":
            self.sentencia=f'''UPDATE {tabla}
                    SET CODIGO = {varios[0][0]} ,
                        NOMBRE_MATERIA = {varios[0][1]} 
                    WHERE CODIGO = {varios[0][0]}'''
        #end condition
        try:
            self.cCursorSql.execute(self.sentencia)
            self.cConnect.commit()
            return "editado"
        except:
            return "error"
        #end try
    #end method

    def consultar(self, tabla):
        self.sentencia = f"select * from '{tabla}'"
        return self.cCursorSql.execute(self.sentencia).fetchall()
    #end method

    def delete(self,_id, tabla, field):
        if _id!="":
            try:
                self.sentencia=f"DELETE FROM {tabla} WHERE {field}={_id}" if(tabla!='MATERIA') else f"DELETE FROM {tabla} WHERE {field}='{_id}'"
                print(self.sentencia)
                self.cCursorSql.execute(self.sentencia)
                self.cConnect.commit()
                return 'eliminado'
            except:
                return 'Error'
        else:
            return 'No valido'
    #end method

    def limit(self, n):
        texto=''
        for i in range(0,n):
            texto=texto=texto+'?,' if(i<(n-1)) else texto+'?'
        return texto
    #end method

    def infotabla(self,tabla):
        self.sentencia = """PRAGMA table_info({});""".format(tabla)
        return self.cCursorSql.execute(self.sentencia)
    #end method

    def exist(self, value, tabla):
        if tabla =="ESTUDIANTE":
            self.sentencia= f"select * from '{tabla}' where ID_ESTUDIANTE={value}"
            dataTable = self.cCursorSql.execute(self.sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
        elif tabla=="MATERIA":
            self.sentencia= f"select * from '{tabla}' where CODIGO='{value}'"
            dataTable = self.cCursorSql.execute(self.sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
        elif tabla=="CALIFICACIONES":
            self.sentencia= f"select * from '{tabla}' where ID_CALIFICACION={value}"
            dataTable = self.cCursorSql.execute(self.sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
#end method
#end class