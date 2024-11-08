import tkinter as Tk
from tkinter import Button, Entry, Frame, Label, StringVar, Toplevel, messagebox, Tk, Radiobutton
from tkinter.ttk import Treeview

clientes = [["Franco Avendaño", 4, "Con Reserva"], ["Logan", 2, "Sin Reserva"]]
raiz = Tk()
raiz.title("Reservaciones")
raiz.resizable(0,0)
raiz.geometry("600x400")

opciones_frame = Frame(raiz)
opciones_frame.pack()
listado_frame = Frame(raiz)
listado_frame.pack()

def agregar_reservacion():
    def aceptar_modal():
        valor = nombre.get()
        print(opcion.get())
        if valor:
            nuevoCliente = [nombre.get(), cantidad_personas.get(), opcion.get()]
            
            if nuevoCliente[2] == "Con Reserva":
                i = 0
                while i < len(clientes) and clientes[i][2] == "Con Reserva":
                    i +=1
                    
                clientes.insert(i, nuevoCliente)
                tabla.insert(parent='',index=i,values=(nuevoCliente[0],nuevoCliente[1],nuevoCliente[2]))
            else:
                clientes.append(nuevoCliente)
                tabla.insert(parent='',index="end",values=(nuevoCliente[0],nuevoCliente[1],nuevoCliente[2]))

            modal.destroy()
            messagebox.showinfo("Valor ingresado", "La reservacion se realizo con exito")
            
        else:
            messagebox.showinfo("Advertencia", "Por favor ingresa un valor.")
        
        
    modal = Toplevel(opciones_frame)
    modal.title("Agregar Reservacion")
    modal.resizable(0,0)
    modal.geometry("300x250")
    modal.grab_set()
    modal.protocol("WM_DELETE_WINDOW", lambda: None)
    
    
    
    label_nombre = Label(modal,text="Nombre:")
    label_nombre.grid(column=0,row=0, ipady=10)
    
    nombre = Entry(modal)
    nombre.grid(column=1,row=0)
    
    label_personas = Label(modal,text="Cantidad de Personas")
    label_personas.grid(column=0,row=1,ipady=10)
    
    cantidad_personas = Entry(modal)
    cantidad_personas.grid(column=1,row=1)
    
    
    selecionar_opcion = Label(modal, text="Seleccione una Opcion")
    selecionar_opcion.grid(column=0, row=2,ipady=10)
    
    # Variable para almacenar la opción seleccionada
    opcion = StringVar(value="")  # Valor inicial vacío
    opciones = ["Con Reserva", "Sin Reserva"]
    for i,texto in enumerate(opciones):
        opciones_reserva = Radiobutton(modal,text=texto,variable=opcion,value=texto)
        opciones_reserva.grid(column=1,row=i+2)
        
    
    boton_modal_cancelar = Button(modal,text="Cancelar", command=modal.destroy,width=15)
    boton_modal_cancelar.grid(column=0,row=5,pady=25,padx=20)
    
    boton_modal_aceptar = Button(modal, text="Aceptar", command=aceptar_modal,width=15)
    boton_modal_aceptar.grid(column=1,row=5,pady=25)
    

mesas = [
    {"id": 1, "capacidad": 2, "ocupado": False},
    {"id": 2, "capacidad": 2, "ocupado": False},
    {"id": 3, "capacidad": 2, "ocupado": False},
    {"id": 4, "capacidad": 3, "ocupado": False},
    {"id": 5, "capacidad": 3, "ocupado": False},
    {"id": 6, "capacidad": 3, "ocupado": False},
    {"id": 7, "capacidad": 4, "ocupado": False},
    {"id": 8, "capacidad": 4, "ocupado": False},
    {"id": 9, "capacidad": 4, "ocupado": False},
    {"id": 10, "capacidad": 5, "ocupado": False},
    {"id": 11, "capacidad": 5, "ocupado": False},
    {"id": 12, "capacidad": 5, "ocupado": False},
]

def atender_cliente():
    if clientes:
        cliente = clientes.pop(0)
        for mesa in mesas:
            if not mesa["ocupado"] and mesa["capacidad"] >= cliente[1]:
                mesa["ocupado"] = True
                messagebox.showinfo("Mesa asignada",f"Mesa {mesa["id"]} asignada a {cliente[0]}")
                for usuario in tabla.get_children():
                    if tabla.item(usuario)["values"][0] == cliente[0]:
                        tabla.delete(usuario)
                        break
                return
        messagebox.showinfo("Sin mesas","No hay mesas disponibles para el cliente actual.")
    else:
        messagebox.showinfo("Sin clientes","No hay clientes en la lista de espera.")

def buscar_reservacion():
    pass

def cancelar_reservacion():
    pass

def modificar_reservacion():
    pass


# UI PRINCIPAL
boton_agregar = Button(opciones_frame,text="Agregar Reservacion", command=agregar_reservacion)
boton_agregar.grid(column=0,row=0)
#boton_agregar.pack(pady=10)

boton_atender = Button(opciones_frame,text="Atender Cliente", command=atender_cliente)
boton_atender.grid(column=1,row=0)
#boton_atender.pack(pady=10)

boton_buscar = Button(opciones_frame,text="Buscar Reservacion")
boton_buscar.grid(column=2,row=0)
#boton_buscar.pack(pady=10)


tabla = Treeview(listado_frame,columns=('Nombre', 'Cantidad Clientes', 'Tipo Reserva'),show='headings')
tabla.heading('Nombre', text="Nombre")
tabla.heading('Cantidad Clientes',text='Cantidad Clientes')
tabla.heading('Tipo Reserva',text='Tipo Reserva')
tabla.pack(fill='both',expand=True)

for i in range(len(clientes)):
    
    tabla.insert(parent='',index="end",values=(clientes[i][0],clientes[i][1],clientes[i][2]))
"""
# LISTADO
fila = 1
for i, cliente in enumerate(clientes):
    columna = 0
    for j, dato in enumerate(cliente):
        label_cliente = Label(raiz,text=dato)
        label_cliente.grid(column=columna,row=fila)
        columna += 1
    boton_cancelar = Button(text="Cancelar Reservacion")
    boton_cancelar.grid(column=columna,row=fila)
    fila += 1
    
boton_cancelar = Button(text="Cancelar Reservacion", height=2, width=25)
#boton_cancelar.pack(pady=10)

boton_modificar = Button(text="Modificar Reservacion", height=2, width=25)
#boton_modificar.pack(pady=10)
"""
raiz.mainloop()