import tkinter as tk
from tkinter.constants import FLAT
import tkinter.font as font
from random import randint

x0 = randint(0,800)
y0 = randint(0,600)
a0 = randint(0,800)
b0 = randint(0,600)
c0 = randint(0,800)
d0 = randint(0,600)

color = 'blue'
fenetre = tk.Tk()
fenetre.title("Mon dessin")
fenetre.geometry("1024x768")
monCanvas = tk.Canvas(fenetre, width=1000, height=768, bg='black', borderwidth=1, relief='flat')
monCanvas.grid()
monCanvas.place(x=100, y=100)
f = font.Font(size=40)
def myfunction():
    monCanvas.create_oval(x0, y0, x0+100, y0+100, width=15, fill=color)

def mysecondfunction():
    monCanvas.create_rectangle(a0, b0, a0+100, b0+100, width=5, fill=color)

def mythirdfunction():
    c1 = c0 + 100
    d1 = d0 + 100
    #monCanvas.create_rectangle(c0, d0, c1, d1, width=5, fill='black')
    monCanvas.create_line(c1, d0, c0, d1, width = 5, fill = color )
    monCanvas.create_line(c1, d1, c0, d0, width = 5, fill = color )
color = "blue"
def anotherfunction():
    global color
    color = str(input("Choisir une couleur"))
    if color != "cyan":
        color = str(input("Choisir une couleur"))
    elif color != "blue":
        color = str(input("choisir une couleur"))
    elif color != "red":
        color = str(input("choisir une couleur"))
    elif color != "yellow":
        color = str(input("choisir une couleur"))
    elif color != "white":
        color = str(input("choisir une couleur"))
    elif color != "green":
        color = str(input("choisir une couleur"))
    elif color != "black":
        color = str(input("choisir une couleur"))

bouton1 = tk.Button(fenetre, text="Choisir une couleur", borderwidth=7, bg='blue', fg='white', relief='sunken', command=anotherfunction)
bouton1['font'] = f
bouton1.grid()
bouton2 = tk.Button(fenetre, text="          Cercle         ", borderwidth=3, bg='red', fg='white', command=myfunction)
bouton2.grid()
bouton3 = tk.Button(fenetre, text="            Carré         ", bg='red', fg='white', command=mysecondfunction)
bouton3.grid()
bouton4 = tk.Button(fenetre, text="            Croix         ", bg='red', fg='white', command=mythirdfunction)
bouton4.grid()
bouton1.place(x=325, y=0)
bouton2.place(y=200)
bouton3.place(y=400)
bouton4.place(y=600)
fenetre.mainloop()