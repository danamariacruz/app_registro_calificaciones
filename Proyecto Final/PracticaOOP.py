from tkinter import Tk, Label, Button
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
import webbrowser
from datetime import date 
from Data import Data
from InsertarRegistro import *

class MyProgram:
  

    def __init__(self, master):
        self.database = Data()
        self.master = master
        master.title("Sistema de Estudiantes")
        self.menubar = Menu(master)
        self.router_tree_view = ttk.Treeview(self.master)
        # self.router_tree_view.bind("<Double-1>", self.itemEvent)
        # self.router_tree_view.bind("<<TreeviewSelect>>", self.tableItemClick)
        #menu 1
        self.estudiantesmenu = Menu(self.menubar, tearoff=0)
        self.estudiantesmenu.add_command(label="Consultar", command=lambda:self.consultar("ESTUDIANTE"))
        self.estudiantesmenu.add_command(label="Modificar", command=lambda:self.estudianteControl())
        self.menubar.add_cascade(label="Estudiantes", menu=self.estudiantesmenu)
        #menu 2
        self.materiasmenu = Menu(self.menubar, tearoff=0)
        self.materiasmenu.add_command(label="Consultar", command=lambda:self.consultar("MATERIA"))
        self.materiasmenu.add_command(label="Modificar", command=lambda:self.materiaControl())
        self.menubar.add_cascade(label="Materias", menu=self.materiasmenu)
        #menu 3
        self.calificacionesmenu = Menu(self.menubar, tearoff=0)
        self.calificacionesmenu.add_command(label="Consultar", command=lambda:self.consultar("CALIFICACIONES"))
        self.calificacionesmenu.add_command(label="Modificar", command=lambda:self.calificacionControl())
        self.menubar.add_cascade(label="Calificaciones", menu=self.calificacionesmenu)
        master.config(menu=self.menubar)
        master.geometry("400x300")
        # self.label = Label(master, text="This is our first GUI!")
        # self.label.pack()

        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()
    #end _init

    def materiaControl(self):
        codigo = StringVar()
        nombre = StringVar()
        ist = InsertarRegistro()
        filewin = Toplevel(self.master) 
        Label(filewin,text = "Codigo").place(x=10, y=30)
        Label(filewin,text = "Nombre").place(x=10, y=60)
        
        TxtBoxCodigo=Entry(filewin, width=20, textvariable=codigo).place(x=100,y=30)
        TxtBoxNombre=Entry(filewin, width=20, textvariable=nombre).place(x=100,y=60)
        
        botonInsertar=Button(filewin, text = "Insertar", width= 14, command= lambda:ist.insertarM(codigo.get(),nombre.get())).place(x=10, y=120)
        botonModificar=Button(filewin, text = "Modificar", width= 14).place(x=120, y=120)
        botonBorrar=Button(filewin, text = "Borrar", width= 14,command=lambda:self.greet()).place(x=60, y=160)

        filewin.geometry("250x200")
        filewin.mainloop()
    #end method

    def estudianteControl(self):
        mat = StringVar()
        nom = StringVar()
        sex = StringVar()
        ist = InsertarRegistro()
        filewin = Toplevel(self.master)
        Label(filewin,text = "Matricula").place(x=10, y=30)
        Label(filewin,text = "Nombre").place(x=10, y=60)
        Label(filewin,text = "Sexo").place(x=10, y=90)
        
        TxtBoxMatricula=Entry(filewin, width=20, textvariable=mat).place(x=100,y=30)
        TxtBoxNombre=Entry(filewin, width=20, textvariable=nom).place(x=100,y=60)
        TxtBoxSexo=Entry(filewin, width=20, textvariable=sex).place(x=100,y=90)
        
        botonInsertar=Button(filewin, text = "Insertar", width= 14, command= lambda:ist.insertarE(mat.get(),nom.get(),sex.get())).place(x=10, y=120)
        botonModificar=Button(filewin, text = "Modificar", width= 14,).place(x=120, y=120)
        botonBorrar=Button(filewin, text = "Borrar", width= 14, command= lambda:self.greet()).place(x=60, y=160)

        filewin.geometry("250x200")
        filewin.mainloop()
    #end method   

    def calificacionControl(self):
        idEstudiante = StringVar()
        idMateria = StringVar()
        practica1 = StringVar()
        practica2 = StringVar()
        foro1 = StringVar()
        foro2 = StringVar()
        primerParcial = StringVar()
        segundoParcial = StringVar()
        examenFinal = StringVar()
        ist = InsertarRegistro()
        filewin = Toplevel(self.master)
        Label(filewin,text = "Estudiante").place(x=10, y=10)
        Label(filewin,text = "Materia").place(x=260, y=10)
        Label(filewin,text = "Practica1").place(x=10, y=30)
        Label(filewin,text = "Practica2").place(x=10, y=50)
        Label(filewin,text = "Foro1").place(x=260, y=30)
        Label(filewin,text = "Foro2").place(x=260, y=50)
        Label(filewin,text = "Primer Parcial").place(x=10, y=70)
        Label(filewin,text = "Segundo Parcial").place(x=10, y=90)
        Label(filewin,text = "Examen Final").place(x=260, y=70)
        
        TxtBoxEstudiante=Entry(filewin, width=20, textvariable=idEstudiante).place(x=100,y=10)
        TxtBoxMateria1=Entry(filewin, width=20, textvariable=idMateria).place(x=350,y=10)
        TxtBoxPractica1=Entry(filewin, width=20, textvariable=practica1).place(x=100,y=30)
        TxtBoxPractica2=Entry(filewin, width=20, textvariable=practica2).place(x=100,y=50)
        TxtBoxForo1=Entry(filewin, width=20, textvariable=foro1).place(x=350,y=30)
        TxtBoxForo2=Entry(filewin, width=20, textvariable=foro2).place(x=350,y=50)
        TxtBoxPrimerParcial=Entry(filewin, width=20, textvariable=primerParcial).place(x=100,y=70)
        TxtBoxSegundoParcial=Entry(filewin, width=20, textvariable=segundoParcial).place(x=100,y=90)
        TxtBoxExamenfinal=Entry(filewin, width=20, textvariable=examenFinal).place(x=350,y=70)
        
        botonInsertar=Button(filewin, text = "Insertar", width= 14, command= lambda:ist.insertarC(idEstudiante.get(),idMateria.get(),practica1.get(), practica2.get(), foro1.get(), foro2.get(), primerParcial.get(), segundoParcial.get(), examenFinal.get())).place(x=100, y=120)
        botonModificar=Button(filewin, text = "Modificar", width= 14,).place(x=260, y=120)
        botonBorrar=Button(filewin, text = "Borrar", width= 14,command= lambda:self.greet()).place(x=180, y=160)

        filewin.geometry("480x200")
        filewin.mainloop()  
    #end method

    def consultar(self, tabla):
        print(tabla)
        filewin = Toplevel(self.master)
        frame_router = Frame(filewin)
        frame_router.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)
        infoTabla = self.database.infotabla(tabla)
        buscartabla=[]
        for campo in infoTabla:
            buscartabla.append(campo[1])
        #end for
        dataTable = self.database.consultar(tabla) 
        # print(dataTable[0][0])
        columns = buscartabla
        self.router_tree_view = Treeview(frame_router, columns=columns, show="headings")
        self.router_tree_view.bind("<Double-1>", self.itemEvent)
        self.router_tree_view.column(buscartabla[0], width=100)
        for col in columns[0:]:
            self.router_tree_view.column(col, width=120)
            self.router_tree_view.heading(col, text=col)
        #end for
        print(dataTable)
        if type(dataTable) is list:
            i=0
            for data in dataTable:
                self.router_tree_view.insert(parent='',index='end', iid=self.dinamyFill(tabla, data)[0], values = self.dinamyFill(tabla, data))
                i=i+1
        #end for
        self.router_tree_view.pack(side="left", fill="y")
        scrollbar = Scrollbar(frame_router, orient='vertical')
        scrollbar.configure(command=self.router_tree_view.yview)
        scrollbar.pack(side="right", fill="y")
        self.router_tree_view.config(yscrollcommand=scrollbar.set)
        filewin.geometry("400x300")
        filewin.mainloop()
    #end method
      

    def dinamyFill(self, tabla, data):
        if tabla =="ESTUDIANTE":
            return (data[0], data[1], data[2], data[3])
        elif tabla=="MATERIA":
            return (data[0], data[1])
        elif tabla=="CALIFICACIONES":
            return (data[0], data[1], data[2], data[3],data[4],data[5],data[6],data[7],data[8],data[9])
    #end method

    def itemEvent(self, item):
        item = self.router_tree_view.selection()#[0] # now you got the item on that tree
        print("you clicked on id", item[0])
    #end method

    def greet(self):        
        print("Greetings!")
    #end methhod
#end class

root = Tk()
my_gui = MyProgram(root)
root.mainloop()