from tkinter import *
from PIL import Image,ImageTk


app=Tk()
app.title("my app")
app.geometry("1200x864")
app.configure(background="skyblue")
bg_image=Image.open("dia.png")
test_img=ImageTk.PhotoImage(bg_image)












bg_lb=Label(app,image=test_img)
bg_lb.place(x=0,y=0,relwidth=1,relheight=1)
























app.mainloop()
