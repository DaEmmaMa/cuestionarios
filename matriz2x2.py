import tkinter as tk
from tkinter import messagebox
import math

def calcular_matriz():
    try:
        # Obtener los valores de la matriz
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = float(entry_d.get())
        
        # Calcular determinante
        determinante = a * d - b * c
        
        # Preparar resultado
        resultado = f"""MATRIZ 2x2:
|{a:6.2f}  {b:6.2f}|
|{c:6.2f}  {d:6.2f}|

DETERMINANTE: {determinante:.4f}

"""
        
        # Calcular inversa si el determinante no es cero
        if determinante != 0:
            # Matriz inversa: (1/det) * |d  -b|
            #                           |-c  a|
            inv_a = d / determinante
            inv_b = -b / determinante
            inv_c = -c / determinante
            inv_d = a / determinante
            
            resultado += f"""MATRIZ INVERSA:
|{inv_a:8.4f}  {inv_b:8.4f}|
|{inv_c:8.4f}  {inv_d:8.4f}|"""
        else:
            resultado += "MATRIZ INVERSA: No existe (determinante = 0)"
        
        messagebox.showinfo("Resultados", resultado)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Matriz 2x2")
ventana.geometry("300x250")

# Título
tk.Label(ventana, text="Matriz 2x2", font=("Arial", 16, "bold")).pack(pady=10)

# Crear frame para la matriz
frame_matriz = tk.Frame(ventana)
frame_matriz.pack(pady=10)

# Etiqueta para mostrar la estructura
tk.Label(frame_matriz, text="|  a    b  |", font=("Courier", 12)).grid(row=0, column=0, columnspan=2)
tk.Label(frame_matriz, text="|  c    d  |", font=("Courier", 12)).grid(row=1, column=0, columnspan=2)

# Campos de entrada organizados como matriz
tk.Label(ventana, text="Elemento a (posición 1,1):").pack()
entry_a = tk.Entry(ventana, width=10, justify="center")
entry_a.pack(pady=2)

tk.Label(ventana, text="Elemento b (posición 1,2):").pack()
entry_b = tk.Entry(ventana, width=10, justify="center")
entry_b.pack(pady=2)

tk.Label(ventana, text="Elemento c (posición 2,1):").pack()
entry_c = tk.Entry(ventana, width=10, justify="center")
entry_c.pack(pady=2)

tk.Label(ventana, text="Elemento d (posición 2,2):").pack()
entry_d = tk.Entry(ventana, width=10, justify="center")
entry_d.pack(pady=2)

# Botón calcular
tk.Button(ventana, text="CALCULAR DETERMINANTE E INVERSA", 
          command=calcular_matriz, bg="#2196F3", fg="white", 
          font=("Arial", 11)).pack(pady=15)

# Ejecutar aplicación
ventana.mainloop()