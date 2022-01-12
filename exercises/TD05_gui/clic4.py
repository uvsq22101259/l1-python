



def draw_pixel(i,j):
    tableau.create_rectangle((i,j)*2, outline= "red")


def colorie_pixel(event):
    draw_pixel(event.x,event.y)

def cercle(event):
    global a
    if event.x > 250:
       a.append(tableau.create_oval((event.x-50,event.y-50),(event.x+50,event.y+50), fill = "red"))
    elif event.x == 250:
        a.append(tableau.create_oval((event.x-50,event.y-50),(event.x+50,event.y+50), fill = "green"))
    else:
        a.append(tableau.create_oval((event.x-50,event.y-50),(event.x+50,event.y+50), fill = "blue"))
    if len(a) == 9:
        for i  in a:
            tableau.itemconfig(i, fill = "yellow")
    elif len(a) == 10:
        for i in a:
            tableau.delete(i)
        a = []
        

   

a =[]
Height = 500
Width = 500
import tkinter as tk
racine = tk.Tk()
racine.title("les clic clic")
tableau = tk.Canvas(racine, height=Height, width=Width,bg="black")
tableau.grid(column=0, row=0)
tableau.bind("<Button-1>",cercle)
tableau.create_line((250,0),(250,Height), fill = "white")
racine.mainloop()
