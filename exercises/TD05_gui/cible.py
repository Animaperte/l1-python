import tkinter as tk
from tkinter.constants import FLAT, N
import tkinter.font as font
from random import randint
from turtle import width


n0 = int(input("nombre de cercles"))
fenetre = tk.Tk()
fenetre.title("Mon dessin")
w = 900
h = 900
monCanvas = tk.Canvas(fenetre, width=w, height=h, bg='black', borderwidth=1, relief='flat')


monCanvas.grid()
xm = w/2
ym = h/2

yq = w - ym
xq = h - xm

zz = 0
colord = ['blue', 'green', 'cyan', 'yellow', 'magenta', 'red']
for i in range(n0):
    xpi = xm/n0*i
    ypi = ym/n0*i
    xqi = w - i*(xm)/n0
    yqi = h - i*(ym)/n0
    monCanvas.create_oval(xpi, ypi, xqi, yqi, width=1, fill=colord[zz])
    zz = zz + 1
    if zz == 6:
        zz = 0




fenetre.mainloop()