



def draw_pixel(i,j):
    tableau.create_rectangle((i,j)*2, outline= "red")


def colorie_pixel(event):
    draw_pixel(event.x,event.y)




Height = 500
Width = 500
import tkinter as tk
racine = tk.Tk()
racine.title("les clic clic")
tableau = tk.Canvas(racine, height=Height, width=Width,bg="black")
tableau.grid(column=0, row=0)
tableau.bind("<Button-1>",colorie_pixel)
racine.mainloop()