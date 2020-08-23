import pyautogui
import tkinter as tk

root=tk.Tk()
canvas=tk.Canvas(root,width=300,height=300)
canvas.pack()


def takeScreenShot():
    my=pyautogui.screenshot()
    my.save('screen2.png')
    print("Saved")

mybutton=tk.Button(text='TakeScreeShot',command=takeScreenShot(),bg='green' ,fg='white',font=10)
canvas.create_window(150,150,window=mybutton)

root.mainloop()
