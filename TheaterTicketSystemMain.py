import tkinter as tk
from tkinter import messagebox, DISABLED, NORMAL


import create_account
import login_window


class StartupGUI:
    def __init__(self):
        

        
        self.main_win = tk.Tk()
        self.main_win.title ("Theater Ticket System")
        self.main_win.minsize (width = 100, height = 100)


        self.main_win.columnconfigure (0, minsize = 175)
        self.main_win.columnconfigure (1, minsize = 175)
        self.main_win.columnconfigure (2, minsize = 175)
        self.main_win.rowconfigure (0, minsize = 80)
        self.main_win.rowconfigure (1, minsize = 80)
        self.main_win.rowconfigure (2, minsize = 80)
        self.main_win.resizable (height = False, width = False)

        photo = tk.PhotoImage (file = "Movie.png")
        self.LabelGIF = tk.Label (image = photo)
        self.LabelGIF.image = photo
        self.LabelGIF.place(x=0, y=0, relwidth=1, relheight=1)

    

        self.heading_label = tk.Label (text = 'Movie Theater Ticket System',\
                                      font = ("MS Sans Serif",18), fg="black")
        
        self.heading_label.grid (row = 0, column = 1,columnspan = 1)

        

        self.login_button = tk.Button (text = ' User Login ', width = 16, \
                                     font = ("MS Sans Serif",12), \
        command = self.login_window)
        self.login_button.grid (row=2,column=2)

        

        self.create_acct_button = tk.Button(text=' Create Account ', width = 16, \
                                     font=("MS Sans Serif",12), \
        command = self.create_account)
        self.create_acct_button.grid (row = 2,column = 1)
        


        self.quit_button = tk.Button(text = ' Cancel ', width = 16, \
                                     font = ("MS Sans Serif",12), \
        command = self.main_win.destroy)
        self.quit_button.grid (row = 2,column = 0)

        
    


        tk.mainloop()

        

        
        
       

       
    def create_account(self):

        self.create_acct_button.config (state = DISABLED)
        self.login_button.config (state = DISABLED)
        CreateAcctWin = create_account.AccountGUI() 
        CreateAcctWin.account_window.wait_window()
        self.create_acct_button.config (state = NORMAL)
        self.login_button.config (state = NORMAL)


    def login_window(self):
        
        self.create_acct_button.config (state = DISABLED)
        self.login_button.config (state = DISABLED)
        CreateAcctWin = login_window.LoginGUI()
        CreateAcctWin.login_window.wait_window()
        self.create_acct_button.config (state = NORMAL)
        self.login_button.config (state = NORMAL)
        
        
                                                                                                                                                                                                                                                                                   
            


   
    

  
dataAnalysis = StartupGUI ()





 

 
