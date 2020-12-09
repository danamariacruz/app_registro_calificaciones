import sqlite3


class Data:
    def __init__(self):
        self._cConnect = sqlite3.connect("ESTUDIO")
        self._cCursorSql = self._cConnect.cursor()
        self._sentencia=""
        self.seek()
    #end _init

    def seek(self):
        #table 1
        self._sentencia ="CREATE TABLE IF NOT EXISTS PROVINCIA (CODIGO INTEGER PRIMARY KEY, DESCRIPCION VARCHAR(30),LATITUD VARCHAR(10), LONGITUD VARCHAR(10))"
        self._cCursorSql.execute(self._sentencia)
        #table 2
        self._sentencia ="CREATE TABLE IF NOT EXISTS CARRERA (CODIGO INTEGER PRIMARY KEY, DESCRIPCION VARCHAR(60))"
        self._cCursorSql.execute(self._sentencia)
        #table 3
        self._sentencia = '''CREATE TABLE IF NOT EXISTS ESTUDIANTE (ID_ESTUDIANTE INTEGER PRIMARY KEY AUTOINCREMENT, MATRICULA INT NOT NULL, NOMBRE VARCHAR(30), 
            APELLIDO VARCHAR(50), CEDULA VARCHAR(15),FOTO VARCHAR(60), SEXO NCHAR(1), PROVINCIA VARCHAR(30), CARRERA VARCHAR(60))'''
        self._cCursorSql.execute(self._sentencia)
        #table 4
        self._sentencia = "CREATE TABLE IF NOT EXISTS MATERIA (CODIGO VARCHAR(6), NOMBRE_MATERIA VARCHAR(15))"
        self._cCursorSql.execute(self._sentencia)
        #table 5
        self._sentencia = '''CREATE TABLE IF NOT EXISTS CALIFICACIONES (ID_CALIFICACION INTEGER PRIMARY KEY AUTOINCREMENT, ID_ESTUDIANTE INTEGER, 
            ID_MATERIA VARCHAR(6), PRACTICA1 INT, PRACTICA2 INT, FORO1 INT, FORO2 INT, PRIMER_PARCIAL INT, SEGUNDO_PARCIAL INT, EXAMEN_FINAL INT,
            FOREIGN KEY(ID_ESTUDIANTE) REFERENCES ESTUDIANTE(ID_ESTUDIANTE),
            FOREIGN KEY(ID_MATERIA) REFERENCES MATERIA(CODIGO))'''
        self._cCursorSql.execute(self._sentencia)
        self._cConnect.commit()
        #data1
        self._data=[(1, 'Santo Domingo', '18.47186','-69.89232'),
             (2, 'Santiago de los Caballeros', '19.4517','-70.69703'),
             (3, 'Santo Domingo Oeste', '18.5','-70'),
             (4, 'Santo Domingo Este', '18.48847','-69.85707'),
             (5, 'San Pedro de Macorís', '18.4539','-69.30864'),
             (6, 'La Romana', '18.42733','-68.97285'),
             (7, 'San Cristóbal', '18.41667','-70.1'),
             (8, 'Puerto Plata', '19.79344','-70.6884'),
             (9, 'Bonao', '18.93687','-70.40923'),
             (10, 'San Juan de la Maguana.	18.80588', '-71.22991','$3'),
             (11, 'Baní', '18.27964','-70.33185'),
             (12, 'Mao', '19.55186','-71.07813'),
             (13, 'Moca', '19.39352','-70.52598'),
             (14, 'Salcedo', '19.37762','-70.41762'),
             (15, 'Azua', '18.45319','-70.7349'),
             (16, 'Bella Vista', '18.45539','-69.9454'),
             (17, 'Cotuí', '19.05272','-70.14939'),
             (18, 'Nagua', '19.3832','-69.8474'),
             (19, 'Dajabón', '19.54878','-71.70829'),
             (20, 'Sabaneta', '19.47793','-71.34125')]
        if(len(self.consultar('PROVINCIA'))==0):
            self.insert(self._data,'PROVINCIA',4)
        #data 2
        self._data=[
            (1, 'Ingeniería eléctrica'),
            (2, 'Ingeniería electrónica'),
            (3, 'Ingeniería de sistemas de computación'),
            (4, 'Ingeniería de software'),
            (5, 'Ingeniería industrial'),
            (6, 'Licenciatura en administración de empresas'),
            (7, 'Licenciatura en administración turística y hotelera'),
            (8, 'Licenciatura en comunicación digital'),
            (9, 'Licenciatura en contabilidad'),
            (10, 'Licenciatura en derecho'),
            (11, 'Licenciatura en diseño de interiores'),
            (12, 'Licenciatura en diseño gráfico'),
            (13, 'Licenciatura en finanzas')]
        if(len(self.consultar('CARRERA'))==0):
            self.insert(self._data,'CARRERA',2)
    #end method

    def insert(self, varios, tabla, n):
        if self.exist(varios[0][0], tabla):
            return self.update(varios, tabla) #ready
        else:
            try:
                self._sentencia=f"INSERT INTO {tabla} VALUES ({self.limit(n)})"
                self._cCursorSql.executemany(self._sentencia, varios)
                self._cConnect.commit()
                return 'insertado'
            except:
                return 'Error'
        #end condition
    #end methhod

    def update(self, varios, tabla):
        if tabla =="ESTUDIANTE":
            self._sentencia=f'''UPDATE {tabla}
                    SET MATRICULA = {varios[0][0]} ,
                        NOMBRE = '{varios[0][2]}' ,
                        APELLIDO = '{varios[0][3]}',
                        CEDULA = '{varios[0][4]}',
                        FOTO = '{varios[0][5]}',
                        SEXO = '{varios[0][6]}',
                        PROVINCIA = '{varios[0][7]}',
                        CARRERA = '{varios[0][8]}'
                    WHERE ID_ESTUDIANTE = {varios[0][0]}'''
        elif tabla=="MATERIA":
            self._sentencia=f'''UPDATE {tabla}
                    SET  NOMBRE_MATERIA = '{varios[0][1]}'
                    WHERE CODIGO = "{varios[0][0]}"'''
        elif tabla=="CALIFICACIONES":
            self._sentencia=f'''UPDATE {tabla}
                    SET ID_ESTUDIANTE ={varios[0][1]},
                        ID_MATERIA = '{varios[0][2]}' ,
                        PRACTICA1 = {varios[0][3]} ,
                        PRACTICA2 = {varios[0][4]} ,
                        FORO1 = {varios[0][5]} ,
                        FORO2 = {varios[0][6]} ,
                        PRIMER_PARCIAL = {varios[0][7]} ,
                        SEGUNDO_PARCIAL = {varios[0][8]} ,
                        EXAMEN_FINAL = {varios[0][9]}
                    WHERE ID_CALIFICACION = {varios[0][0]}'''
        #end condition
        try:
            self._cCursorSql.execute(self._sentencia)
            self._cConnect.commit()
            return "editado"
        except:
            return "error"
        #end try
    #end method

    def calificacionByEstudiante(self, idestudiante):
        self._sentencia = f"select * from 'CALIFICACIONES' WHERE ID_ESTUDIANTE ={idestudiante}"
        return self._cCursorSql.execute(self._sentencia).fetchall()
    #end method

    def mapaData(self, values):
        self._sentencia=f"""SELECT * from PROVINCIA inner join ESTUDIANTE
        on PROVINCIA.DESCRIPCION=ESTUDIANTE.PROVINCIA
        inner join CALIFICACIONES 
        on CALIFICACIONES.ID_ESTUDIANTE=ESTUDIANTE.ID_ESTUDIANTE
        inner join MATERIA
        on MATERIA.CODIGO=CALIFICACIONES.ID_MATERIA
        WHERE MATERIA.CODIGO='{values[0]}' AND PROVINCIA.DESCRIPCION='{values[1]}'"""
        return self._cCursorSql.execute(self._sentencia).fetchall()
    #end method

    def estudianteByCarrera(self):
        self._sentencia="""SELECT count(*) AS total, C.DESCRIPCION AS carrera FROM ESTUDIANTE  as E
            inner join CARRERA as C
            on E.CARRERA=C.DESCRIPCION
            GROUP by C.DESCRIPCION"""
        return self._cCursorSql.execute(self._sentencia).fetchall()
    #end method

    def literalesByProvincia(self):
        self._sentencia="""SELECT C.*, P.DESCRIPCION as PROVINCIA from ESTUDIANTE AS E
            inner join CALIFICACIONES AS C
            on C.ID_ESTUDIANTE=E.ID_ESTUDIANTE
            INNER JOIN PROVINCIA AS P
            ON P.DESCRIPCION=E.PROVINCIA"""
        return self._cCursorSql.execute(self._sentencia).fetchall()
    #end method
    
    def sacarMateria(self):
        self._sentencia="""SELECT C.*, P.DESCRIPCION as PROVINCIA, M.NOMBRE_MATERIA from ESTUDIANTE AS E
            inner join CALIFICACIONES AS C
            on C.ID_ESTUDIANTE=E.ID_ESTUDIANTE
            INNER JOIN PROVINCIA AS P
            ON P.DESCRIPCION=E.PROVINCIA 
            inner join Materia as m
            on M.CODIGO = C.ID_MATERIA"""
        return self._cCursorSql.execute(self._sentencia).fetchall()
    #end method

    def consultar(self, tabla):
        self._sentencia = f"select * from '{tabla}'"
        return self._cCursorSql.execute(self._sentencia).fetchall()
    #end method

    def consultarById(self, tabla, field, id):
        self._sentencia = f"select * from '{tabla}' where {field}={id}" if(tabla!='MATERIA') else f"select * FROM {tabla} WHERE {field}='{id}'"
        return self._cCursorSql.execute(self._sentencia).fetchone()
    #end method

    def delete(self,_id, tabla, field):
        if _id!="":
            try:
                self._sentencia=f"DELETE FROM {tabla} WHERE {field}={_id}" if(tabla!='MATERIA') else f"DELETE FROM {tabla} WHERE {field}='{_id}'"
                print(self._sentencia)
                self._cCursorSql.execute(self._sentencia)
                self._cConnect.commit()
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
        self._sentencia = """PRAGMA table_info({});""".format(tabla)
        return self._cCursorSql.execute(self._sentencia)
    #end method

    def exist(self, value, tabla):
        if tabla =="ESTUDIANTE":
            self._sentencia= f"select * from '{tabla}' where ID_ESTUDIANTE={value}"
            dataTable = self._cCursorSql.execute(self._sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
        elif tabla=="MATERIA":
            self._sentencia= f"select * from '{tabla}' where CODIGO='{value}'"
            dataTable = self._cCursorSql.execute(self._sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
        elif tabla=="CALIFICACIONES":
            self._sentencia= f"select * from '{tabla}' where ID_CALIFICACION={value}"
            dataTable = self._cCursorSql.execute(self._sentencia).fetchone()
            return True if(type(dataTable) is tuple) else False
#end method
#end class