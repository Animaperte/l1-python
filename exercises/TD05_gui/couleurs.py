import tkinter as tk
from tkinter.constants import FLAT
import tkinter.font as font

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

fenetre = tk.Tk()
fenetre.title("Mon dessin")
fenetre.geometry("375x256")
monCanvas = tk.Canvas(fenetre, width=256, height=256, bg='black', borderwidth=1, relief='flat')
monCanvas.grid()
monCanvas.place(x=80, y=0)
f = font.Font(size=40)

bouton1 = tk.Button(fenetre, text="Aléatoire", bg='white', fg='blue')
bouton1.grid()
bouton2 = tk.Button(fenetre, text="Dégradé gris", bg='white', fg='blue')
bouton2.grid()
bouton3 = tk.Button(fenetre, text="Dégradé 2D ", bg='white', fg='blue')
bouton3.grid()
bouton1.place(y=0)
bouton2.place(y=50)
bouton3.place(y=100)
fenetre.mainloop()