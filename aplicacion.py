##importaciones
import tkinter as tk
from tkinter import Frame
import tensorflow as tf
import numpy as np


##definimos las listas con los ejemplos que la ia va a usar para aprender
celsiuslist= [-40,-10,0,8,15,22,38]
farenheitlist= [-40,14,32,46,59,72,100]
celsius= np.array(celsiuslist, dtype=float)
farenheit= np.array(farenheitlist,dtype=float)

##definimos la ia

capa= tf.keras.layers.Dense(units=1, input_shape=[1])
modelo= tf.keras.Sequential([capa])

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1),loss='mean_squared_error')

###historial=modelo.fit(celsius,farenheit,epochs=x, verbose=False)


##definimos las funciones

"""
##
# ignorar por ahora
# def agregaraC():
    try:
        cent=  ventanaingresarcent.get()
        cent2= float(cent)
        np.append(gradoscentigrados,cent2)
    except ValueError:
        pass

def agregaraf():
    try:
        far=  ventanaingresarfar.get()
        far2= float(far)
        np.append(gradosfarenheit,far2)
    except ValueError:
        pass
"""

def procesar():
    x= int(cantenviar.get())
    historial=modelo.fit(celsius,farenheit,epochs=x, verbose=False)
    y=int(ventanaingresarcent.get())
    resultado= modelo.predict([np.array([y])])
    valorcalculado.config(text=round(float(resultado[0]),4))

#creo la ventana
ventana= tk.Tk()
ventana.title("1er Aplicacion de IA")
ventana.configure(background= "lightblue")
ventana.geometry("800x800")
rotulo= tk.Label(ventana, text= "Aprendiendo de IA!",font=("swiss", 30, "bold"),bg= "lightblue")
rotulo.pack()
##creo los frames
frame1= Frame(ventana,bg='dodger blue',pady=10,relief=tk.GROOVE)
frame1.pack(expand=True,fill='both')

frame2=Frame(ventana,bg='cadet blue',pady=20,relief=tk.GROOVE)
frame2.pack(expand=True,fill='both')

##breve explicacion de la aplicacion
rotulo4=tk.Label(frame1, text='Vamos a demostrar como funciona una inteligencia artificial', font=("arial",12),bg="cadet blue",pady=10,padx=10,relief=tk.GROOVE)
rotulo4.pack()
rotulo7= tk.Label(frame1, text= "En esta aplicacion tenemos cargadas las siguientes listas\n La primera con grados celcius, celsiuslist= [-40,-10,0,8,15,22,38],\n y la segunda con grados farenheit', farenheitlist= [-40,14,32,46,59,72,100]", font=("arial",12),bg="cadet blue",pady=10,padx=10,relief=tk.GROOVE)
rotulo7.pack()
rotulo6=tk.Label(frame1, text='Lo que hace este programa mediante una funcion incorporada del modulo tensorflow,\n es comparar las listas, ya que los valores en cada posicion, son equivalencias entre grados F y C', font=("arial",10),bg="cadet blue",pady=10,padx=12,relief=tk.GROOVE)
rotulo6.pack()
##elementos dentro de la aplicacion
rotulo1=tk.Label(frame2, text='Cantidad de veces que vas a entrenar la IA', font=("arial",20),bg="sky blue",pady=10,padx=10,relief=tk.GROOVE)
rotulo1.pack()
cantenviar= tk.Entry(frame2,text="Ingresar cantidad a calcular", font=("arial",20),bg="azure3",relief=tk.SUNKEN)
cantenviar.pack()
rotulo2=tk.Label(frame2, text='Grados celcius que se van a calcular a grados farenheit',bg="sky blue", font=("arial",20),pady=10, padx=10,relief=tk.GROOVE)
rotulo2.pack()
ventanaingresarcent= tk.Entry(frame2, text="Ingrese los grados C",font=("arial",20),bg="azure3",relief=tk.SUNKEN)
ventanaingresarcent.pack()
procesar= tk.Button(frame2,text="calcular!", font=("arial",20), bg="light steel blue", command=procesar,pady=10, padx=10,relief=tk.GROOVE)
procesar.pack()
rotulo3=tk.Label(frame2, text='Grados Farenheit calculados', font=("arial",20),bg="sky blue",pady=10, padx=10,relief=tk.GROOVE)
rotulo3.pack()
valorcalculado= tk.Label(frame2, text="",font=("arial",20), bg="lavender",pady=10,padx=10,width=20,relief=tk.GROOVE)
valorcalculado.pack()

ventana.mainloop()
