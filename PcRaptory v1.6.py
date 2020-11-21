import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import psycopg2
#conexcion--------------------------------------
def sqlConnection():
    con = psycopg2.connect("host='localhost' user='postgres' password='' dbname=''")
    return con

#ventana de registro-------------------------------------------------------------------------------------
def registro():
    registro_usuario=tk.Tk()
    registro_usuario.title("Registro")
    registro_usuario.geometry('900x400')
    registro_usuario.resizable(0,0)
    registro_usuario['bg']='#32cd32'
    nombre=tk.Label(registro_usuario,text="Nombre",font=50)
    nombre.place(x=100,y=20)
    nombre_entrada=tk.Entry(registro_usuario,width=50)
    nombre_entrada.place(x=100,y=40,height=25)

    apellido=tk.Label(registro_usuario,text="Apellido",font=50)
    apellido.place(x=500,y=20)
    apellido_entrada=tk.Entry(registro_usuario,width=50)
    apellido_entrada.place(x=500,y=40,height=25)

    email=tk.Label(registro_usuario,text="Email",font=50)
    email.place(x=100,y=80)
    email_entrada=tk.Entry(registro_usuario,width=50)
    email_entrada.place(x=100,y=100,height=25)

    confirma_email=tk.Label(registro_usuario,text="confirma email",font=50)
    confirma_email.place(x=500,y=80)
    confirma_email_entrada=tk.Entry(registro_usuario,width=50)
    confirma_email_entrada.place(x=500,y=100,height=25)

    rut=tk.Label(registro_usuario,text="Rut",font=50)
    rut.place(x=100,y=140)
    rut_entrada=tk.Entry(registro_usuario,width=50)
    rut_entrada.place(x=100,y=160,height=25)

    telefono=tk.Label(registro_usuario,text="Telefono fijo o celular",font=50)
    telefono.place(x=500,y=140)
    telefono_entrada=tk.Entry(registro_usuario,width=50)
    telefono_entrada.place(x=500,y=160,height=25)

    contraseña=tk.Label(registro_usuario,text="Contraseña",font=50)
    contraseña.place(x=100,y=210)
    contraseña_entrada=tk.Entry(registro_usuario,width=50)
    contraseña_entrada.place(x=100,y=230,height=25)

    confirmar_contraeña=tk.Label(registro_usuario,text="Confirma contraseña",font=50)
    confirmar_contraeña.place(x=500,y=210)
    confirma_contraeña_entrada=tk.Entry(registro_usuario,width=50)
    confirma_contraeña_entrada.place(x=500,y=230,height=25)

    registrate=tk.Button(registro_usuario,text="Registrate",height=2, width=15,font=80)
    registrate.place(x=375,y=300)

    registro_usuario.mainloop()
#ventana de inicion sesion-------------------------------------------------------------------------------
def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()
#VENTANA "VERIFICACION DE LOGIN".
def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
    print("usuario: ",usuario1,"clave: ",clave1)
    if usuario1 == "admin@pcraptory.cl" and clave1=="admin":
        dueño()
    elif usuario1 == "vendedor@pcraptory.cl" and clave1 =="vendedor":
        vende_empl()
#carro de compra-----------------------------------------------------------------------------------------
def carro():
    carro=tk.Tk()
    carro.title("Carro de compra")
    carro.geometry('1000x500')
    carro.resizable(0,0)
    carro['bg']='#c3c3c3'

    tabla=ttk.Treeview(carro)
    tabla["columns"]=("id","dos","tres","cuatro")
    tabla["show"]="headings"
    tabla.heading("id",text="id")
    tabla.column("id",width=20)
    tabla.heading("dos",text="dos")
    tabla.column("dos",width=80)
    tabla.heading("tres",text="tres")
    tabla.column("tres",width=80)
    tabla.heading("cuatro",text="Cuatro")
    tabla.column("cuatro",width=80)
    tuples=[(1,"uno","uno.1","uno.2"),(2,"dos","dos.1","dos.2")]
    index=iid=0
    for row in tuples:
        tabla.insert("",index,iid,values=row)
        index=iid=index+1        
    tabla.place(x=10,y=50)

    numeroProductos=1 
    logo_detalle=tk.Button(carro,text="Logo", width=5, height=2)
    logo_detalle.place(x=10,y=10)    
    #item1=tk.Label(carro, text="Producto", width=18, height=11)
    #item1.place(x=10,y=60)
    #botonMas=tk.Button(item1, text="+", width=2, height=1)
    #botonMas.place(x=75, y=140)
    #botonMenos=tk.Button(item1, text="-", width=2, height=1)
    #botonMenos.place(x=15, y=140)
    numProdu=tk.Label( text=numeroProductos, width=2, height=1)
    numProdu.place(x=47, y=143)
    #numProdu=tk.Entry(item1, textvariable=numeroProductos)
    #numProdu.place(x=0, y=120)
    numProdu['bg']='#c3c3c3'
    frame_detalle=tk.Frame(carro,width=200, height=500)
    frame_detalle.pack(side="bottom",ancho="e")
    frame_detalle['bg']='#a2cadf'
    nombre1="Producto"
    valor1=300000
    valor2=200000
    valor3=100000
    total=valor1+valor2+valor3
    detalle_item1=tk.Label(frame_detalle,height=10, width=15,text=nombre1+"....... $"+str(valor1))
    detalle_item1.place(x=10, y=10, width=180, height=25)
    detalle_item1['bg']='#a2cadf'
    detalle_item2=tk.Label(frame_detalle,height=10, width=15,text=nombre1+"....... $"+str(valor2))
    detalle_item2.place(x=10, y=30, width=180, height=25)
    detalle_item2['bg']='#a2cadf'    
    detalle_item3=tk.Label(frame_detalle,height=10, width=15,text=nombre1+"....... $"+str(valor3))
    detalle_item3.place(x=10, y=50, width=180, height=25)
    detalle_item3['bg']='#a2cadf'    
    detalle_total=tk.Label(frame_detalle,height=10, width=15,text="-------------------------")
    detalle_total.place(x=10, y=70, width=180, height=25)
    detalle_total['bg']='#a2cadf'
    detalle_total1=tk.Label(frame_detalle,height=10, width=15,text="Total............... $"+str(total))
    detalle_total1.place(x=10, y=90, width=180, height=25)
    detalle_total1['bg']='#a2cadf'
    comprar=tk.Button(frame_detalle,text="Comprar")
    comprar.place(x=80,y=450)
    #segir=tk.Button(carro,text="Segir compra",command=seguimiento)
    #segir.place(x=450,y=450)
    carro.mainloop() 
#ventana de seguimiento----------------------------------------------------------------------------------
def seguimiento():
    seguimiento=tk.Tk()
    seguimiento.title("Seguimiento")
    seguimiento.geometry('1000x500')
    seguimiento.resizable(0,0)
    id_compra=tk.Label(seguimiento,text="Id de compra")
    id_compra.place(x=250,y=10)
    ingreso_id_compra=tk.Entry(seguimiento,width=50)
    ingreso_id_compra.place(x=350,y=10,height=25)
    busqueda=tk.Button(seguimiento,text="Imagen pendiemte de busqueda")
    busqueda.place(x=660,y=10)
    frame_seguimiento=tk.Frame(seguimiento,width=1000,height=450)
    frame_seguimiento.pack(side="bottom",ancho="s")
    frame_seguimiento['bg']='#d53032'
    progreso=tk.Label(frame_seguimiento,text="Imagen de seguimiento pendiente")
    progreso.place(x=400,y=200)
    seguimiento.mainloop()
#Ventana de vendedor o empleado--------------------------------------------------------------------------
def vende_empl():
    ventana_vend_emp=tk.Tk()
    ventana_vend_emp.title("Vendedoer o empleado")
    ventana_vend_emp.geometry('1000x500')
    ventana_vend_emp.resizable(0,0)
    frame_perfil=tk.Frame(ventana_vend_emp,width=850,height=425)
    frame_perfil['bg']='#d53032'
    frame_progreso=tk.Frame(ventana_vend_emp,width=850,height=425)
    frame_progreso['bg']='#49b848'
    frame_venta=tk.Frame(ventana_vend_emp,width=850,height=425)
    frame_venta['bg']='#3f888f'
    frame_inventario=tk.Frame(ventana_vend_emp,width=850,height=425)
    frame_inventario['bg']='#3f888f'
    a=1000   
    x1=[1,2,3,4,5,6,7,8,9,10,11,12]
    y1=[10,25,42,12,25,14,10,2,3,8,11,12]
    x2=[1,2,3,4,5,6,7,8,9,10,11,12] 
    y2=[5,2,4,3,6,12,52,12,32,10,11,9]
    fig1=Figure(figsize=(5,4), dpi=100)
    fig1.add_subplot(111).bar(x1,y1)
    frame_graf1=FigureCanvasTkAgg(fig1,ventana_vend_emp)
    frame_graf1.draw()
    fig2=Figure(figsize=(5,4), dpi=100)
    fig2.add_subplot(111).bar(x2,y2)
    frame_graf2=FigureCanvasTkAgg(fig2,ventana_vend_emp)
    frame_graf2.draw()
    canvas=tk.Canvas(frame_progreso,width=850, height=425)
    if(a<50000):
        b='red'
    elif(a>=50000 and a<=250000):
        b='yellow'
    else:
        b='Green'

    canvas.create_oval(750, 250, 650, 150, fill=b)
    def grafica_dia():
        frame_progreso.pack_forget()
        frame_graf2.get_tk_widget().pack_forget()
        canvas.pack_forget()
        frame_graf1.get_tk_widget().pack(side="bottom",ancho="s")
    def grafica_mes():
        frame_progreso.pack_forget()
        frame_graf1.get_tk_widget().pack_forget()
        canvas.pack_forget()
        frame_graf2.get_tk_widget().pack(side="bottom",ancho="s")  
    def cont_perfil():
        retrato=tk.Label(frame_perfil,text="Imagen pendiente")
        retrato.place(x=350,y=50)
        nombre=tk.Label(frame_perfil,text="Nombre: Juanito perez")
        nombre.place(x=350,y=100)
        cargo=tk.Label(frame_perfil,text="Cargo: Gerente de ventas")
        cargo.place(x=350,y=150)
        antiguedad=tk.Label(frame_perfil,text="Antiguedad: 10 Años")
        antiguedad.place(x=350,y=200)
        edad=tk.Label(frame_perfil,text="Edad: 56 años")
        edad.place(x=350,y=250)
    def evento_agregar():
        producto1=tk.Label(frame_venta,text="Producto agregado a la lista de compra")
        producto1.place(x=10,y=10) 
        frame_venta.pack(side="bottom",ancho="se")
        frame_inventario.pack_forget()
    def tabla():
        tabla=ttk.Treeview(frame_inventario)
        frame_inventario.pack(side="bottom",ancho="se")
        frame_venta.pack_forget()
        tabla["columns"]=("uno","dos","tres")
        tabla["show"]="headings"
        tabla.heading("uno",text="uno")
        tabla.heading("dos",text="dos")
        tabla.heading("tres",text="tres")
        tuples=[(1,"uno","uno.1"),(2,"dos","dos.1")]
        index=iid=0
        for row in tuples:
            tabla.insert("",index,iid,values=row)
            index=iid=index+1
        
        tabla.place(x=125,y=50)

    invertario=tk.Button(ventana_vend_emp,text="Inventario",command=tabla)
    ventasxdia=tk.Button(ventana_vend_emp,text="Ventas del mes",command=grafica_dia)
    ventasxmes=tk.Button(ventana_vend_emp,text="Ventas del año",command=grafica_mes)
    agregar=tk.Button(ventana_vend_emp,text="Agregar producto",command=evento_agregar)

    def prefil():        
        cont_perfil()
        frame_progreso.pack_forget()
        frame_venta.pack_forget()
        frame_perfil.pack(side="bottom",ancho="se")
        frame_graf2.get_tk_widget().pack_forget()  
        frame_graf1.get_tk_widget().pack_forget() 
        invertario.place_forget()
        agregar.place_forget() 
        ventasxdia.place_forget()
        ventasxmes.place_forget()
    def progreso():
        frame_perfil.pack_forget()
        frame_venta.pack_forget()
        frame_progreso.pack(side="bottom",ancho="se") 
        canvas.pack()
        frame_graf1.get_tk_widget().pack_forget()
        frame_graf2.get_tk_widget().pack_forget()
        invertario.place_forget()  
        agregar.place_forget()
        ventasxdia.place(x=150,y=50) 
        ventasxmes.place(x=250,y=50)
    def ventas():
        frame_perfil.pack_forget()
        frame_progreso.pack_forget()
        frame_graf2.get_tk_widget().pack_forget()
        frame_graf1.get_tk_widget().pack_forget()
        frame_venta.pack(side="bottom",ancho="se")
        invertario.place(x=150,y=50)
        agregar.place(x=225,y=50)
        ventasxdia.place_forget()
        ventasxmes.place_forget()


 
    perfil=tk.Button(ventana_vend_emp,text="Perfil",command=prefil,height=3, width=10,font=50)
    perfil.place(x=25,y=100)

    progreso=tk.Button(ventana_vend_emp,text="Progreso",command=progreso,height=3, width=10,font=50)
    progreso.place(x=25,y=200)

    ventas=tk.Button(ventana_vend_emp,text="Ventas",command=ventas,height=3, width=10,font=50)
    ventas.place(x=25,y=300)
    c='Total de las ventas realizadas: ',a
    temporal_progreso=tk.Label(frame_progreso,text=c,font=50)
    temporal_progreso.place(x=350,y=200)

    ventana_vend_emp.mainloop()
#Dueño---------------------------------------------------------------------------------------------------
def dueño():
    ventana_dueño=tk.Tk()
    ventana_dueño.title("Administracion")
    ventana_dueño.geometry('1000x500')
    ventana_dueño.resizable(0,0)
    x1=[1,2,3,4,5,6,7,8,9,10,11,12]
    y1=[10,25,42,12,25,14,10,2,3,8,11,12]
    x2=[1,2,3,4,5,6,7,8,9,10,11,12] 
    y2=[5,2,4,3,6,12,52,12,32,10,11,9]
    proce=[5]
    ram=[12]
    refrigeracion=[5]
    grafica=[3]
    division=[5,12,5,3]
    actividad=['procesador','ram','Refrigeracion','tarjetas graficas']
    colores=['red','green','blue','pink']
    fig1=Figure(figsize=(5,4), dpi=100,)
    fig1.add_subplot(111).plot(x1,y1,label='2019')
    fig1.add_subplot(111).plot(x2,y2,label='2020')
    fig1.suptitle('Comparacion de ventas del año')
    fig1.legend()
    fig2=Figure(figsize=(5,4), dpi=100)
    fig2.add_subplot(111).pie(division,colors=colores,startangle=90,shadow=True,explode=(0.1,0,0,0), autopct='%1.1f%%')
    fig2.legend(actividad)
    fig3=Figure(figsize=(5,4), dpi=100)
    fig3.add_subplot(111).bar(x1,y1,label='inventario')
    fig3.legend()
    fig4=Figure(figsize=(5,4), dpi=100)
    fig4.add_subplot(111).bar(x1,y1,label='promedio Boletas')
    fig4.legend()

    #analisis 1------------------------------------------------------------
    frame_analisis1=FigureCanvasTkAgg(fig1,ventana_dueño)
    frame_analisis1.draw()
    mes=tk.Label(ventana_dueño,text="meses",font=50,bg="white")
    años=tk.Label(ventana_dueño,text="años",font=50,wraplength=1,bg="white")
    #frame_analisis1['bg']='#c9cc44'
    def analisis1():
        frame_analisis2.get_tk_widget().pack_forget()
        frame_analisis3.get_tk_widget().pack_forget()
        frame_analisis4.get_tk_widget().pack_forget()
        frame_analisis5.get_tk_widget().pack_forget()
        frame_analisis6.get_tk_widget().pack_forget()
        frame_registro.pack_forget()
        frame_analisis1.get_tk_widget().pack(side="bottom",ancho="s")
        mes.place(x=495,y=470)
        años.place(x=260,y=250)
    boton1=tk.Button(ventana_dueño,text="Ganancias por años",command=analisis1)
    boton1.place(x=10,y=60)
    #analisis2--------------------------------------------------------------
    frame_analisis2=FigureCanvasTkAgg(fig2,ventana_dueño)
    frame_analisis2.draw()
    #frame_analisis2['bg']='#30a815'
    def analisis2():
        frame_analisis1.get_tk_widget().pack_forget()
        frame_analisis3.get_tk_widget().pack_forget()
        frame_analisis4.get_tk_widget().pack_forget()
        frame_analisis5.get_tk_widget().pack_forget()
        frame_analisis6.get_tk_widget().pack_forget()
        frame_registro.pack_forget()
        frame_analisis2.get_tk_widget().pack(side="bottom",ancho="s")
    boton1=tk.Button(ventana_dueño,text="Productos mas vendidos",command=analisis2)
    boton1.place(x=130,y=60)
    #analisis3-------------------------------------------------------------
    frame_analisis3=FigureCanvasTkAgg(fig3,ventana_dueño)
    frame_analisis3.draw()
    #frame_analisis3['bg']='#7b180e'
    def analisis3():
        frame_analisis1.get_tk_widget().pack_forget()
        frame_analisis2.get_tk_widget().pack_forget()
        frame_analisis4.get_tk_widget().pack_forget()
        frame_analisis5.get_tk_widget().pack_forget()
        frame_analisis6.get_tk_widget().pack_forget()
        frame_registro.pack_forget()
        mes.place(x=495,y=470)
        años.place(x=260,y=250)
        frame_analisis3.get_tk_widget().pack (side="bottom",ancho="s")    
    boton1=tk.Button(ventana_dueño,text="Rotacion de inventario",command=analisis3)
    boton1.place(x=280,y=60)
    #analisis4------------------------------------------------------------
    frame_analisis4=FigureCanvasTkAgg(fig4,ventana_dueño)
    frame_analisis4.draw()
    #frame_analisis4['bg']='#3450b7'
    def analisis4():
        frame_analisis1.get_tk_widget().pack_forget()
        frame_analisis2.get_tk_widget().pack_forget()
        frame_analisis3.get_tk_widget().pack_forget()
        frame_analisis5.get_tk_widget().pack_forget()
        frame_analisis6.get_tk_widget().pack_forget()
        frame_registro.pack_forget()
        mes.place(x=495,y=470)
        años.place(x=260,y=250)
        frame_analisis4.get_tk_widget().pack(side="bottom",ancho="s")    
    boton1=tk.Button(ventana_dueño,text="Valor promedio de boletas",command=analisis4)
    boton1.place(x=420,y=60)
    #analisis5------------------------------------------------------------
    frame_analisis5=FigureCanvasTkAgg(fig1,ventana_dueño)
    frame_analisis5.draw()
    #frame_analisis5['bg']='#d3705a'
    def analisis5():
        frame_analisis1.get_tk_widget().pack_forget()
        frame_analisis2.get_tk_widget().pack_forget()
        frame_analisis3.get_tk_widget().pack_forget()
        frame_analisis4.get_tk_widget().pack_forget()
        frame_analisis6.get_tk_widget().pack_forget()
        frame_registro.pack_forget()
        frame_analisis5.get_tk_widget().pack(side="bottom",ancho="s")
    #boton1=tk.Button(ventana_dueño,text="ventas por categorias",command=analisis5)
    #boton1.place(x=340,y=60)
    #analisis6------------------------------------------------------------
    frame_analisis6=FigureCanvasTkAgg(fig2,ventana_dueño)
    frame_analisis6.draw()
    #frame_analisis6['bg']='#9c5f44'
    def analisis6():
        frame_analisis1.get_tk_widget().pack_forget()
        frame_analisis2.get_tk_widget().pack_forget()
        frame_analisis3.get_tk_widget().pack_forget()
        frame_analisis4.get_tk_widget().pack_forget()
        frame_analisis5.get_tk_widget().pack_forget()
        frame_registro.pack_forget()
        frame_analisis6.get_tk_widget().pack(side="bottom",ancho="s")
    #boton1=tk.Button(ventana_dueño,text="ganancias por producto",command=analisis6)
    #boton1.place(x=420,y=60)
    #Registro empleados---------------------------------------------------
    frame_registro=tk.Frame(ventana_dueño,width=850,height=380)
    frame_registro['bg']='#a2cadf'
    def seccion_registro():
        frame_analisis1.get_tk_widget().pack_forget()
        frame_analisis2.get_tk_widget().pack_forget()
        frame_analisis3.get_tk_widget().pack_forget()
        frame_analisis4.get_tk_widget().pack_forget()
        frame_analisis5.get_tk_widget().pack_forget()
        frame_analisis6.get_tk_widget().pack_forget()
        frame_registro.pack(side="bottom",ancho="s")
        nombre=tk.Label(frame_registro,text="Nombre")
        apellido=tk.Label(frame_registro,text="apellido")
        rut=tk.Label(frame_registro,text="rut")
        cargo=tk.Label(frame_registro,text="cargo")
        fecha_contratacion=tk.Label(frame_registro,text="fecha de contratacion")
        nombre.place(x=20,y=10)
        apellido.place(x=20,y=30)
        rut.place(x=20,y=50)
        cargo.place(x=20,y=70)
        fecha_contratacion.place(x=20,y=90)
        entrada_nombre=tk.Entry(frame_registro)
        entrada_apellido=tk.Entry(frame_registro)
        entrada_rut=tk.Entry(frame_registro)
        entrada_cargo=tk.Entry(frame_registro)
        entrada_fecha_contratacion=tk.Entry(frame_registro)
        entrada_nombre.place(x=200,y=10)
        entrada_apellido.place(x=200,y=30)
        entrada_rut.place(x=200,y=50)
        entrada_cargo.place(x=200,y=70)
        entrada_fecha_contratacion.place(x=200,y=90)
    boton1=tk.Button(ventana_dueño,text="registro",command=seccion_registro)
    boton1.place(x=580,y=60)
    ventana_dueño.mainloop()
#Ventana principal---------------------------------------------------------------------------------------
#conce = sqlConnection()

global ventana_principal
ventana_principal=tk.Tk()
ventana_principal.title("PcRaptory")
ventana_principal.geometry('1220x700')
ventana_principal.resizable(0,0)
ventana_principal['bg']='#a2cadf'

#logoFoto = PhotoImage(file=r"D:\titoo\Documents\Universidad Central\Semestre 2-20\Programacion de aplicaciones\Aplicacion\images\logo.png")
#logoFoto = logoFoto.subsample(2,3)
Logo=tk.Label(ventana_principal,text="PcRaptory")
Logo.place(x=0,y=10)
Logo['bg']= '#a2cadf'

boton_busqueda=tk.Button(ventana_principal,text="Busqueda")
boton_busqueda.place(x=800,y=10)
ingreso_texto_busqueda=tk.Entry(ventana_principal,width=50)
ingreso_texto_busqueda.place(x=490,y=10,height=25)

#fotocarro = PhotoImage(file=r"D:\titoo\Documents\Universidad Central\Semestre 2-20\Programacion de aplicaciones\Aplicacion\images\carro.png")
#fotocarro = fotocarro.subsample(15,15)
boton_carro=tk.Button(ventana_principal,command=carro)
boton_carro.place(x=950,y=10)

boton_inicio_sesion=tk.Button(ventana_principal,text="Inicio sesion",command=login)
boton_inicio_sesion.place(x=1120,y=10)
#frame-------------------------------------------------------
frame_item=tk.Frame(ventana_principal,width=1000,height=620)
frame_item.pack(side="bottom",ancho="se")
frame_item['bg']='#c3c3c3'
destacado=tk.Label(frame_item,text="Destacados",font=50)
destacado.place(x=470,y=0)
destacado['bg']='#c3c3c3'
nuevo=tk.Label(frame_item,text="Nuevos Productos",font=50)
nuevo.place(x=450,y=250)
nuevo['bg']='#c3c3c3'
#Botones----------------------------------------------------
#primera fila-----------------------------------------------

#proce = PhotoImage(file = r"D:\titoo\Documents\Universidad Central\Semestre 2-20\Programacion de aplicaciones\Aplicacion\images\proce.png")
#proce = proce.subsample(5,5)
boton_item1=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item1.place(x=20,y=50)
boton_item2=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item2.place(x=190,y=50)
boton_item3=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item3.place(x=360,y=50)
boton_item4=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item4.place(x=530,y=50)
boton_item5=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item5.place(x=700,y=50)
boton_item6=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item6.place(x=870,y=50)
#segunda fila----------------------------------------------
boton_item7=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item7.place(x=20,y=300)
boton_item8=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item8.place(x=190,y=300)
boton_item9=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item9.place(x=360,y=300)
boton_item10=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item10.place(x=530,y=300)
boton_item10=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item10.place(x=700,y=300)
boton_item10=tk.Button(frame_item,height=155, width=110,text="Imagen pendiente")
boton_item10.place(x=870,y=300)

for i in range(12):
    labelproducto = tk.Label(frame_item,text="Producto")
    if i < 6:
        labelproducto.place(x=20+(i%6)*170,y=220)
    else:
        labelproducto.place(x=20+(i%6)*170,y=470)
    labelproducto["bg"] = '#c3c3c3'

#filtros tipo arbol------------------------------------------
def rescatar_valor():
    # print(opcion1.get())
    # print(opcion2.get())
    # print(opcion3.get())
    for i in range(len(lst_cb_categorias)):
        print(lst_cb_categorias[i].get())
    print("------------------")
    for i in range(len(lst_cb_marcas)):
        print(lst_cb_marcas[i].get())
    print("------------------")
    for i in range(len(lst_cb_precio)):
        print(lst_cb_precio[i].get())
def reinicio():
    # opcion1.set(None)
    # opcion2.set(None)
    # opcion3.set(None)
    for i in range(len(lst_cb_categorias)):
        lst_cb_categorias[i].set(0)
    for i in range(len(lst_cb_marcas)):
        lst_cb_marcas[i].set(0)
    for i in range(len(lst_cb_precio)):
        lst_cb_precio[i].set(0)
def evento_boton():
    rescatar_valor()
    reinicio()

opcion1= IntVar()
opcion2= IntVar()
opcion3= IntVar()
lst_cb_categorias = list()
lst_cb_marcas = list()
lst_cb_precio = list()
for i in range(8):
    lst_cb_categorias.append(IntVar())
    lst_cb_marcas.append(IntVar())
    if i < 3:
        lst_cb_precio.append(IntVar())

categoria=tk.Label(ventana_principal,text="Categorias")
categoria.place(x=0,y=80)
categoria["bg"] = '#a2cadf'

radio=tk.Checkbutton(ventana_principal, text="Almacenamiento", variable=lst_cb_categorias[0],onvalue=1)
radio.place(x=30,y=120)
radio["bg"] = '#a2cadf'
radio2=tk.Checkbutton(ventana_principal, text="Fuente de Poder", variable=lst_cb_categorias[1],onvalue=2)
radio2.place(x=30,y=140)
radio2["bg"] = '#a2cadf'
radio3=tk.Checkbutton(ventana_principal, text="Gabinete", variable=lst_cb_categorias[2],onvalue=3)
radio3.place(x=30,y=160)
radio3["bg"] = '#a2cadf'
radio4=tk.Checkbutton(ventana_principal, text="Memoria", variable=lst_cb_categorias[3],onvalue=4)
radio4.place(x=30,y=180)
radio4["bg"] = '#a2cadf'
radio5=tk.Checkbutton(ventana_principal, text="Placa Madre", variable=lst_cb_categorias[4],onvalue=5)
radio5.place(x=30,y=200)
radio5["bg"] = '#a2cadf'
radio6=tk.Checkbutton(ventana_principal, text="Procesador", variable=lst_cb_categorias[5],onvalue=6)
radio6.place(x=30,y=220)
radio6["bg"] = '#a2cadf'
radio7=tk.Checkbutton(ventana_principal, text="Refrigeración", variable=lst_cb_categorias[6],onvalue=7)
radio7.place(x=30,y=240)
radio7["bg"] = '#a2cadf'
radio8=tk.Checkbutton(ventana_principal, text="Tarjeta Gráfica", variable=lst_cb_categorias[7],onvalue=8)
radio8.place(x=30,y=260)
radio8["bg"] = '#a2cadf'

marca=tk.Label(ventana_principal,text="Marcas")
marca.place(x=0,y=300)
marca["bg"] = '#a2cadf'
radio9=tk.Checkbutton(ventana_principal, text="Acer", variable=lst_cb_marcas[0],onvalue=1)
radio9.place(x=30,y=340)
radio9["bg"] = '#a2cadf'
radio10=tk.Checkbutton(ventana_principal, text="ASRock", variable=lst_cb_marcas[1],onvalue=2)
radio10.place(x=30,y=360)
radio10["bg"] = '#a2cadf'
radio11=tk.Checkbutton(ventana_principal, text="Asus", variable=lst_cb_marcas[2],onvalue=3)
radio11.place(x=30,y=380)
radio11["bg"] = '#a2cadf'
radio12=tk.Checkbutton(ventana_principal, text="Corsair", variable=lst_cb_marcas[3],onvalue=4)
radio12.place(x=30,y=400)
radio12["bg"] = '#a2cadf'
radio13=tk.Checkbutton(ventana_principal, text="Dell", variable=lst_cb_marcas[4],onvalue=5)
radio13.place(x=30,y=420)
radio13["bg"] = '#a2cadf'
radio14=tk.Checkbutton(ventana_principal, text="Gigabyte", variable=lst_cb_marcas[5],onvalue=6)
radio14.place(x=30,y=440)
radio14["bg"] = '#a2cadf'
radio15=tk.Checkbutton(ventana_principal, text="Msi", variable=lst_cb_marcas[6],onvalue=7)
radio15.place(x=30,y=460)
radio15["bg"] = '#a2cadf'
radio16=tk.Checkbutton(ventana_principal, text="Razer", variable=lst_cb_marcas[7],onvalue=8)
radio16.place(x=30,y=480)
radio16["bg"] = '#a2cadf'

precio=tk.Label(ventana_principal,text="Precios")
precio.place(x=0,y=520)
precio["bg"] = '#a2cadf'
radio17=tk.Checkbutton(ventana_principal, text="0 - 100.000", variable=lst_cb_precio[0],onvalue=1)
radio17.place(x=30,y=560)
radio17["bg"] = '#a2cadf'
radio18=tk.Checkbutton(ventana_principal, text="100.001 - 500.000", variable=lst_cb_precio[1],onvalue=2)
radio18.place(x=30,y=580)
radio18["bg"] = '#a2cadf'
radio19=tk.Checkbutton(ventana_principal, text="500.001 - 1.000.000", variable=lst_cb_precio[2],onvalue=3)
radio19.place(x=30,y=600)
radio19["bg"] = '#a2cadf'

boton=tk.Button(ventana_principal, text="Reiniciar",command=evento_boton)
boton.place(x=0,y=640)

ventana_principal.mainloop()
