import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 300
x1 = 300
y1 = 100
y2 = 300
y = CANVAS_HEIGHT / 2
canvas.create_line(x0, y1, x1, y2)
canvas.create_oval((x0 + x1) / 2 - 50, y + 150, (x0 + x1) / 2 + 50, y + 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y - 50, (x0 + x1) / 2 + 50, y - 150)
    
# Fin de votre code

canvas.grid()
root.mainloop()
