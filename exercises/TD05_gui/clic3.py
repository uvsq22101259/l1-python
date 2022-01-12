def draw_pixel(i,j):
    tableau.create_rectangle((i,j)*2, outline= "red")


def colorie_pixel(event):
    draw_pixel(event.x,event.y)
    tableau.create_oval((event.x-50,event.y-50),(event.x+50,event.y+50), fill = "blue")
def ligne(event):
    global a
    a.append(event.x)
    a.append(event.y)
    
    if len(a)== 4 :
        if a[0] < 250 and a[2] < 250 or a[0] > 250 and a[2] > 250:
            tableau.create_line((a[0],a[1]),(a[2],a[3]),fill="blue")
            a = []
        else:
            tableau.create_line((a[0],a[1]),(a[2],a[3]),fill="red")
            a = []

    

a=[]

Height = 500
Width = 500
import tkinter as tk
racine = tk.Tk()
racine.title("les clic clic")
tableau = tk.Canvas(racine, height=Height, width=Width,bg="black")
tableau.grid(column=0, row=0)
tableau.bind("<Button-1>",ligne)
tableau.create_line((250,0),(250,Height), fill = "white")
racine.mainloop()