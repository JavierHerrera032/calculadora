import tkinter as tk
from tkinter import messagebox

# Función para agregar números y operaciones en la pantalla
def click(boton):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(boton))

# Función para limpiar la pantalla
def clear():
    entrada.delete(0, tk.END)

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())  # Evalúa la expresión ingresada
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except ZeroDivisionError:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error: División entre 0")
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear el campo de entrada para mostrar los números y el resultado
entrada = tk.Entry(ventana, width=20, borderwidth=5, font=('Arial', 18), justify='right')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones de la calculadora
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '=',
    '+'
]

# Crear un ciclo para posicionar los botones en una cuadrícula
fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        tk.Button(ventana, text=boton, padx=30, pady=20, font=('Arial', 14),
                  command=calcular).grid(row=fila, column=columna)
    elif boton == 'C':
        tk.Button(ventana, text=boton, padx=30, pady=20, font=('Arial', 14),
                  command=clear).grid(row=fila, column=columna)
    else:
        tk.Button(ventana, text=boton, padx=30, pady=20, font=('Arial', 14),
                  command=lambda b=boton: click(b)).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Iniciar el bucle principal de la ventana
ventana.mainloop()
