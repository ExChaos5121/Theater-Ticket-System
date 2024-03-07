import tkinter as tk
 
class Window:
    def __init__(self, master):
        self.master = master
 
        # Frame
        self.frame = tk.Frame(self.master, width = 200, height = 200)
        self.frame.pack()
 
        # Radiobutton
        self.var1 = tk.IntVar()
 
        self.radio = tk.Radiobutton(self.frame, variable = self.var1, value = 1, text = "Option 1", command = self.submit)
        self.radio.place(x = 30, y = 30)
 
        self.radio2 = tk.Radiobutton(self.frame, variable = self.var1, value = 2, text = "Option 2", command = self.submit)
        self.radio2.place(x = 30, y = 60)
 
 
    def submit(self):
        if self.var1.get() == 1:
            print("Option 1 was selected")
        elif self.var1.get() == 2:
            print("Option 2 was selected")
 
 
root = tk.Tk()
root.title("Tkinter")
 
window = Window(root)
root.mainloop()
