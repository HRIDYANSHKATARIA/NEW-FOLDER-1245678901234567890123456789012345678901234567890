from tkinter import *
import random

root = Tk()

root.title("Password Generator")
root.geometry("400x400")

label = Label(root)

array_3d = [[['1','2','3','4','5','6','7','8','9','0'],["Head","Tail"],["A","B","C","D","E","F"]]]

def New_Password():
    random1 = random.randint(0,9)
    random2 = random.randint(0,1)
    random3 = random.randint(0,5)
    letter1 = str(array_3d[0][0][random1])
    letter2 = str(array_3d[0][1][random2])
    letter3 = str(array_3d[0][2][random3])
    label["text"] = letter1+""+letter2+""+letter3

btn =Button(root,text="Generate New Password",command=New_Password)

btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()