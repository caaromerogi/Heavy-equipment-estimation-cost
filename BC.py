from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import math
import sqlite3


class Costos:
    #conexión con db
    db_name = 'Maquinaria.db'

    def __init__(self, root):
        #Inicializando la ventana raiz
        self.root = root
        self.root.title('Estimación de costos')
        width= self.root.winfo_screenwidth()
        height= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))


        #CREATING THE WINDOW
        nb = Notebook(self.root)

        #GENERAL DATABASE FRAME
        #Contenedor general
        contenedor0 = Frame(nb)
        contenedor0.pack(fill=BOTH, expand=True)

        #Empaquetar contenedor en notebook
        nb.add(contenedor0, text='Historico Maquinaria')
        
        #Creando canvas dentro de contenedor principal
        canvas0 = Canvas(contenedor0)
        canvas0.pack(side = LEFT, fill = BOTH, expand = True)

        #Creando la scrollbar para el canvas 
        scrollv0 = ttk.Scrollbar(contenedor0, orient = VERTICAL, command = canvas0.yview)
        scrollv0.pack(side = RIGHT, fill = Y)
        
        #Configurando canvas
        canvas0.config(yscrollcommand = scrollv0.set)
        canvas0.bind('<Configure>', lambda e: canvas0.bbox('all'))

        #Creando la ventana del canvas con otro frame
        frame_historico = Frame(canvas0)
        canvas0.create_window((1000,500), window = frame_historico)

        #EQUIPTMENT COSTS FRAME
        #Creando contenedor principal
        contenedor1 = Frame(nb)
        contenedor1.pack(fill=BOTH, expand=True)

        #Empaquetando contenendor en el notebook
        nb.add(contenedor1, text='Costos Maquinaria')

        #Creando el canvas dentro del contenedor principal
        canvas1 = Canvas(contenedor1)
        canvas1.pack(side = LEFT, fill = BOTH, expand = True)

        #Creando el scrollbar
        scrollv1 = Scrollbar(contenedor1, command = canvas1.yview)
        scrollv1.pack(side = RIGHT, fill = Y)

        #Configurando canvas para scrollbar
        canvas1.config(yscrollcommand = scrollv1.set, scrollregion = (0, 0, 100, 1000))
        
        #Creando la ventana con un nuevo frame
        frame_costos = Frame(canvas1)
        canvas1.create_window(1000, 500, window = frame_costos)
        
        #Empaquetando el notebook
        nb.pack(expand = 1, fill = "both")

        #GENERAL DATABASE WIDGETS
        self.lf_datos_historicos_maquinaria = LabelFrame(frame_historico, text = 'Ingreso de datos')
        self.lf_datos_historicos_maquinaria.grid(column = 0, row = 0, ipadx = 5)
        #títulos
        Label(self.lf_datos_historicos_maquinaria, text = 'Equipo: ').grid(column = 0, row = 0, sticky = W, pady = 4)
        self.equipo = Entry(self.lf_datos_historicos_maquinaria, width = 15)
        self.equipo.grid(column = 1, row = 0, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Vida Económica(años): ').grid(column = 0, row = 1, sticky = W, pady = 4)
        self.vida_economica = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.vida_economica.grid(column = 1, row = 1, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Tasa de seguro (%): ').grid(column = 0, row = 2, sticky = W, pady = 4)
        self.tasa_seguro = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.tasa_seguro.grid(column = 1, row = 2, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = '% de mantenimiento (%): ').grid(column = 0, row = 3, sticky = W, pady = 4)
        self.mantenimiento = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.mantenimiento.grid(column = 1, row = 3, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = '% de rescate (%): ').grid(column = 0, row = 4, sticky = W, pady = 4)
        self.rescate = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.rescate.grid(column = 1, row = 4, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Tasa de interés (%): ').grid(column = 0, row = 5, sticky = W, pady = 4)
        self.interes = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.interes.grid(column = 1, row = 5, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Consumo combustible (gal/hr): ').grid(column = 0, row = 6, sticky = W, pady = 4)
        self.consumo_combustible = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.consumo_combustible.grid(column = 1, row = 6, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Consumo lubricante carter (gal/hr): ').grid(column = 0, row = 7, sticky = W, pady = 4)
        self.consumo_lubricante_carter = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.consumo_lubricante_carter.grid(column = 1, row = 7, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Consumo lubricante hidráulico (gal/hr): ').grid(column = 0, row = 8, sticky = W, pady = 4)
        self.consumo_lubricante_hidraulico = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.consumo_lubricante_hidraulico.grid(column = 1, row = 8, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Consumo lubricante transmisión/mandos finales (gal/hr): ').grid(column = 0, row = 9, sticky = W, pady = 4)
        self.consumo_lubricante_transmision = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.consumo_lubricante_transmision.grid(column = 1, row = 9, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Tendido de llantas por hr (tendido/hr): ').grid(column = 0, row = 10, sticky = W, pady = 4)
        self.tendido_llantas = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.tendido_llantas.grid(column = 1, row = 10, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Capacidad del tanque (gal): ').grid(column = 0, row = 11, sticky = W, pady = 4)
        self.capacidad_tanque = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.capacidad_tanque.grid(column = 1, row = 11, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Tiempo de tanqueo (min): ').grid(column = 0, row = 12, sticky = W, pady = 4)
        self.tiempo_tanqueo = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.tiempo_tanqueo.grid(column = 1, row = 12, pady = 4, sticky = W)

        Label(self.lf_datos_historicos_maquinaria, text = 'Capacidad balde/carga (m3): ').grid(column = 0, row = 13, sticky = W, pady = 4)
        self.capacidad_carga = Entry(self.lf_datos_historicos_maquinaria, width = 12)
        self.capacidad_carga.grid(column = 1, row = 13, pady = 4, sticky = W)

        #Boton para adicionar los datos a la base de datos
        Button(self.lf_datos_historicos_maquinaria, text = 'Enviar', command = self.add_values).grid(column = 0, row = 14, columnspan = 2, pady = 5)

        #LABELFRAME TREEVIEW DATOS HISTORICOS MAQUINARIA
        self.lf_treeview_datos_historicos = LabelFrame(frame_historico)
        self.lf_treeview_datos_historicos.grid(column = 0, row = 1)


        #columnas del treeview
        columns = ['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11','#12', '#13', '#14', '#15']
        #Treeview
        self.treeview_datos_historicos = ttk.Treeview(self.lf_treeview_datos_historicos, columns = columns, show = 'headings', selectmode = 'browse')
        self.treeview_datos_historicos.grid(column = 0, row = 0, columnspan = 2, rowspan = 10, sticky = "nsew")

        #scrollbar x
        self.scrollbar_maquinariax = Scrollbar(self.lf_treeview_datos_historicos, orient = 'horizontal', command = self.treeview_datos_historicos.xview)
        self.scrollbar_maquinariax.grid(column = 0, row = 11, sticky = "nsew", columnspan = 2)

        self.treeview_datos_historicos.configure(xscrollcommand = self.scrollbar_maquinariax.set)

        #scrollbar y
        self.scrollbar_maquinariay = Scrollbar(self.lf_treeview_datos_historicos, orient = 'vertical', command = self.treeview_datos_historicos.yview)
        self.scrollbar_maquinariay.grid(column = 2, row = 1, sticky = "nsew", columnspan = 2, rowspan = 10)

        self.treeview_datos_historicos.configure(yscrollcommand = self.scrollbar_maquinariay.set)

        #headings
        self.treeview_datos_historicos.heading('#1', text = 'ID')
        self.treeview_datos_historicos.heading('#2', text = 'EQUIPO')
        self.treeview_datos_historicos.heading('#3', text = 'VIDA ECONÓMICA')
        self.treeview_datos_historicos.heading('#4', text = 'TASA DE SEGURO (%)')
        self.treeview_datos_historicos.heading('#5', text = '% DE MANTENIMIENTO')
        self.treeview_datos_historicos.heading('#6', text = '% DE RESCATE')
        self.treeview_datos_historicos.heading('#7', text = 'TASA DE INTERÉS')
        self.treeview_datos_historicos.heading('#8', text = 'CONSUMO COMBUSTIBLE (gal/hr)')
        self.treeview_datos_historicos.heading('#9', text = 'CONSUMO LUBRICANTE CARTER (gal/hr)')
        self.treeview_datos_historicos.heading('#10', text = 'CONSUMO LUBRICANTE HIDRÁULICO (gal/hr)')
        self.treeview_datos_historicos.heading('#11', text = 'CONSUMO LUBRICANTE TRANSMISIÓN (gal/hr)')
        self.treeview_datos_historicos.heading('#12', text = 'TENDIDO LLANTAS (tendido/hr)')
        self.treeview_datos_historicos.heading('#13', text = 'CAPACIDAD TANQUE (gal)')
        self.treeview_datos_historicos.heading('#14', text = 'TIEMPO DE TANQUEO (min)')
        self.treeview_datos_historicos.heading('#15', text = 'CAPACIDAD CARGA/BALDE (m3)')

        #tamaño de columnas
        self.treeview_datos_historicos.column('#1', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#2', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#3', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#4', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#5', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#6', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#7', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#8', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#9', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#10', anchor = CENTER, width = 75, minwidth = 270)
        self.treeview_datos_historicos.column('#11', anchor = CENTER, width = 75, minwidth = 270)
        self.treeview_datos_historicos.column('#12', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#13', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#14', anchor = CENTER, width = 75, minwidth = 250)
        self.treeview_datos_historicos.column('#15', anchor = CENTER, width = 75, minwidth = 250)
        
        #Columnas visibles
        self.treeview_datos_historicos['displaycolumns'] = ['#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11','#12', '#13', '#14', '#15']

        #Botón borrar
        Button(self.lf_treeview_datos_historicos, text = 'Borrar', command = self.pre_delete_values).grid(column = 0, row = 12, columnspan = 1, sticky = 'nsew')
        #Botón actualizar
        Button(self.lf_treeview_datos_historicos, text = 'Actualizar', command = self.actualizar_valores).grid(column = 1, row = 12, columnspan = 1, sticky = 'nsew')
        self.get_values()

        #lABELFRAME PARA LOS TIEMPOS
        self.lf_calculo_costos = LabelFrame(frame_costos, text = 'Información de la zona')
        self.lf_calculo_costos.grid(column = 0, row = 0)

        #COLUMNA 1
        #uso de disponibilidad
        Label(self.lf_calculo_costos, text = 'Uso de disponibilidad* (%): ').grid(column = 0, row = 0, pady = 4, padx = 5)
        self.uso_disponibilidad = Entry(self.lf_calculo_costos, width = 12)
        self.uso_disponibilidad.grid(column = 1, row = 0, pady = 4, padx = 5)

        #turno
        Label(self.lf_calculo_costos, text = 'Turno* (hr): ').grid(column = 0, row = 1, pady = 4, padx = 5)
        self.turno = Entry(self.lf_calculo_costos, width = 12)
        self.turno.grid(column = 1, row = 1, pady = 4, padx = 5)

        #horas lluvia
        Label(self.lf_calculo_costos, text = 'Horas lluvia* (hr): ').grid(column = 0, row = 2, pady = 4, padx = 5)
        self.horas_lluvia = Entry(self.lf_calculo_costos, width = 12)
        self.horas_lluvia.grid(column = 1, row = 2, pady = 4, padx = 5)

        #dias semana
        Label(self.lf_calculo_costos, text = 'Dias por semana* (días): ').grid(column = 0, row = 3, pady = 4, padx = 5)
        self.dias_semana = Entry(self.lf_calculo_costos, width = 12)
        self.dias_semana.grid(column = 1, row = 3, pady = 4, padx = 5)

        #dias no laborables
        Label(self.lf_calculo_costos, text = 'Dias no laborables* (días): ').grid(column = 0, row = 4, pady = 4, padx = 5)
        self.dias_no_laborables = Entry(self.lf_calculo_costos, width = 12)
        self.dias_no_laborables.grid(column = 1, row = 4, pady = 4, padx = 5)

        #Densidad suelta
        Label(self.lf_calculo_costos, text = 'Densidad suelta* (ton/m3): ').grid(column = 0, row = 5, pady = 4, padx = 5)
        self.densidad_suelta = Entry(self.lf_calculo_costos, width = 12)
        self.densidad_suelta.grid(column = 1, row = 5, pady = 4, padx = 5)


        #COLUMNA 2
        #tiempo de aculatamiento
        Label(self.lf_calculo_costos, text = 'Tiempo de aculatamiento* (s): ').grid(column = 2, row = 0, pady = 4, padx = 5)
        self.tiempo_aculatamiento = Entry(self.lf_calculo_costos, width = 12)
        self.tiempo_aculatamiento.grid(column = 3, row = 0, pady = 4, padx = 5)

        #tiempo de excavadora
        Label(self.lf_calculo_costos, text = 'Tiempo de ciclo cargador* (s): ').grid(column = 2, row = 1, pady = 4, padx = 5)
        self.tiempo_cargador = Entry(self.lf_calculo_costos, width = 12)
        self.tiempo_cargador.grid(column = 3, row = 1, pady = 4, padx = 5)

        #tiempo de descarga
        Label(self.lf_calculo_costos, text = 'Tiempo de descarga* (s): ').grid(column = 2, row = 2, pady = 4, padx = 5)
        self.tiempo_descarga = Entry(self.lf_calculo_costos, width = 12)
        self.tiempo_descarga.grid(column = 3, row = 2, pady = 4, padx = 5)

        #distancia de vía
        Label(self.lf_calculo_costos, text = 'Distancia de vía en un sentido* (m): ').grid(column = 2, row = 3, pady = 4, padx = 5)
        self.distancia_via = Entry(self.lf_calculo_costos, width = 12)
        self.distancia_via.grid(column = 3, row = 3, pady = 4, padx = 5)

        #velocidad vehículos cargados
        Label(self.lf_calculo_costos, text = 'Velocidad vehículo cargado* (km/hr): ').grid(column = 2, row = 4, pady = 4, padx = 5)
        self.velocidad_cargado = Entry(self.lf_calculo_costos, width = 12)
        self.velocidad_cargado.grid(column = 3, row = 4, pady = 4, padx = 5)

        #Velocidad descargado
        Label(self.lf_calculo_costos, text = 'Velocidad vehículo descargado* (km/hr): ').grid(column = 2, row = 5, pady = 4, padx = 5)
        self.velocidad_descargado = Entry(self.lf_calculo_costos, width = 12)
        self.velocidad_descargado.grid(column = 3, row = 5, pady = 4, padx = 5)


        #LABELFRAME COSTO DE COMBUSTIBLES Y LUBRICANTES
        self.lf_costo_combustible = LabelFrame(self.lf_calculo_costos, text = 'Diesel y Lubricantes')
        self.lf_costo_combustible.grid(column = 0, row = 6, columnspan = 4, sticky = 'nsew', pady = 10)

        #Diesel
        Label(self.lf_costo_combustible, text = 'Costo Diesel ($/gal): ').grid(column = 0, row = 0, pady = 5, padx = 5)
        self.costo_diesel = Entry(self.lf_costo_combustible, width = 12)
        self.costo_diesel.grid(column = 1, row = 0, pady = 5, padx = 5)

        #lubricante carter
        Label(self.lf_costo_combustible, text = 'Costo Lubricante Carter ($/gal): ').grid(column = 0, row = 1, pady = 5, padx = 5)
        self.costo_lubricante_carter = Entry(self.lf_costo_combustible, width = 12)
        self.costo_lubricante_carter.grid(column = 1, row = 1, pady = 5, padx = 5)

        #lubricante hidraulico
        Label(self.lf_costo_combustible, text = 'Costo Lubricante Hidráulico ($/gal): ').grid(column = 2, row = 0, pady = 5, padx = 5)
        self.costo_lubricante_hidraulico = Entry(self.lf_costo_combustible, width = 12)
        self.costo_lubricante_hidraulico.grid(column = 3, row = 0, pady = 5, padx = 5)

        #lubricante transmisión
        Label(self.lf_costo_combustible, text = 'Costo Lubricante Transmisión ($/gal): ').grid(column = 2, row = 1, pady = 5, padx = 5)
        self.costo_lubricante_transmision = Entry(self.lf_costo_combustible, width = 12)
        self.costo_lubricante_transmision.grid(column = 3, row = 1, pady = 5, padx = 5)

        #LABELFRAME EQUIPOS
        self.lf_equipos = LabelFrame(frame_costos, text = 'Equipos')
        self.lf_equipos.grid(column = 0, row = 1, pady = 10)

        #EQUIPO DE TANQUEO
        self.lf_equipo_tanqueo = LabelFrame(self.lf_equipos, text = 'EQUIPO DE TANQUEO')
        self.lf_equipo_tanqueo.grid(column = 0, row = 0, padx = 5, pady = 10, columnspan = 2)

        #seleccion equipo
        Label(self.lf_equipo_tanqueo, text = 'Equipo').grid(column = 0, row = 1, pady = (6, 0))
        self.combo_equipo_tanqueo = Combobox(self.lf_equipo_tanqueo, state = 'readonly', width = 16)
        self.combo_equipo_tanqueo.grid(column = 0, row = 2, pady = 3, padx = 3)
        #precio del equipo
        Label(self.lf_equipo_tanqueo, text = 'Precio equipo').grid(column = 1, row = 1, pady = (6,0))
        self.precio_equipo_tanqueo = Entry(self.lf_equipo_tanqueo, width = 16)
        self.precio_equipo_tanqueo.grid(column = 1, row = 2, pady = 3, padx = 3)
        #precio de las llantas
        Label(self.lf_equipo_tanqueo, text = 'Precio llantas').grid(column = 2, row = 1, pady = (6,0))
        self.precio_llantas_tanqueo = Entry(self.lf_equipo_tanqueo, width = 16)
        self.precio_llantas_tanqueo.grid(column = 2, row = 2, pady = 3, padx = 3)
        #Costo operador
        Label(self.lf_equipo_tanqueo, text = 'Costo operador/mes').grid(column = 3, row = 1, pady = (6,0))
        self.costo_operador_mes_tanqueo = Entry(self.lf_equipo_tanqueo, width = 16)
        self.costo_operador_mes_tanqueo.grid(column = 3, row = 2, pady = 3, padx = 3)
        #Disponibilidad mecanica
        Label(self.lf_equipo_tanqueo, text = 'D. mecánica (%)').grid(column = 4, row = 1, pady = (6,0))
        self.disponibilidad_mecanica_tanqueo = Entry(self.lf_equipo_tanqueo, width = 16)
        self.disponibilidad_mecanica_tanqueo.grid(column = 4, row = 2, pady = 3, padx = 3)

        #EQUIPO DE CARGA-ACARREO
        self.lf_equipo_carga = LabelFrame(self.lf_equipos, text = 'EQUIPOS CARGA - ACARREO')
        self.lf_equipo_carga.grid(column = 0, row = 1, sticky = W, padx = 5, pady = 5)

        #EQUIPO CARGADOR
        #seleccion equipo
        Label(self.lf_equipo_carga, text = 'Equipo Carga').grid(column = 0, row = 1, pady = (6, 0))
        self.combo_equipo_carga = Combobox(self.lf_equipo_carga, height = 6, state = 'readonly', width = 16)
        self.combo_equipo_carga.grid(column = 0, row = 2, pady = 3, padx = 3)
        #precio del equipo
        Label(self.lf_equipo_carga, text = 'Precio equipo').grid(column = 1, row = 1, pady = (6,0))
        self.precio_equipo_carga = Entry(self.lf_equipo_carga, width = 16)
        self.precio_equipo_carga.grid(column = 1, row = 2, pady = 3, padx = 3)
        #precio de las llantas
        Label(self.lf_equipo_carga, text = 'Precio llantas').grid(column = 2, row = 1, pady = (6,0))
        self.precio_llantas_carga = Entry(self.lf_equipo_carga, width = 16)
        self.precio_llantas_carga.grid(column = 2, row = 2, pady = 3, padx = 3)
        #Costo operador mes
        Label(self.lf_equipo_carga, text = 'Costo operador/mes').grid(column = 3, row = 1, pady = (6,0))
        self.costo_operador_mes_carga = Entry(self.lf_equipo_carga, width = 16)
        self.costo_operador_mes_carga.grid(column = 3, row = 2, pady = 3, padx = 3)
        #Disponibilidad mecanica
        Label(self.lf_equipo_carga, text = 'D. mecánica (%)').grid(column = 4, row = 1, pady = (6,0))
        self.disponibilidad_mecanica_carga = Entry(self.lf_equipo_carga, width = 16)
        self.disponibilidad_mecanica_carga.grid(column = 4, row = 2, pady = 3, padx = 3)
        #servicio de tanqueo
        Label(self.lf_equipo_carga, text = '¿Servicio de tanqueo?').grid(column = 5, row = 1, pady = (6,0))
        self.servicio_tanqueo_carga = Combobox(self.lf_equipo_carga, state = 'readonly', values = ['SI', 'NO'], width = 5)
        self.servicio_tanqueo_carga.grid(column = 5, row = 2, pady = 3, padx = 3)
        self.servicio_tanqueo_carga.current(1)

        #EQUIPO ACARREO
        #seleccion equipo
        Label(self.lf_equipo_carga, text = 'Equipo Acarreo').grid(column = 0, row = 3, pady = (6, 0))
        self.combo_equipo_acarreo = Combobox(self.lf_equipo_carga, state = 'readonly', width = 16)
        self.combo_equipo_acarreo.grid(column = 0, row = 4, pady = 3, padx = 3)
        #precio del equipo
        Label(self.lf_equipo_carga, text = 'Precio equipo').grid(column = 1, row = 3, pady = (6,0))
        self.precio_equipo_acarreo = Entry(self.lf_equipo_carga, width = 16)
        self.precio_equipo_acarreo.grid(column = 1, row = 4, pady = 3, padx = 3)
        #precio de las llantas
        Label(self.lf_equipo_carga, text = 'Precio llantas').grid(column = 2, row = 3, pady = (6,0))
        self.precio_llantas_acarreo = Entry(self.lf_equipo_carga, width = 16)
        self.precio_llantas_acarreo.grid(column = 2, row = 4, pady = 3, padx = 3)
        #Costo operador mes
        Label(self.lf_equipo_carga, text = 'Costo operador/mes').grid(column = 3, row = 3, pady = (6,0))
        self.costo_operador_mes_acarreo = Entry(self.lf_equipo_carga, width = 16)
        self.costo_operador_mes_acarreo.grid(column = 3, row = 4, pady = 3, padx = 3)
        #Disponibilidad mecanica
        Label(self.lf_equipo_carga, text = 'D. mecánica (%)').grid(column = 4, row = 3, pady = (6,0))
        self.disponibilidad_mecanica_acarreo = Entry(self.lf_equipo_carga, width = 16)
        self.disponibilidad_mecanica_acarreo.grid(column = 4, row = 4, pady = 3, padx = 3)
        #servicio de tanqueo
        Label(self.lf_equipo_carga, text = '¿Servicio de tanqueo?').grid(column = 5, row = 3, pady = (6,0))
        self.servicio_tanqueo_acarreo = Combobox(self.lf_equipo_carga, state = 'readonly', values = ['SI', 'NO'], width = 5)
        self.servicio_tanqueo_acarreo.grid(column = 5, row = 4, pady = 3, padx = 3)
        self.servicio_tanqueo_acarreo.current(1)

        #EQUIPÓS ADICIONALES
        #Equipo adicional 1
        self.lf_equipo_adicional = LabelFrame(self.lf_equipos, text = 'EQUIPOS ADICIONALES')
        self.lf_equipo_adicional.grid(column = 0, row = 2, sticky = W, padx = 5, pady = 5)

        #seleccion equipo
        Label(self.lf_equipo_adicional, text = 'Equipo').grid(column = 0, row = 1, pady = (6, 0))
        self.combo_equipo_adicional_1 = Combobox(self.lf_equipo_adicional, state = 'readonly', width = 16)
        self.combo_equipo_adicional_1.grid(column = 0, row = 2, pady = 3, padx = 3)
        #precio del equipo
        Label(self.lf_equipo_adicional, text = 'Precio equipo').grid(column = 1, row = 1, pady = (6,0))
        self.precio_equipo_adicional_1 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_equipo_adicional_1.grid(column = 1, row = 2, pady = 3, padx = 3)
        #precio de las llantas
        Label(self.lf_equipo_adicional, text = 'Precio llantas').grid(column = 2, row = 1, pady = (6,0))
        self.precio_llantas_adicional_1 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_llantas_adicional_1.grid(column = 2, row = 2, pady = 3, padx = 3)
        #Costo operador mes
        Label(self.lf_equipo_adicional, text = 'Costo operador/mes').grid(column = 3, row = 1, pady = (6,0))
        self.costo_operador_mes_adicional_1 = Entry(self.lf_equipo_adicional, width = 16)
        self.costo_operador_mes_adicional_1.grid(column = 3, row = 2, pady = 3, padx = 3)
        #Disponibilidad mecanica
        Label(self.lf_equipo_adicional, text = 'D. mecánica (%)').grid(column = 4, row = 1, pady = (6,0))
        self.disponibilidad_mecanica_adicional_1 = Entry(self.lf_equipo_adicional, width = 16)
        self.disponibilidad_mecanica_adicional_1.grid(column = 4, row = 2, pady = 3, padx = 3)
        #servicio de tanqueo
        Label(self.lf_equipo_adicional, text = '¿Servicio de tanqueo?').grid(column = 5, row = 1, pady = (6,0))
        self.servicio_tanqueo_adicional_1 = Combobox(self.lf_equipo_adicional, state = 'readonly', values = ['SI', 'NO'], width = 5)
        self.servicio_tanqueo_adicional_1.grid(column = 5, row = 2, pady = 3, padx = 3)
        self.servicio_tanqueo_adicional_1.current(1)

        #Equipo adicional 2
        #seleccion equipo
        Label(self.lf_equipo_adicional, text = 'Equipo').grid(column = 0, row = 3, pady = (6, 0))
        self.combo_equipo_adicional_2 = Combobox(self.lf_equipo_adicional, state = 'readonly', width = 16)
        self.combo_equipo_adicional_2.grid(column = 0, row = 4, pady = 3, padx = 3)
        #precio del equipo
        Label(self.lf_equipo_adicional, text = 'Precio equipo').grid(column = 1, row = 3, pady = (6,0))
        self.precio_equipo_adicional_2 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_equipo_adicional_2.grid(column = 1, row = 4, pady = 3, padx = 3)
        #precio de las llantas
        Label(self.lf_equipo_adicional, text = 'Precio llantas').grid(column = 2, row = 3, pady = (6,0))
        self.precio_llantas_adicional_2 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_llantas_adicional_2.grid(column = 2, row = 4, pady = 3, padx = 3)
        #Costo operador mes
        Label(self.lf_equipo_adicional, text = 'Costo operador/mes').grid(column = 3, row = 3, pady = (6,0))
        self.costo_operador_mes_adicional_2 = Entry(self.lf_equipo_adicional, width = 16)
        self.costo_operador_mes_adicional_2.grid(column = 3, row = 4, pady = 3, padx = 3)
        #Disponibilidad mecanica
        Label(self.lf_equipo_adicional, text = 'D. mecánica (%)').grid(column = 4, row = 3, pady = (6,0))
        self.disponibilidad_mecanica_adicional_2 = Entry(self.lf_equipo_adicional, width = 16)
        self.disponibilidad_mecanica_adicional_2.grid(column = 4, row = 4, pady = 3, padx = 3)
        #servicio de tanqueo
        Label(self.lf_equipo_adicional, text = '¿Servicio de tanqueo?').grid(column = 5, row = 3, pady = (6,0))
        self.servicio_tanqueo_adicional_2 = Combobox(self.lf_equipo_adicional, state = 'readonly', values = ['SI', 'NO'], width = 5)
        self.servicio_tanqueo_adicional_2.grid(column = 5, row = 4, pady = 3, padx = 3)
        self.servicio_tanqueo_adicional_2.current(1)

        #Equipo adicional 3
        #seleccion equipo
        Label(self.lf_equipo_adicional, text = 'Equipo').grid(column = 0, row = 5, pady = (6, 0))
        self.combo_equipo_adicional_3 = Combobox(self.lf_equipo_adicional, state = 'readonly', width = 16)
        self.combo_equipo_adicional_3.grid(column = 0, row = 6, pady = 3, padx = 3)
        #precio del equipo
        Label(self.lf_equipo_adicional, text = 'Precio equipo').grid(column = 1, row = 5, pady = (6,0))
        self.precio_equipo_adicional_3 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_equipo_adicional_3.grid(column = 1, row = 6, pady = 3, padx = 3)
        #precio de las llantas
        Label(self.lf_equipo_adicional, text = 'Precio llantas').grid(column = 2, row = 5, pady = (6,0))
        self.precio_llantas_adicional_3 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_llantas_adicional_3.grid(column = 2, row = 6, pady = 3, padx = 3)
        #Costo operador mes
        Label(self.lf_equipo_adicional, text = 'Costo operador/mes)').grid(column = 3, row = 5, pady = (6,0))
        self.costo_operador_mes_adicional_3 = Entry(self.lf_equipo_adicional, width = 16)
        self.costo_operador_mes_adicional_3.grid(column = 3, row = 6, pady = 3, padx = 3)
        #Disponibilidad mecanica
        Label(self.lf_equipo_adicional, text = 'D. mecánica (%)').grid(column = 4, row = 5, pady = (6,0))
        self.disponibilidad_mecanica_adicional_3 = Entry(self.lf_equipo_adicional, width = 16)
        self.disponibilidad_mecanica_adicional_3.grid(column = 4, row = 6, pady = 3, padx = 3)
        #servicio de tanqueo
        Label(self.lf_equipo_adicional, text = '¿Servicio de tanqueo?').grid(column = 5, row = 5, pady = (6,0))
        self.servicio_tanqueo_adicional_3 = Combobox(self.lf_equipo_adicional, state = 'readonly', values = ['SI', 'NO'], width = 5)
        self.servicio_tanqueo_adicional_3.grid(column = 5, row = 6, pady = 3, padx = 3)
        self.servicio_tanqueo_adicional_3.current(1)

        #Equipo adicional 4
        #seleccion equipo
        Label(self.lf_equipo_adicional, text = 'Equipo').grid(column = 0, row = 7, pady = (6, 0))
        self.combo_equipo_adicional_4 = Combobox(self.lf_equipo_adicional, state = 'readonly', width = 16)
        self.combo_equipo_adicional_4.grid(column = 0, row = 8, pady = 3, padx = 3)
        #precio del equipo
        Label(self.lf_equipo_adicional, text = 'Precio equipo').grid(column = 1, row = 7, pady = (6,0))
        self.precio_equipo_adicional_4 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_equipo_adicional_4.grid(column = 1, row = 8, pady = 3, padx = 3)
        #precio de las llantas
        Label(self.lf_equipo_adicional, text = 'Precio llantas').grid(column = 2, row = 7, pady = (6,0))
        self.precio_llantas_adicional_4 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_llantas_adicional_4.grid(column = 2, row = 8, pady = 3, padx = 3)
        #Costo operador mes
        Label(self.lf_equipo_adicional, text = 'Costo operador/mes').grid(column = 3, row = 7, pady = (6,0))
        self.costo_operador_mes_adicional_4 = Entry(self.lf_equipo_adicional, width = 16)
        self.costo_operador_mes_adicional_4.grid(column = 3, row = 8, pady = 3, padx = 3)
        #Disponibilidad mecanica
        Label(self.lf_equipo_adicional, text = 'D. mecánica (%)').grid(column = 4, row = 7, pady = (6,0))
        self.disponibilidad_mecanica_adicional_4 = Entry(self.lf_equipo_adicional, width = 16)
        self.disponibilidad_mecanica_adicional_4.grid(column = 4, row = 8, pady = 3, padx = 3)
        #servicio de tanqueo
        Label(self.lf_equipo_adicional, text = '¿Servicio de tanqueo?').grid(column = 5, row = 7, pady = (6,0))
        self.servicio_tanqueo_adicional_4 = Combobox(self.lf_equipo_adicional, state = 'readonly', values = ['SI', 'NO'], width = 5)
        self.servicio_tanqueo_adicional_4.grid(column = 5, row = 8, pady = 3, padx = 3)
        self.servicio_tanqueo_adicional_4.current(1)

        #Equipo adicional 5
        #seleccion equipo
        Label(self.lf_equipo_adicional, text = 'Equipo').grid(column = 0, row = 9, pady = (6, 0))
        self.combo_equipo_adicional_5 = Combobox(self.lf_equipo_adicional, state = 'readonly', width = 16)
        self.combo_equipo_adicional_5.grid(column = 0, row = 10, pady = 3, padx = 3)
        #precio del equipo
        Label(self.lf_equipo_adicional, text = 'Precio equipo').grid(column = 1, row = 9, pady = (6,0))
        self.precio_equipo_adicional_5 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_equipo_adicional_5.grid(column = 1, row = 10, pady = 3, padx = 3)
        #precio de las llantas
        Label(self.lf_equipo_adicional, text = 'Precio llantas').grid(column = 2, row = 9, pady = (6,0))
        self.precio_llantas_adicional_5 = Entry(self.lf_equipo_adicional, width = 16)
        self.precio_llantas_adicional_5.grid(column = 2, row = 10, pady = 3, padx = 3)
        #Costo operador mes
        Label(self.lf_equipo_adicional, text = 'Costo operador/mes').grid(column = 3, row = 9, pady = (6,0))
        self.costo_operador_mes_adicional_5 = Entry(self.lf_equipo_adicional, width = 16)
        self.costo_operador_mes_adicional_5.grid(column = 3, row = 10, pady = 3, padx = 3)
        #Disponibilidad mecanica
        Label(self.lf_equipo_adicional, text = 'D. mecánica (%)').grid(column = 4, row = 9, pady = (6,0))
        self.disponibilidad_mecanica_adicional_5 = Entry(self.lf_equipo_adicional, width = 16)
        self.disponibilidad_mecanica_adicional_5.grid(column = 4, row = 10, pady = 3, padx = 3)
        #servicio de tanqueo
        Label(self.lf_equipo_adicional, text = '¿Servicio de tanqueo?').grid(column = 5, row = 9, pady = (6,0))
        self.servicio_tanqueo_adicional_5 = Combobox(self.lf_equipo_adicional, state = 'readonly', values = ['SI', 'NO'], width = 5)
        self.servicio_tanqueo_adicional_5.grid(column = 5, row = 10, pady = 3, padx = 3)
        self.servicio_tanqueo_adicional_5.current(1)

        #Columna central
        #Produccion anual
        Label(self.lf_equipo_adicional, text = 'Producción').grid(column = 2, row = 11, pady = (15,0), padx = 5)
        Label(self.lf_equipo_adicional, text = '  anual* (Ton): ').grid(column = 2, row = 12, pady = (1,7), padx = 5)
        self.produccion_anual = Entry(self.lf_equipo_adicional, width = 12)
        self.produccion_anual.grid(column = 3, row = 11, pady = (15,7), padx = 5, rowspan = 2)

        #Realizar los cálculos de BC
        Button(self.lf_equipos, text = 'Enviar', command = self.ventana_resumen).grid(column = 0, row = 4, columnspan = 2)

        #ejecución de metodos
        self.combobox_valores_equipos()
    
    #MÉTODOS
    #Ejecución de query
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            resultdb = cursor.execute(query, parameters)
            conn.commit()
        return resultdb


    #OBTENER VALORES DE BASE DE DATOS
    def get_values(self):
        # cleaning Table
        records = self.treeview_datos_historicos.get_children()
        for element in records:
            self.treeview_datos_historicos.delete(element)
        # getting data
        query = 'SELECT * FROM Maquinaria ORDER BY equipo DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.treeview_datos_historicos.insert('', 0, text = row[0], values = row[0:])

    #Validar que str sea float
    def check_float(self, number):
        try:
            float(number)

            return True
        except ValueError:
            return False

    #Validación
    def validation(self):
        return len(self.equipo.get()) != 0 and len(self.vida_economica.get()) != 0 and len(self.tasa_seguro.get()) != 0 and len(self.mantenimiento.get()) != 0 and len(self.rescate.get()) != 0 and len(self.interes.get()) != 0 and len(self.consumo_combustible.get()) != 0 and len(self.consumo_lubricante_carter.get()) != 0 and len(self.consumo_lubricante_hidraulico.get()) != 0 and len(self.consumo_lubricante_transmision.get()) != 0 and len(self.tendido_llantas.get()) != 0 and len(self.capacidad_tanque.get()) != 0 and len(self.tiempo_tanqueo.get()) != 0 and len(self.capacidad_carga.get()) != 0 and self.check_float(self.vida_economica.get()) and self.check_float(self.tasa_seguro.get()) and self.check_float(self.mantenimiento.get()) and self.check_float(self.rescate.get()) and self.check_float(self.interes.get()) and self.check_float(self.consumo_combustible.get()) and self.check_float(self.consumo_lubricante_carter.get()) and self.check_float(self.consumo_lubricante_hidraulico.get()) and self.check_float(self.consumo_lubricante_transmision.get()) and self.check_float(self.tendido_llantas.get()) and self.check_float(self.capacidad_tanque.get()) and self.check_float(self.tiempo_tanqueo.get()) and self.check_float(self.capacidad_carga.get())

    #Añadir valores a la base de datos
    def add_values(self):
        if self.validation() == True:
            query = 'INSERT INTO Maquinaria VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.equipo.get(),
            self.vida_economica.get(),
            self.tasa_seguro.get(),
            self.mantenimiento.get(),
            self.rescate.get(),
            self.interes.get(),
            self.consumo_combustible.get(),
            self.consumo_lubricante_carter.get(),
            self.consumo_lubricante_hidraulico.get(),
            self.consumo_lubricante_transmision.get(),
            self.tendido_llantas.get(),
            self.capacidad_tanque.get(),
            self.tiempo_tanqueo.get(),
            self.capacidad_carga.get()
            )
            #Query para agregar datos
            self.run_query(query, parameters)
            #Actualizar combobox de equipos en la pestaña de costos
            self.combobox_valores_equipos()
        else:
            error = Toplevel(self.root)
            Label(error, text = 'Asegúrese de: ').grid(column = 0, row = 0, pady = 1, padx = 10, sticky = "w")
            Label(error, text = '- Llenar todos los campos').grid(column = 0, row = 1, pady = 1, padx = 10, sticky = 'w')
            Label(error, text = '- Introducir sólo valores numéricos').grid(column = 0, row = 2, pady = 1, padx = 10, sticky = 'w')

            Button(error, text = 'Aceptar', command = (lambda: error.destroy())).grid(column = 0, row = 3, pady = (2, 7))
            error.grab_set()
        self.get_values()

    #Borrar valores de la base de datos
    def pre_delete_values(self):
        id =  self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][0]
        def delete_values(id):
            query = 'DELETE FROM Maquinaria WHERE id = ?'
            self.run_query(query, (id, ))
            self.get_values()
            borrar.destroy()

        borrar = Toplevel()
        Label(borrar, text = 'Se borrará este equipo de forma permanente').grid(column = 0, row = 0, columnspan = 2, padx = 5, pady = 6)
        #Boton aceptar
        Button(borrar, text = 'Aceptar', command = (lambda: delete_values(id))).grid(column = 0, row = 1, columnspan = 1, padx = 3, pady = (0,5))
        #Boton Cancelar
        Button(borrar, text = 'Cancelar', command = (lambda: borrar.destroy())).grid(column = 1, row = 1, columnspan = 1, padx = 3, pady = (0, 5))

        self.get_values()
        self.combobox_valores_equipos()

    #Actualizar valores
    def actualizar_valores(self):
        equipo = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][1]
        vida_economica = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][2]
        tasa_seguro = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][3]
        mantenimiento = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][4]
        rescate = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][5]
        interes = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][6]
        consumo_combustible = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][7]
        consumo_lubricante_carter = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][8]
        consumo_lubricante_hidraulico = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][9]
        consumo_lubricante_transmision = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][10]
        tendido_llantas = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][11]
        capacidad_tanque = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][12]
        tiempo_tanqueo = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][13]
        capacidad_carga = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][14]

        #Inicializando toplevel
        self.actualizar = Toplevel()

        #títulos
        Label(self.actualizar, text = 'Equipo: ').grid(column = 0, row = 0, sticky = W, pady = 4, padx = (5,0))
        self.equipo_edit = Entry(self.actualizar, width = 15)
        self.equipo_edit.insert(END, equipo)
        self.equipo_edit.grid(column = 1, row = 0, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Vida Económica(años): ').grid(column = 0, row = 1, sticky = W, pady = 4, padx = (5,0))
        self.vida_economica_edit = Entry(self.actualizar, width = 12)
        self.vida_economica_edit.insert(END, vida_economica)
        self.vida_economica_edit.grid(column = 1, row = 1, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Tasa de seguro (%): ').grid(column = 0, row = 2, sticky = W, pady = 4, padx = (5,0))
        self.tasa_seguro_edit = Entry(self.actualizar, width = 12)
        self.tasa_seguro_edit.insert(END, tasa_seguro)
        self.tasa_seguro_edit.grid(column = 1, row = 2, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = '% de mantenimiento (%): ').grid(column = 0, row = 3, sticky = W, pady = 4, padx = (5,0))
        self.mantenimiento_edit = Entry(self.actualizar, width = 12)
        self.mantenimiento_edit.insert(END, mantenimiento)
        self.mantenimiento_edit.grid(column = 1, row = 3, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = '% de rescate (%): ').grid(column = 0, row = 4, sticky = W, pady = 4, padx = (5,0))
        self.rescate_edit = Entry(self.actualizar, width = 12)
        self.rescate_edit.insert(END, rescate)
        self.rescate_edit.grid(column = 1, row = 4, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Tasa de interés (%): ').grid(column = 0, row = 5, sticky = W, pady = 4, padx = (5,0))
        self.interes_edit = Entry(self.actualizar, width = 12)
        self.interes_edit.insert(END, interes)
        self.interes_edit.grid(column = 1, row = 5, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Consumo combustible (gal/hr): ').grid(column = 0, row = 6, sticky = W, pady = 4, padx = (5,0))
        self.consumo_combustible_edit = Entry(self.actualizar, width = 12)
        self.consumo_combustible_edit.insert(END, consumo_combustible)
        self.consumo_combustible_edit.grid(column = 1, row = 6, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Consumo lubricante carter (gal/hr): ').grid(column = 0, row = 7, sticky = W, pady = 4, padx = (5,0))
        self.consumo_lubricante_carter_edit = Entry(self.actualizar, width = 12)
        self.consumo_lubricante_carter_edit.insert(END, consumo_lubricante_carter)
        self.consumo_lubricante_carter_edit.grid(column = 1, row = 7, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Consumo lubricante hidráulico (gal/hr): ').grid(column = 0, row = 8, sticky = W, pady = 4, padx = (5,0))
        self.consumo_lubricante_hidraulico_edit = Entry(self.actualizar, width = 12)
        self.consumo_lubricante_hidraulico_edit.insert(END, consumo_lubricante_hidraulico)
        self.consumo_lubricante_hidraulico_edit.grid(column = 1, row = 8, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Consumo lubricante transmisión/mandos finales (gal/hr): ').grid(column = 0, row = 9, sticky = W, pady = 4, padx = (5,0))
        self.consumo_lubricante_transmision_edit = Entry(self.actualizar, width = 12)
        self.consumo_lubricante_transmision_edit.insert(END, consumo_lubricante_transmision)
        self.consumo_lubricante_transmision_edit.grid(column = 1, row = 9, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Tendido de llantas por hr (tendido/hr): ').grid(column = 0, row = 10, sticky = W, pady = 4, padx = (5,0))
        self.tendido_llantas_edit = Entry(self.actualizar, width = 12)
        self.tendido_llantas_edit.insert(END, tendido_llantas)
        self.tendido_llantas_edit.grid(column = 1, row = 10, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Capacidad del tanque (gal): ').grid(column = 0, row = 11, sticky = W, pady = 4, padx = (5,0))
        self.capacidad_tanque_edit = Entry(self.actualizar, width = 12)
        self.capacidad_tanque_edit.insert(END, capacidad_tanque)
        self.capacidad_tanque_edit.grid(column = 1, row = 11, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Tiempo de tanqueo (min): ').grid(column = 0, row = 12, sticky = W, pady = 4, padx = (5,0))
        self.tiempo_tanqueo_edit = Entry(self.actualizar, width = 12)
        self.tiempo_tanqueo_edit.insert(END, tiempo_tanqueo)
        self.tiempo_tanqueo_edit.grid(column = 1, row = 12, pady = 4, sticky = W, padx = (0,5))

        Label(self.actualizar, text = 'Capacidad de carga (m3): ').grid(column = 0, row = 13, sticky = W, pady = 4, padx = (5,0))
        self.capacidad_carga_edit = Entry(self.actualizar, width = 12)
        self.capacidad_carga_edit.insert(END, capacidad_carga)
        self.capacidad_carga_edit.grid(column = 1, row = 13, pady = 4, sticky = W, padx = (0,5))

        self.actualizar.grab_set()

        Button(self.actualizar, text = 'Enviar', command = self.guardar_valores).grid(column = 0, row = 14, columnspan = 2, pady = 5, padx = (5,0))

    #guardar los valores de la ventana de actualización
    def guardar_valores(self):
        id = self.treeview_datos_historicos.item(self.treeview_datos_historicos.selection())['values'][0]
        query = 'UPDATE Maquinaria SET equipo = ?, vida_economica = ?, tasa_seguro = ?, p_mantenimiento = ?, p_rescate = ?, tasa_interes = ?, consumo_combustible = ?, consumo_carter = ?, consumo_hidraulico = ?, consumo_transmision = ?, tendido = ?, capacidad_tanque = ?, tiempo_tanqueo = ?, capacidad_carga = ?  WHERE id = ?'
        parameters = (
        self.equipo_edit.get(),
        self.vida_economica_edit.get(),
        self.tasa_seguro_edit.get(),
        self.mantenimiento_edit.get(),
        self.rescate_edit.get(),
        self.interes_edit.get(),
        self.consumo_combustible_edit.get(),
        self.consumo_lubricante_carter_edit.get(),
        self.consumo_lubricante_hidraulico_edit.get(),
        self.consumo_lubricante_transmision_edit.get(),
        self.tendido_llantas_edit.get(),
        self.capacidad_tanque_edit.get(),
        self.tiempo_tanqueo_edit.get(),
        self.capacidad_carga_edit.get(),
        id
        )

        self.run_query(query, parameters)
        self.get_values()
        self.actualizar.destroy()
        self.combobox_valores_equipos()

    #Pasando los valores de equipós de la base de datos a los combobox de la pestaña costo maquinaria
    def combobox_valores_equipos(self):
        query = 'SELECT equipo FROM Maquinaria'
        bd = self.run_query(query)
        bd_list = list(bd)
        valores = []
        for values in bd_list:
            valor = values[0]
            valores.append(valor)
        valores.append('')
        self.combo_equipo_tanqueo['values'] = valores
        self.combo_equipo_carga['values'] = valores
        self.combo_equipo_acarreo['values'] = valores
        self.combo_equipo_adicional_1['values'] = valores
        self.combo_equipo_adicional_2['values'] = valores
        self.combo_equipo_adicional_3['values'] = valores
        self.combo_equipo_adicional_4['values'] = valores
        self.combo_equipo_adicional_5['values'] = valores

    #Validación de entradas no nulas y numéricas en pestaña costo maquinaria
    def validation_calculo(self):
        return len(self.uso_disponibilidad.get()) != 0 and len(self.turno.get()) != 0 and len(self.horas_lluvia.get()) != 0 and len(self.dias_semana.get()) != 0 and len(self.dias_no_laborables.get()) != 0 and len(self.densidad_suelta.get()) != 0 and len(self.velocidad_cargado.get()) != 0 and len(self.tiempo_aculatamiento.get()) != 0 and len(self.tiempo_cargador.get()) != 0 and len(self.tiempo_descarga.get()) != 0 and len(self.distancia_via.get()) != 0 and len(self.produccion_anual.get()) != 0 and len(self.velocidad_cargado.get()) != 0 and len(self.costo_diesel.get()) != 0 and len(self.costo_lubricante_carter.get()) != 0 and len(self.costo_lubricante_hidraulico.get()) != 0 and len(self.costo_lubricante_transmision.get()) != 0 and self.check_float(self.uso_disponibilidad.get()) and self.check_float(self.turno.get()) and self.check_float(self.horas_lluvia.get()) and self.check_float(self.dias_no_laborables.get()) and self.check_float(self.densidad_suelta.get()) and self.check_float(self.velocidad_cargado.get()) and self.check_float(self.tiempo_aculatamiento.get()) and self.check_float(self.tiempo_cargador.get()) and self.check_float(self.tiempo_descarga.get()) and self.check_float(self.distancia_via.get()) and self.check_float(self.produccion_anual.get()) and self.check_float(self.velocidad_descargado.get()) and self.check_float(self.dias_semana.get()) and self.check_float(self.costo_diesel.get()) and self.check_float(self.costo_lubricante_carter.get()) and self.check_float(self.costo_lubricante_hidraulico.get()) and self.check_float(self.costo_lubricante_transmision.get())

    def horas_disponibles(self):
        if self.validation_calculo() == True:
            uso_disponibilidad = float(self.uso_disponibilidad.get())
            turno = float(self.turno.get())
            horas_lluvia = float(self.horas_lluvia.get())
            dias_semana = float(self.dias_semana.get())
            dias_no_laborables = float(self.dias_no_laborables.get())

            #Calculo horas disponibles año
            horas_ano = ((365 - dias_no_laborables - ((7 - dias_semana)*52) - (horas_lluvia/24))*turno)*(uso_disponibilidad/100)


        else:
            error = Toplevel(self.root)
            Label(error, text = 'Asegúrese de: ').grid(column = 0, row = 0, pady = 1, padx = 10, sticky = "w")
            Label(error, text = '- Llenar todos los campos con *').grid(column = 0, row = 1, pady = 1, padx = 10, sticky = 'w')
            Label(error, text = '- Introducir sólo valores numéricos').grid(column = 0, row = 2, pady = 1, padx = 10, sticky = 'w')

            Button(error, text = 'Aceptar', command = (lambda: error.destroy())).grid(column = 0, row = 3, pady = (2, 7))
            error.grab_set()
        return horas_ano

    def hora(self):
        bb = self.horas_disponibles()
        print(bb)

    def costo_equipo_tanqueo(self, equipo, precio_equipo, precio_llantas, precio_operador, disponibilidad_mecanica, precio_diesel, precio_carter, precio_hidraulico, precio_transmision):

        #EJECUCION DE QUERY PARA OBTENER VALORES DE LA BD
        query_vida_economica = 'SELECT vida_economica FROM Maquinaria WHERE equipo = ?'
        query_tasa_seguro = 'SELECT tasa_seguro FROM Maquinaria WHERE equipo = ?'
        query_mantenimiento = 'SELECT p_mantenimiento FROM Maquinaria WHERE equipo = ?'
        query_rescate = 'SELECT p_rescate FROM Maquinaria WHERE equipo = ?'
        query_interes = 'SELECT tasa_interes FROM Maquinaria WHERE equipo = ?'
        query_diesel = 'SELECT consumo_combustible FROM Maquinaria WHERE equipo = ?'
        query_carter = 'SELECT consumo_carter FROM Maquinaria WHERE equipo = ?'
        query_hidraulico = 'SELECT consumo_hidraulico FROM Maquinaria WHERE equipo = ?'
        query_transmision ='SELECT consumo_transmision FROM Maquinaria WHERE equipo = ?'
        query_tendido = 'SELECT tendido FROM Maquinaria WHERE equipo = ?'
        query_capacidad_tanque = 'SELECT capacidad_tanque FROM Maquinaria WHERE equipo = ?'
        query_tiempo_tanqueo =  'SELECT tiempo_tanqueo FROM Maquinaria WHERE equipo = ?'


        #vida economica
        vida_economica_l = list(self.run_query(query_vida_economica, (equipo, )))
        for vida in vida_economica_l:
            vida_economica = float(vida[0])
        #tasa de seguro
        tasa_seguro_l = list(self.run_query(query_tasa_seguro, (equipo, )))
        for seguro in tasa_seguro_l:
            tasa_seguro = float(seguro[0])/100
        #mantenimiento
        mantenimiento_l = list(self.run_query(query_mantenimiento, (equipo, )))
        for p_mantenimiento in mantenimiento_l:
            mantenimiento = float(p_mantenimiento[0])/100
        #Rescate
        rescate_l = list(self.run_query(query_rescate, (equipo, )))
        for p_rescate in rescate_l:
            rescate = float(p_rescate[0])/100
        #interes
        interes_l = list(self.run_query(query_interes, (equipo, )))
        for p_interes in interes_l:
            interes = float(p_interes[0])/100
        #Diesel
        consumo_diesel_l = list(self.run_query(query_diesel, (equipo, )))
        for diesel in consumo_diesel_l:
            consumo_diesel = float(diesel[0])
        #Carter
        consumo_carter_l = list(self.run_query(query_carter, (equipo, )))
        for carter in consumo_carter_l:
            consumo_carter = float(carter[0])
        #Hidraulico
        consumo_hidraulico_l = list(self.run_query(query_hidraulico, (equipo, )))
        for hidraulico in consumo_hidraulico_l:
            consumo_hidraulico = float(hidraulico[0])
        #Transmision
        consumo_transmision_l = list(self.run_query(query_transmision, (equipo, )))
        for transmision in consumo_transmision_l:
            consumo_transmision = float(transmision[0])
        #tendido
        tendido_l = list(self.run_query(query_tendido, (equipo, )))
        for tendido_i in tendido_l:
            tendido = float(tendido_i[0])
        #Capacidad tanque
        capacidad_tanque_l = list(self.run_query(query_capacidad_tanque, (equipo, )))
        for tanque in capacidad_tanque_l:
            capacidad_tanque = float(tanque[0])
        #tiempo tanqueo
        tiempo_tanqueo_l = list(self.run_query(query_tiempo_tanqueo, (equipo, )))
        for tiempo_t in tiempo_tanqueo_l:
            tiempo_tanqueo = float(tiempo_t[0])

        #precio_equipo_float = float(precio_equipo)
        #precio_llantas_float = float(precio_llantas)
        #costo_operador_float = float(costo_operador)
        disponibilidad_mecanica_float = float(disponibilidad_mecanica)

        horas = self.horas_disponibles()

        #Horas efectivas
        horas_efectivas = horas * disponibilidad_mecanica_float/100
        #Valor máquina (Vm)
        valor_maquina = precio_equipo - precio_llantas
        #Vr
        vr = valor_maquina*rescate
        #Ve
        ve = vida_economica*horas_efectivas

        #CARGOS FIJOS
        depreciacion = (valor_maquina-vr)/ve
        inversion = ((valor_maquina + vr)*interes)/(2*horas_efectivas)
        seguros = ((valor_maquina + vr)*tasa_seguro)/(2*horas_efectivas)
        costo_mantenimiento = mantenimiento*depreciacion

        #CONSUMIBLES
        costo_diesel = consumo_diesel*precio_diesel
        costo_carter = consumo_carter*precio_carter
        costo_hidraulico = consumo_hidraulico*precio_hidraulico
        costo_transmision = consumo_transmision*precio_transmision
        costo_llantas = tendido*precio_llantas

        #OPERADOR
        costo_operador = precio_operador/(horas_efectivas/12)

        costo_total = depreciacion + inversion + seguros + costo_mantenimiento + costo_diesel + costo_carter + costo_hidraulico + costo_transmision + costo_llantas + costo_operador

        return costo_total

    def costo_equipos(self, equipo, precio_equipo, precio_llantas, precio_operador, disponibilidad_mecanica, precio_diesel, precio_carter, precio_hidraulico, precio_transmision, servicio):
        if servicio == 'SI':
            costo_tanqueo = self.costo_equipo_tanqueo(self.combo_equipo_tanqueo.get(), float(self.precio_equipo_tanqueo.get()), float(self.precio_llantas_tanqueo.get()), float(self.costo_operador_mes_tanqueo.get()), float(self.disponibilidad_mecanica_tanqueo.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()))

            #EJECUCION DE QUERY PARA OBTENER VALORES DE LA BD
            query_vida_economica = 'SELECT vida_economica FROM Maquinaria WHERE equipo = ?'
            query_tasa_seguro = 'SELECT tasa_seguro FROM Maquinaria WHERE equipo = ?'
            query_mantenimiento = 'SELECT p_mantenimiento FROM Maquinaria WHERE equipo = ?'
            query_rescate = 'SELECT p_rescate FROM Maquinaria WHERE equipo = ?'
            query_interes = 'SELECT tasa_interes FROM Maquinaria WHERE equipo = ?'
            query_diesel = 'SELECT consumo_combustible FROM Maquinaria WHERE equipo = ?'
            query_carter = 'SELECT consumo_carter FROM Maquinaria WHERE equipo = ?'
            query_hidraulico = 'SELECT consumo_hidraulico FROM Maquinaria WHERE equipo = ?'
            query_transmision ='SELECT consumo_transmision FROM Maquinaria WHERE equipo = ?'
            query_tendido = 'SELECT tendido FROM Maquinaria WHERE equipo = ?'
            query_capacidad_tanque = 'SELECT capacidad_tanque FROM Maquinaria WHERE equipo = ?'
            query_tiempo_tanqueo =  'SELECT tiempo_tanqueo FROM Maquinaria WHERE equipo = ?'


            #vida economica
            vida_economica_l = list(self.run_query(query_vida_economica, (equipo, )))
            for vida in vida_economica_l:
                vida_economica = float(vida[0])
            #tasa de seguro
            tasa_seguro_l = list(self.run_query(query_tasa_seguro, (equipo, )))
            for seguro in tasa_seguro_l:
                tasa_seguro = float(seguro[0])/100
            #mantenimiento
            mantenimiento_l = list(self.run_query(query_mantenimiento, (equipo, )))
            for p_mantenimiento in mantenimiento_l:
                mantenimiento = float(p_mantenimiento[0])/100
            #Rescate
            rescate_l = list(self.run_query(query_rescate, (equipo, )))
            for p_rescate in rescate_l:
                rescate = float(p_rescate[0])/100
            #interes
            interes_l = list(self.run_query(query_interes, (equipo, )))
            for p_interes in interes_l:
                interes = float(p_interes[0])/100
            #Diesel
            consumo_diesel_l = list(self.run_query(query_diesel, (equipo, )))
            for diesel in consumo_diesel_l:
                consumo_diesel = float(diesel[0])
            #Carter
            consumo_carter_l = list(self.run_query(query_carter, (equipo, )))
            for carter in consumo_carter_l:
                consumo_carter = float(carter[0])
            #Hidraulico
            consumo_hidraulico_l = list(self.run_query(query_hidraulico, (equipo, )))
            for hidraulico in consumo_hidraulico_l:
                consumo_hidraulico = float(hidraulico[0])
            #Transmision
            consumo_transmision_l = list(self.run_query(query_transmision, (equipo, )))
            for transmision in consumo_transmision_l:
                consumo_transmision = float(transmision[0])
            #tendido
            tendido_l = list(self.run_query(query_tendido, (equipo, )))
            for tendido_i in tendido_l:
                tendido = float(tendido_i[0])
            #Capacidad tanque
            capacidad_tanque_l = list(self.run_query(query_capacidad_tanque, (equipo, )))
            for tanque in capacidad_tanque_l:
                capacidad_tanque = float(tanque[0])
            #tiempo tanqueo
            tiempo_tanqueo_l = list(self.run_query(query_tiempo_tanqueo, (equipo, )))
            for tiempo_t in tiempo_tanqueo_l:
                tiempo_tanqueo = float(tiempo_t[0])

            #precio_equipo_float = float(precio_equipo)
            #precio_llantas_float = float(precio_llantas)
            #costo_operador_float = float(costo_operador)
            disponibilidad_mecanica_float = float(disponibilidad_mecanica)

            horas = self.horas_disponibles()



            #Horas efectivas
            horas_efectivas = horas * disponibilidad_mecanica_float/100
            #Valor máquina (Vm)
            valor_maquina = precio_equipo - precio_llantas
            #Vr
            vr = valor_maquina*rescate
            #Ve
            ve = vida_economica*horas_efectivas
            #numero de tanqueadas
            numero_tanqueadas = int(math.ceil(((horas_efectivas*consumo_diesel*0.8)/capacidad_tanque)/12))
            #tiempo de tanqueo al año horas
            tiempo_tanqueo_ano = (12*numero_tanqueadas*tiempo_tanqueo)/60
            #consumo_tanqueo
            consumo_tanqueo = tiempo_tanqueo_ano/horas_efectivas


            #CARGOS FIJOS
            depreciacion = (valor_maquina-vr)/ve
            inversion = ((valor_maquina + vr)*interes)/(2*horas_efectivas)
            seguros = ((valor_maquina + vr)*tasa_seguro)/(2*horas_efectivas)
            costo_mantenimiento = mantenimiento*depreciacion

            #CONSUMIBLES
            costo_diesel = consumo_diesel*precio_diesel
            costo_carter = consumo_carter*precio_carter
            costo_hidraulico = consumo_hidraulico*precio_hidraulico
            costo_transmision = consumo_transmision*precio_transmision
            costo_llantas = tendido*precio_llantas

            #OPERADOR
            costo_operador = precio_operador/(horas_efectivas/12)

            costo_total = depreciacion + inversion + seguros + costo_mantenimiento + costo_diesel + costo_carter + costo_hidraulico + costo_transmision + costo_llantas + costo_operador + costo_tanqueo*consumo_tanqueo

        else:

            #EJECUCION DE QUERY PARA OBTENER VALORES DE LA BD
            query_vida_economica = 'SELECT vida_economica FROM Maquinaria WHERE equipo = ?'
            query_tasa_seguro = 'SELECT tasa_seguro FROM Maquinaria WHERE equipo = ?'
            query_mantenimiento = 'SELECT p_mantenimiento FROM Maquinaria WHERE equipo = ?'
            query_rescate = 'SELECT p_rescate FROM Maquinaria WHERE equipo = ?'
            query_interes = 'SELECT tasa_interes FROM Maquinaria WHERE equipo = ?'
            query_diesel = 'SELECT consumo_combustible FROM Maquinaria WHERE equipo = ?'
            query_carter = 'SELECT consumo_carter FROM Maquinaria WHERE equipo = ?'
            query_hidraulico = 'SELECT consumo_hidraulico FROM Maquinaria WHERE equipo = ?'
            query_transmision ='SELECT consumo_transmision FROM Maquinaria WHERE equipo = ?'
            query_tendido = 'SELECT tendido FROM Maquinaria WHERE equipo = ?'
            query_capacidad_tanque = 'SELECT capacidad_tanque FROM Maquinaria WHERE equipo = ?'
            query_tiempo_tanqueo =  'SELECT tiempo_tanqueo FROM Maquinaria WHERE equipo = ?'


            #vida economica
            vida_economica_l = list(self.run_query(query_vida_economica, (equipo, )))
            for vida in vida_economica_l:
                vida_economica = float(vida[0])
            #tasa de seguro
            tasa_seguro_l = list(self.run_query(query_tasa_seguro, (equipo, )))
            for seguro in tasa_seguro_l:
                tasa_seguro = float(seguro[0])/100
            #mantenimiento
            mantenimiento_l = list(self.run_query(query_mantenimiento, (equipo, )))
            for p_mantenimiento in mantenimiento_l:
                mantenimiento = float(p_mantenimiento[0])/100
            #Rescate
            rescate_l = list(self.run_query(query_rescate, (equipo, )))
            for p_rescate in rescate_l:
                rescate = float(p_rescate[0])/100
            #interes
            interes_l = list(self.run_query(query_interes, (equipo, )))
            for p_interes in interes_l:
                interes = float(p_interes[0])/100
            #Diesel
            consumo_diesel_l = list(self.run_query(query_diesel, (equipo, )))
            for diesel in consumo_diesel_l:
                consumo_diesel = float(diesel[0])
            #Carter
            consumo_carter_l = list(self.run_query(query_carter, (equipo, )))
            for carter in consumo_carter_l:
                consumo_carter = float(carter[0])
            #Hidraulico
            consumo_hidraulico_l = list(self.run_query(query_hidraulico, (equipo, )))
            for hidraulico in consumo_hidraulico_l:
                consumo_hidraulico = float(hidraulico[0])
            #Transmision
            consumo_transmision_l = list(self.run_query(query_transmision, (equipo, )))
            for transmision in consumo_transmision_l:
                consumo_transmision = float(transmision[0])
            #tendido
            tendido_l = list(self.run_query(query_tendido, (equipo, )))
            for tendido_i in tendido_l:
                tendido = float(tendido_i[0])
            #Capacidad tanque
            capacidad_tanque_l = list(self.run_query(query_capacidad_tanque, (equipo, )))
            for tanque in capacidad_tanque_l:
                capacidad_tanque = float(tanque[0])
            #tiempo tanqueo
            tiempo_tanqueo_l = list(self.run_query(query_tiempo_tanqueo, (equipo, )))
            for tiempo_t in tiempo_tanqueo_l:
                tiempo_tanqueo = float(tiempo_t[0])

            #precio_equipo_float = float(precio_equipo)
            #precio_llantas_float = float(precio_llantas)
            #costo_operador_float = float(costo_operador)
            disponibilidad_mecanica_float = float(disponibilidad_mecanica)

            horas = self.horas_disponibles()

            #Horas efectivas
            horas_efectivas = horas * disponibilidad_mecanica_float/100
            #Valor máquina (Vm)
            valor_maquina = precio_equipo - precio_llantas
            #Vr
            vr = valor_maquina*rescate
            #Ve
            ve = vida_economica*horas_efectivas

            #CARGOS FIJOS
            depreciacion = (valor_maquina-vr)/ve
            inversion = ((valor_maquina + vr)*interes)/(2*horas_efectivas)
            seguros = ((valor_maquina + vr)*tasa_seguro)/(2*horas_efectivas)
            costo_mantenimiento = mantenimiento*depreciacion

            #CONSUMIBLES
            costo_diesel = consumo_diesel*precio_diesel
            costo_carter = consumo_carter*precio_carter
            costo_hidraulico = consumo_hidraulico*precio_hidraulico
            costo_transmision = consumo_transmision*precio_transmision
            costo_llantas = tendido*precio_llantas

            #OPERADOR
            costo_operador = precio_operador/(horas_efectivas/12)

            costo_total = depreciacion + inversion + seguros + costo_mantenimiento + costo_diesel + costo_carter + costo_hidraulico + costo_transmision + costo_llantas + costo_operador

        return costo_total

    def calculo_camiones(self, carga, acarreo, disponibilidad_mecanica):

        query_capacidad_balde = 'SELECT capacidad_carga FROM Maquinaria WHERE equipo = ?'
        query_capacidad_camion =  'SELECT capacidad_carga FROM Maquinaria WHERE equipo = ?'

        capacidad_balde_l = list(self.run_query(query_capacidad_balde, (carga, )))
        for capacidad_b in capacidad_balde_l:
            capacidad_balde = float(capacidad_b[0])

        capacidad_camion_l = list(self.run_query(query_capacidad_camion, (acarreo, )))
        for capacidad_c in capacidad_camion_l:
            capacidad_camion = float(capacidad_c[0])

        horas = float(self.horas_disponibles())
        horas_efectivas = horas*disponibilidad_mecanica/100
        densidad = float(self.densidad_suelta.get())
        toneladas = float(self.produccion_anual.get())
        metros_cubicos_requeridos = (toneladas/densidad)/horas_efectivas

        #tiempos
        tiempo_cargador = float(self.tiempo_cargador.get())
        tiempo_descarga = float(self.tiempo_descarga.get())

        #distancia via
        distancia_via = float(self.distancia_via.get())
        #Velocidades
        velocidad_cargado = float(self.velocidad_cargado.get())
        velocidad_descargado = float(self.velocidad_descargado.get())

        #Número pasadas
        numero_pasadas = float(math.ceil(capacidad_camion/capacidad_balde))

        #tiempo de carga
        tiempo_cargando = (numero_pasadas*tiempo_cargador)/60

        #tiempo recorriendo la distancia cargado
        tiempo_camion_cargado = (distancia_via*0.06)/(velocidad_cargado)

        #tiempo recorriendo la distancia descargado
        tiempo_camion_descargado = (distancia_via*0.06)/(velocidad_descargado)

        #tiempoo de aculatamiento
        tiempo_aculatamiento = float(self.tiempo_aculatamiento.get())

        #tiempo de descarga
        tiempo_descarga = float(self.tiempo_descarga.get())

        #tiempo de ciclo
        tiempo_ciclo = tiempo_aculatamiento/60 + tiempo_cargando + tiempo_camion_cargado + tiempo_descarga/60 + tiempo_camion_descargado

        #Producción por volquetas/hr
        produccion_volqueta = (60*capacidad_camion)/tiempo_ciclo

        #número volquetas
        numero_volquetas = int(math.ceil((metros_cubicos_requeridos/produccion_volqueta)+1))


        return numero_volquetas

    #TOPLEVEL PARA LA EXHIBICIÓN DE LOS RESULTADOS
    def ventana_resumen(self):
        #VALIDAR QUE LOS CAMPOS NO SE ENCUENTREN VACIOS - NOTA: REALIZAR LA VALIDACIÓN DE QUE LOS CAMPOS SEAN NUMÉRICOS DONDE APLIQUE
        if self.validation_calculo() == True:

            self.top_costos = Toplevel(self.root)

            Label(self.top_costos, text = 'EQUIPO' , font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 1, pady = 5, padx = 6)

            Label(self.top_costos, text = 'CANTIDAD', font = ('Helvetica', '9', 'bold')).grid(column = 1, row =1, pady = 5, padx = 6)

            Label(self.top_costos, text = 'COSTO MENSUAL', font = ('Helvetica', '9', 'bold')).grid(column = 2, row =1, pady = 5, padx = 6)

            Label(self.top_costos, text = 'COSTO ANUAL', font = ('Helvetica', '9', 'bold')).grid(column = 3, row =1, pady = 5, padx = 6)

            if len(self.combo_equipo_carga.get()) != 0:

                #costo equipo carga
                costo_carga = self.costo_equipos(self.combo_equipo_carga.get(), float(self.precio_equipo_carga.get()), float(self.precio_llantas_carga.get()), float(self.costo_operador_mes_carga.get()), float(self.disponibilidad_mecanica_carga.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()), self.servicio_tanqueo_carga.get())
                #Número de camiones
                camiones = self.calculo_camiones(self.combo_equipo_carga.get(), self.combo_equipo_acarreo.get(), float(self.disponibilidad_mecanica_carga.get()))
                #Label para numero de camiones
                Label(self.top_costos, text = 'Se necesitan ' + str(camiones) + " " + self.combo_equipo_acarreo.get() + ' operando con ' + self.combo_equipo_carga.get()).grid(column = 0, row = 0, columnspan = 4, pady = 5)

                #Costo mensual
                costo_carga_mes = float(costo_carga)*((float(self.horas_disponibles())*float(self.disponibilidad_mecanica_carga.get())/100/12))
                #Costo año
                costo_carga_ano = costo_carga_mes*12

                #equipo carga
                Label(self.top_costos, text = self.combo_equipo_carga.get(), font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 2, pady = 5, padx = 6)
                #cantidad equipo carga
                Label(self.top_costos, text = '1').grid(column = 1, row = 2, pady = 5, padx = 6)
                #costo equipo carga mes
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_carga_mes))).grid(column = 2, row = 2,  pady = 5, padx = 6)
                #costo equipo carga año
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_carga_ano))).grid(column = 3, row = 2,  pady = 5, padx = 6)
            else:
                #Costo mensual
                costo_carga_mes = 0
                #Costo año
                costo_carga_ano = 0



            if len(self.combo_equipo_acarreo.get()) != 0:

                #costo_acarreo
                costo_acarreo = self.costo_equipos(self.combo_equipo_acarreo.get(), float(self.precio_equipo_acarreo.get()), float(self.precio_llantas_acarreo.get()), float(self.costo_operador_mes_acarreo.get()), float(self.disponibilidad_mecanica_acarreo.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()), self.servicio_tanqueo_acarreo.get())
                #Costo mensual
                costo_acarreo_mes = float(costo_acarreo)*((float(self.horas_disponibles())*float(self.disponibilidad_mecanica_acarreo.get())/100/12))*int(camiones)
                #Costo año
                costo_acarreo_ano = costo_acarreo_mes*12

                #equipo acarreo
                Label(self.top_costos, text = self.combo_equipo_acarreo.get(), font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 3, pady = 5, padx = 6)
                #cantidad equipo acarreo
                Label(self.top_costos, text = str(camiones)).grid(column = 1, row = 3, pady = 5, padx = 6)
                #costo equipo acarreo mes
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_acarreo_mes))).grid(column = 2, row = 3,  pady = 5, padx = 6)
                #costo equipo acarreo año
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_acarreo_ano))).grid(column = 3, row = 3,  pady = 5, padx = 6)
            else:
                #costo_acarreo
                costo_acarreo = 0
                #Costo mensual
                costo_acarreo_mes = 0
                #Costo año
                costo_acarreo_ano = 0

            if len(self.combo_equipo_adicional_1.get()) != 0:

                #Costo equipo adicional 1
                costo_equipo_adicional_1 = self.costo_equipos(self.combo_equipo_adicional_1.get(), float(self.precio_equipo_adicional_1.get()), float(self.precio_llantas_adicional_1.get()), float(self.costo_operador_mes_adicional_1.get()), float(self.disponibilidad_mecanica_adicional_1.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()), self.servicio_tanqueo_adicional_1.get())
                #Costo mes
                costo_equipo_adicional_1_mes = float(costo_equipo_adicional_1)*((float(self.horas_disponibles())*float(self.disponibilidad_mecanica_adicional_1.get())/100/12))
                #Costo año
                costo_equipo_adicional_1_ano = costo_equipo_adicional_1_mes*12

                #equipo equipo_adicional_1
                Label(self.top_costos, text = self.combo_equipo_adicional_1.get(), font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 4, pady = 5, padx = 6)
                #cantidad equipo equipo_adicional_1
                Label(self.top_costos, text = "1").grid(column = 1, row = 4, pady = 5, padx = 6)
                #costo equipo equipo_adicional_1 mes
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_1_mes))).grid(column = 2, row = 4,  pady = 5, padx = 6)
                #costo equipo equipo_adicional_1 año
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_1_ano))).grid(column = 3, row = 4,  pady = 5, padx = 6)
            else:
                costo_equipo_adicional_1 = 0
                #Costo mes
                costo_equipo_adicional_1_mes = 0
                #Costo año
                costo_equipo_adicional_1_ano = 0

            if len(self.combo_equipo_adicional_2.get()) != 0:

                #Costo equipo adicional 2
                costo_equipo_adicional_2 = self.costo_equipos(self.combo_equipo_adicional_2.get(), float(self.precio_equipo_adicional_2.get()), float(self.precio_llantas_adicional_2.get()), float(self.costo_operador_mes_adicional_2.get()), float(self.disponibilidad_mecanica_adicional_2.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()), self.servicio_tanqueo_adicional_2.get())
                #Costo mes
                costo_equipo_adicional_2_mes = float(costo_equipo_adicional_2)*((float(self.horas_disponibles())*float(self.disponibilidad_mecanica_adicional_2.get())/100/12))
                #Costo año
                costo_equipo_adicional_2_ano = costo_equipo_adicional_2_mes*12

                #equipo equipo_adicional_2
                Label(self.top_costos, text = self.combo_equipo_adicional_2.get(), font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 5, pady = 5, padx = 6)
                #cantidad equipo equipo_adicional_2
                Label(self.top_costos, text = "1").grid(column = 1, row = 5, pady = 5, padx = 6)
                #costo equipo equipo_adicional_2 mes
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_2_mes))).grid(column = 2, row = 5,  pady = 5, padx = 6)
                #costo equipo equipo_adicional_2 año
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_2_ano))).grid(column = 3, row = 5,  pady = 5, padx = 6)
            else:
                #Costo equipo adicional 2
                costo_equipo_adicional_2 = 0
                #Costo mes
                costo_equipo_adicional_2_mes = 0
                #Costo año
                costo_equipo_adicional_2_ano = 0


            if len(self.combo_equipo_adicional_3.get()) != 0:

                #Costo equipo adicional 3
                costo_equipo_adicional_3 = self.costo_equipos(self.combo_equipo_adicional_3.get(), float(self.precio_equipo_adicional_3.get()), float(self.precio_llantas_adicional_3.get()), float(self.costo_operador_mes_adicional_3.get()), float(self.disponibilidad_mecanica_adicional_3.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()), self.servicio_tanqueo_adicional_3.get())
                #Costo mes
                costo_equipo_adicional_3_mes = float(costo_equipo_adicional_3)*((float(self.horas_disponibles())*float(self.disponibilidad_mecanica_adicional_3.get())/100/12))
                #Costo año
                costo_equipo_adicional_3_ano = costo_equipo_adicional_3_mes*12

                #equipo equipo_adicional_3
                Label(self.top_costos, text = self.combo_equipo_adicional_3.get(), font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 7, pady = 5, padx = 6)
                #cantidad equipo equipo_adicional_3
                Label(self.top_costos, text = "1").grid(column = 1, row = 7, pady = 5, padx = 6)
                #costo equipo equipo_adicional_3 mes
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_3_mes))).grid(column = 2, row = 7,  pady = 5, padx = 6)
                #costo equipo equipo_adicional_3 año
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_3_ano))).grid(column = 3, row = 7,  pady = 5, padx = 6)
            else:
                #Costo equipo adicional 3
                costo_equipo_adicional_3 = 0
                #Costo mes
                costo_equipo_adicional_3_mes = 0
                #Costo año
                costo_equipo_adicional_3_ano = 0

            if len(self.combo_equipo_adicional_4.get()) != 0:

                #Costo equipo adicional 4
                costo_equipo_adicional_4 = self.costo_equipos(self.combo_equipo_adicional_4.get(), float(self.precio_equipo_adicional_4.get()), float(self.precio_llantas_adicional_4.get()), float(self.costo_operador_mes_adicional_4.get()), float(self.disponibilidad_mecanica_adicional_4.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()), self.servicio_tanqueo_adicional_4.get())
                #Costo mes
                costo_equipo_adicional_4_mes = float(costo_equipo_adicional_4)*((float(self.horas_disponibles())*float(self.disponibilidad_mecanica_adicional_4.get())/100/12))
                #Costo año
                costo_equipo_adicional_4_ano = costo_equipo_adicional_4_mes*12

                #equipo equipo_adicional_4
                Label(self.top_costos, text = self.combo_equipo_adicional_4.get(), font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 6, pady = 5, padx = 6)
                #cantidad equipo equipo_adicional_4
                Label(self.top_costos, text = "1").grid(column = 1, row = 6, pady = 5, padx = 6)
                #costo equipo equipo_adicional_4 mes
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_4_mes))).grid(column = 2, row = 6,  pady = 5, padx = 6)
                #costo equipo equipo_adicional_4 año
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_4_ano))).grid(column = 3, row = 6,  pady = 5, padx = 6)
            else:
                #Costo equipo adicional 4
                costo_equipo_adicional_4 = 0
                #Costo mes
                costo_equipo_adicional_4_mes = 0
                #Costo año
                costo_equipo_adicional_4_ano = 0

            if len(self.combo_equipo_adicional_5.get()) != 0:

                #Costo equipo adicional 5
                costo_equipo_adicional_5 = self.costo_equipos(self.combo_equipo_adicional_5.get(), float(self.precio_equipo_adicional_5.get()), float(self.precio_llantas_adicional_5.get()), float(self.costo_operador_mes_adicional_5.get()), float(self.disponibilidad_mecanica_adicional_5.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()), self.servicio_tanqueo_adicional_5.get())
                #Costo mes
                costo_equipo_adicional_5_mes = float(costo_equipo_adicional_5)*((float(self.horas_disponibles())*float(self.disponibilidad_mecanica_adicional_5.get())/100/12))
                #Costo año
                costo_equipo_adicional_5_ano = costo_equipo_adicional_5_mes*12

                #equipo equipo_adicional_5
                Label(self.top_costos, text = self.combo_equipo_adicional_5.get(), font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 8, pady = 5, padx = 6)
                #cantidad equipo equipo_adicional_5
                Label(self.top_costos, text = "1").grid(column = 1, row = 8, pady = 5, padx = 6)
                #costo equipo equipo_adicional_5 mes
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_5_mes))).grid(column = 2, row = 8,  pady = 5, padx = 6)
                #costo equipo equipo_adicional_5 año
                Label(self.top_costos, text = "${:,.2f}". format(int(costo_equipo_adicional_5_ano))).grid(column = 3, row = 8,  pady = 5, padx = 6)
            else:
                #Costo equipo adicional 5
                costo_equipo_adicional_5 = 0
                #Costo mes
                costo_equipo_adicional_5_mes = 0
                #Costo año
                costo_equipo_adicional_5_ano = 0

            #TOTALES
            #Total mes
            costo_total_mes = costo_acarreo_mes + costo_carga_mes + costo_equipo_adicional_1_mes + costo_equipo_adicional_2_mes + costo_equipo_adicional_3_mes + costo_equipo_adicional_4_mes + costo_equipo_adicional_5_mes
            #Total año
            costo_total_ano = costo_acarreo_ano + costo_carga_ano + costo_equipo_adicional_1_ano + costo_equipo_adicional_2_ano + costo_equipo_adicional_3_ano + costo_equipo_adicional_4_ano + costo_equipo_adicional_5_ano

            #label total
            Label(self.top_costos, text = 'TOTAL', font = ('Helvetica', '9', 'bold')).grid(column = 0, row = 9, pady = 5, padx = 6)
            #total cantidad
            Label(self.top_costos, text = "x" , font = ('Helvetica', '9', 'bold')).grid(column = 1, row = 9, pady = 5, padx = 6)
            #total mes
            Label(self.top_costos, text = "${:,.2f}". format(int(costo_total_mes)), font = ('Helvetica', '9', 'bold')).grid(column = 2, row = 9, pady = 5, padx = 6)
            #total año
            Label(self.top_costos, text = "${:,.2f}". format(int(costo_total_ano)), font = ('helvetica', '9', 'bold')).grid(column = 3, row = 9, pady = 5, padx = 6)

            top_costos.grab_set()
 


        else:
            error = Toplevel(self.root)
            Label(error, text = 'Asegúrese de: ').grid(column = 0, row = 0, pady = 1, padx = 10, sticky = "w")
            Label(error, text = '- Llenar todos los campos con *').grid(column = 0, row = 1, pady = 1, padx = 10, sticky = 'w')
            Label(error, text = '- Introducir sólo valores numéricos').grid(column = 0, row = 2, pady = 1, padx = 10, sticky = 'w')

            Button(error, text = 'Aceptar', command = (lambda: error.destroy())).grid(column = 0, row = 3, pady = (2, 7))
            error.grab_set()



    def costo(self):
        self.calculo_camiones(self.combo_equipo_carga.get(), self.combo_equipo_acarreo.get(), float(self.disponibilidad_mecanica_carga.get()))
        #self.costo_equipos(self.combo_equipo_carga.get(), float(self.precio_equipo_carga.get()), float(self.precio_llantas_carga.get()), float(self.costo_operador_mes_carga.get()), float(self.disponibilidad_mecanica_carga.get()), float(self.costo_diesel.get()), float(self.costo_lubricante_carter.get()), float(self.costo_lubricante_hidraulico.get()), float(self.costo_lubricante_transmision.get()), self.servicio_tanqueo_carga.get())

if __name__ == '__main__':
    root = Tk()

    app = Costos(root)
    root.mainloop()
