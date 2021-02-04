# importing tkinter and tkinter.ttk 
# and all their functions and classes 
from tkinter import * 
from tkinter.ttk import *
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
  
root = Tk() 
root.geometry('200x100') 
  
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
  
    
btn = Button(root, text ='Open', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10) 
  
mainloop() 
