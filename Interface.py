import tkinter as tk
from tkinter import ttk
from main import *


root = tk.Tk()
root.geometry("600x400")
root.title("Simulation")


b = tk.StringVar(value="1")
k = tk.StringVar(value="1")
M = tk.StringVar(value="1")
Tend = tk.StringVar(value="10")
deltaT = tk.StringVar(value="0.01")
T = tk.StringVar(value="2")
Amp = tk.StringVar(value="1")
shape = tk.StringVar(value="rectangle")


def simulate():
    try:
        b_val = float(b.get())
        k_val = float(k.get())
        M_val = float(M.get())
        Tend_val = float(Tend.get())
        deltaT_val = float(deltaT.get())
        T_val = float(T.get())
        Amp_val = float(Amp.get())
        shape_val = shape.get()

        simulate_system(b_val, k_val, M_val, deltaT_val, Tend_val, T_val, shape_val, Amp_val)

    except ValueError:
        print("Please enter valid numeric values.")


   

b_label = tk.Label(root, text='b', font=('calibre', 10, 'bold'))
b_entry = tk.Entry(root, textvariable=b, font=('calibre', 10, 'normal'))

k_label = tk.Label(root, text='k', font=('calibre', 10, 'bold'))
k_entry = tk.Entry(root, textvariable=k, font=('calibre', 10, 'normal'))

M_label = tk.Label(root, text='M', font=('calibre', 10, 'bold'))
M_entry = tk.Entry(root, textvariable=M, font=('calibre', 10, 'normal'))

Tend_label = tk.Label(root, text='Tend', font=('calibre', 10, 'bold'))
Tend_entry = tk.Entry(root, textvariable=Tend, font=('calibre', 10, 'normal'))

deltaT_label = tk.Label(root, text='deltaT', font=('calibre', 10, 'bold'))
deltaT_entry = tk.Entry(root, textvariable=deltaT, font=('calibre', 10, 'normal'))

T_label = tk.Label(root, text='Time period of the input signal', font=('calibre', 10, 'bold'))
T_entry = tk.Entry(root, textvariable=T, font=('calibre', 10, 'normal'))

Amp_label = tk.Label(root, text='Amplitude of the input signal', font=('calibre', 10, 'bold'))
Amp_entry = tk.Entry(root, textvariable=Amp, font=('calibre', 10, 'normal'))

shape_label = tk.Label(root, text='Input Signal Shape', font=('calibre', 10, 'bold'))
shape_combo = ttk.Combobox(root, textvariable=shape, values=["rectangle", "harmonic", "triangle"], state="readonly")
shape_combo.current(0)

sim_btn = tk.Button(root, text='Simulate', command=simulate)


b_label.grid(row=0, column=0, padx=10, pady=10)
b_entry.grid(row=0, column=1, padx=10, pady=10)

k_label.grid(row=1, column=0, padx=10, pady=10)
k_entry.grid(row=1, column=1, padx=10, pady=10)

M_label.grid(row=2, column=0, padx=10, pady=10)
M_entry.grid(row=2, column=1, padx=10, pady=10)

Tend_label.grid(row=3, column=0, padx=10, pady=10)
Tend_entry.grid(row=3, column=1, padx=10, pady=10)

deltaT_label.grid(row=4, column=0, padx=10, pady=10)
deltaT_entry.grid(row=4, column=1, padx=10, pady=10)

T_label.grid(row=5, column=0, padx=10, pady=10)
T_entry.grid(row=5, column=1, padx=10, pady=10)

Amp_label.grid(row=6, column=0, padx=10, pady=10)
Amp_entry.grid(row=6, column=1, padx=10, pady=10)

shape_label.grid(row=7, column=0, padx=10, pady=10)
shape_combo.grid(row=7, column=1, padx=10, pady=10)

sim_btn.grid(row=8, column=1, pady=20)


root.mainloop()
