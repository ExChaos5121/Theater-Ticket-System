import tkinter as tk 
from tkinter import *
from tkinter import messagebox



class AccountGUI: 
    def __init__(acct):
        


        acct.account_window = tk.Tk()
        acct.account_window.title ("Account Creation")
        acct.account_window.minsize (width = 100, height = 100)



        acct.account_window.columnconfigure (0, minsize = 200)
        acct.account_window.columnconfigure (1, minsize = 200)
        acct.account_window.rowconfigure (0, minsize = 50)
        acct.account_window.rowconfigure (1, minsize = 50)
        acct.account_window.rowconfigure (2, minsize = 50)
        acct.account_window.rowconfigure (3, minsize = 50)
        acct.account_window.resizable (height = False, width = False)
        


        acct.username_txt = tk.Label(acct.account_window, text = " User Name: ", \
                      width = 15, font=("MS Sans Serif",12))
        acct.username_txt.grid (row = 0, column = 0)
        


        acct.account_window.username_entry = tk.Entry(acct.account_window, \
                      width = 15, justify='right', font=("MS Sans Serif",12))
        acct.account_window.username_entry.grid(row=0, column=1)
        acct.account_window.username_entry.focus_force()

        


        acct.username_txt = tk.Label(acct.account_window, text = " Create a "
                                    "password of at least nine (9) characters, \n"
                                    "that contains at least one digit, one uppercase, \n" 
                                    "and one lowercase letter.",  font=("MS Sans Serif",12))
        acct.username_txt.grid (row = 1, column = 0, columnspan = 2)
        
        

        acct.password_txt = tk.Label(acct.account_window, text = " Password: ", \
                      width = 15, font=("MS Sans Serif",12))
        acct.password_txt.grid (row = 2, column = 0)

        

        acct.account_window.password_entry = tk.Entry(acct.account_window, \
                      width = 15, justify='right', font=("MS Sans Serif",12))
        acct.account_window.password_entry.grid(row=2, column=1)
        acct.account_window.password_entry.focus_force()
        

     
        acct.login_button = tk.Button(acct.account_window, text = ' User Login ', width = 16, \
                                     font = ("MS Sans Serif",12), command = acct.verify_new_user)
        acct.login_button.grid(row = 3,column = 1, pady = 15)

        

        acct.quit_button = tk.Button(acct.account_window, text = ' Cancel ', width = 16, \
                                     font = ("MS Sans Serif",12), \
        command = acct.account_window.destroy)
        acct.quit_button.grid(row = 3,column = 0)

        
        
    def verify_new_user(acct):
        valid = True
        newUser =  (acct.account_window.username_entry.get())
        
        try:
            userDataFile = open("acct_user_names.txt", "r")

            for userTemp in userDataFile:
                
                if newUser == userTemp.rstrip():
                    valid = False


            userDataFile.close()

            if (valid == False):
                messagebox.showinfo("Invalid User Name", "That user name already exists.")
                acct.account_window.username_entry.delete(0,END)
                acct.account_window.username_entry.focus_force()
                accct.account_window.lift()
                
            else:
                acct.verify_new_pass(newUser)

        except IOError:
            print("No File exists")

    def verify_new_pass(acct, user):
         valid = False
         txt = (acct.account_window.password_entry.get())
         
         
         

         if (len(txt) >= 9 and any(x.isupper() for x in txt) and any(x.islower() for x in txt) \
                and any(x.isdigit() for x in txt)):
             
             userFile = open("acct_user_names.txt", "a")
             userFile.write(user + "\n")
             userFile.close()

             passwordFile = open("acct_user_passwords.txt", "a")
             passwordFile.write(txt + "\n")
             passwordFile.close()
             messagebox.showinfo("Account Creation", "Account Successfully Created.")
             acct.account_window.lift()
             acct.account_window.destroy()
             
         else:
             messagebox.showinfo( "Password Validation", '"' + txt + '"' + "is not a valid, \n"
                                        "password.")
             acct.account_window.lift()
             acct.account_window.destroy()

        

                  

          
           



