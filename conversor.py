from tkinter import *
from tkinter import messagebox

def pulgadas_a_milimetros():
    milimetros = pulgadas.get() * 25.40
    message = f"{pulgadas.get()} pulgadas equivalen a {milimetros} milímetros."
    messagebox.showinfo("Resultado", message)

def yardas_a_metros():
    metros = yardas.get() * 0.9144
    message = f"{yardas.get()} yardas equivalen a {metros} metros."
    messagebox.showinfo("Resultado", message)

def millas_a_kilometros():
    kilometros = millas.get() * 1.6093
    message = f"{millas.get()} millas equivalen a {kilometros} kilómetros."
    messagebox.showinfo("Resultado", message)

def limpiar_campos():
    """Elimina widgets anteriores para que no se superpongan"""
    for widget in frame.winfo_children():
        widget.destroy()

def conversor():
    global pulgadas, yardas, millas
    limpiar_campos()

    if opcion.get() == 1:
        Label(frame, text="Ingrese la cantidad de pulgadas a convertir: ").grid(row=0, column=0, padx=10, pady=5)
        pulgadas = IntVar()
        Entry(frame, textvariable=pulgadas).grid(row=0, column=1, padx=10, pady=5)
        Button(frame, text="Convertir", command=pulgadas_a_milimetros).grid(row=1, column=0, columnspan=2, pady=5)

    elif opcion.get() == 2:
        Label(frame, text="Ingrese la cantidad de yardas a convertir: ").grid(row=0, column=0, padx=10, pady=5)
        yardas = IntVar()
        Entry(frame, textvariable=yardas).grid(row=0, column=1, padx=10, pady=5)
        Button(frame, text="Convertir", command=yardas_a_metros).grid(row=1, column=0, columnspan=2, pady=5)

    elif opcion.get() == 3:
        Label(frame, text="Ingrese la cantidad de millas a convertir: ").grid(row=0, column=0, padx=10, pady=5)
        millas = IntVar()
        Entry(frame, textvariable=millas).grid(row=0, column=1, padx=10, pady=5)
        Button(frame, text="Convertir", command=millas_a_kilometros).grid(row=1, column=0, columnspan=2, pady=5)

interfaz = Tk()
interfaz.geometry("500x200+650+400")
interfaz.title("Conversor de Unidades")

Label(interfaz, text="Seleccione la opción que desea: ").pack(anchor=W, padx=10, pady=5)

opcion = IntVar()
Radiobutton(interfaz, text="Pulgadas a milímetros", value=1, variable=opcion, command=conversor).pack(anchor=W, padx=20)
Radiobutton(interfaz, text="Yardas a metros", value=2, variable=opcion, command=conversor).pack(anchor=W, padx=20)
Radiobutton(interfaz, text="Millas a kilómetros", value=3, variable=opcion, command=conversor).pack(anchor=W, padx=20)

frame = Frame(interfaz)
frame.pack(pady=10)

interfaz.mainloop()
