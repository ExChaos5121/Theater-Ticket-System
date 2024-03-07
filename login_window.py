import tkinter as tk 
from tkinter import messagebox, DISABLED
from datetime import datetime
from functools import partial
import numpy as np
import matplotlib.pyplot as plt
import create_account



class LoginGUI:
    def __init__(log):

        



        log.login_window = tk.Tk()
        log.login_window.title ("Login Window")
        log.login_window.minsize (width = 100, height = 100)
        
        

        log.login_window.columnconfigure(0, minsize = 150)
        log.login_window.columnconfigure(1, minsize = 150)
        log.login_window.rowconfigure(0, minsize = 50)
        log.login_window.rowconfigure(1, minsize = 50)
        log.login_window.rowconfigure(2, minsize = 50)
        log.login_window.rowconfigure(3, minsize = 50)
        log.login_window.rowconfigure(4, minsize = 50)
        log.login_window.resizable(height = False, width = False)

        

        log.heading_label = tk.Label(log.login_window, text = 'Account Login ',\
                                      font = ("MS Sans Serif",18), fg="black")
        
        log.heading_label.grid(row = 0, column = 0,columnspan = 2)

        
        
        log.username_txt = tk.Label(log.login_window, text = " User Name: ", \
                     font = ("MS Sans Serif",12))
        log.username_txt.grid (row = 1, column = 0, columnspan = 1)

        


        log.login_window.username_entry = tk.Entry(log.login_window, \
                      width = 15, justify='right', font=("MS Sans Serif",12))
        log.login_window.username_entry.grid(row=1, column=1)
        log.login_window.username_entry.focus_force()

        


        log.password_txt = tk.Label(log.login_window, text = " Password: ", \
                                    font = ("MS Sans Serif",12))
        log.password_txt.grid (row = 2, column = 0)

        

        log.login_window.password_entry = tk.Entry(log.login_window, \
                      width = 15, justify='right', font=("HMS Sans Serif",12))
        log.login_window.password_entry.bind('<Return>', log.verify_user)
        log.login_window.password_entry.grid(row=2, column=1)
        log.login_window.password_entry.focus_force()

        
     
        log.login_button = tk.Button(log.login_window, text = ' User Login ', width = 16, \
                                     font = ("MS Sans Serif",12))
        log.login_button.bind('<Button-1>', log.verify_user)                           
        log.login_button.grid(row = 4,column = 1,  padx = 20, pady = 20)

        

        log.quit_button = tk.Button(log.login_window, text = ' Cancel ', width = 16, \
                                     font = ("MS Sans Serif",12), \
        command = log.login_window.destroy)
        log.quit_button.grid(row = 4,column = 0, padx = 20, pady = 20)

        


    def verify_user (log, event):

        usernameFile = open("acct_user_names.txt", "r")
        passwordFile = open("acct_user_passwords.txt", "r")
        usern = (log.login_window.username_entry.get())
        passw = (log.login_window.password_entry.get())

        user_list = []
        pass_list = []

        con_list = usernameFile.readlines()
        ocon_list = passwordFile.readlines()

        element = '\n'

        for element in con_list:
            user_list.append(element.strip())

        for element in ocon_list:
            pass_list.append(element.strip())

        usernameFile.close()
        passwordFile.close()

        try:
            
            

            user_index = user_list.index(usern)

            pass_index = pass_list.index(passw)
            
            if (pass_index == user_index):

                
                 
                
                if(usern == ('Manager')):

                   

                    

                    log.gui_win = tk.Tk()
                    log.gui_win.title ("Theater Ticket System")
                    log.gui_win.minsize (width = 100, height = 100)


                    log.gui_win.columnconfigure (0, minsize = 175)
                    log.gui_win.columnconfigure (1, minsize = 175)
                    log.gui_win.columnconfigure (2, minsize = 175)
                    log.gui_win.rowconfigure (0, minsize = 80)
                    log.gui_win.rowconfigure (1, minsize = 80)
                    log.gui_win.rowconfigure (2, minsize = 80)
                    log.gui_win.rowconfigure (3, minsize = 80)
                    log.gui_win.resizable (height = False, width = False)

                    log.heading_label = tk.Label (log.gui_win, text = 'Movie Theater Price Manager System',\
                                      font = ("MS Sans Serif",18), fg="black")
        
                    log.heading_label.grid (row = 0, column = 1)

                    log.select_txt = tk.Label(log.gui_win, text = " Select a showtime: ", \
                      width = 15, font=("MS Sans Serif",12))
                    log.select_txt.grid (row = 1, column = 1)

                    log.theat_var = tk.IntVar()

                    log.theat_var.set(1)

                    log.data_button = tk.Button(log.gui_win, text = ' View seating data ', width = 16, \
                                                font = ("MS Sans Serif",12), command = log.data_window)
                    log.data_button.grid(row = 2,column = 1, padx = 20, pady = 20)

                    
                    
                    log.matinee_press = tk.Radiobutton(log.gui_win, text = " Matinee Pricing",\
                                                       font=("Arial",12), variable=log.theat_var, value = 1 , command = log.matprice_chosen)
                    log.matinee_press.grid(row=3, column=0)
                   
                    log.evening_press = tk.Radiobutton(log.gui_win, text = " Evening Pricing", \
                                                    font=("Arial",12), variable=log.theat_var, value = 2 , command = log.evenprice_chosen)
                    log.evening_press.grid(row=3, column=2)

                    log.gui_win.destroy
            
                if(usern != ('Manager')):

                    
                    

                    managerFile = open("manager_choice.txt", "r")

                    manager_list = []

                    dummy_list = managerFile.readlines()
        
                    element = '\n'

                    for element in dummy_list:
                        manager_list.append(element.strip())

       
                    managerFile.close()

                    strings = [str(integer) for integer in manager_list]
                    string = "".join(strings)
                    checker = int(string)    

                    if(checker == 1):
                        log.eveningGUI()
                    else:
                        log.matineeGUI()

                    

                    
                                 
            else:
                
                log.error_txt = tk.Label(log.login_window, text = " Username or Password is invalid", \
                                            font=("MS Sans Serif",12), fg = 'red')
                log.error_txt.grid (row = 3, column = 0, columnspan = 2)
            
            
        except ValueError:
            
            log.error_txt = tk.Label(log.login_window, text = " Username or Password is invalid", \
                                            font=("MS Sans Serif",12), fg = 'red')
            log.error_txt.grid (row = 3, column = 0, columnspan = 2)


    def data_window(log):
        
        
        log.data_button = tk.Button(log.gui_win, text = ' View seating data ', width = 16, \
                                    font = ("MS Sans Serif",12), state = DISABLED)
        log.data_button.grid(row = 2,column = 1, padx = 20, pady = 20)

       
        
        plt.style.use('ggplot')
        
        x = ['101 - 105', '108 - 110', '106, 107 & 111, 112', '205, 206, 207', '203, 204, & 208, 209', '201, 202 & 210, 211']

            
        seatingFile = open("seat_availability.txt", "r")
       
        
        seating_list = []

        dummy_list = seatingFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            
            
                
            seating_list.append(element.strip())
            
        seatingFile.close()
        

        integer_map = map(int, seating_list)

        seats = list(integer_map)

        sect101 = 150 - seats[0]
        sect108 = 120 - seats[1]
        sect106 = 200 - seats[2]
        sect205 = 80 - seats[3]
        sect203 = 120 - seats[4]
        sect201 = 80 - seats[5]

        totalTicketsSold = sect101 + sect108 + sect106 + sect205 + sect203 + sect201

        totalSales = 0

        
        managerFile = open("manager_choice.txt", "r")

        manager_list = []

        dummy_list = managerFile.readlines()

        element = '\n'

        for element in dummy_list:

            manager_list.append(element.strip())

        managerFile.close()

        strings = [str(integer) for integer in manager_list]

        string = "".join(strings)

        checker = int(string)

        if(checker == 1):
            
            eveningFile = open("evening_pricing.txt", "r")

            evening_list = []

            dummy_list = eveningFile.readlines()

            element = '\n'

            for element in dummy_list:

                evening_list.append(element.strip())

       
            eveningFile.close()

            integer_map = map(float, evening_list)

            sales = list(integer_map)

            sectSale101 = sect101 * sales[0]
            sectSale108 = sect108 * sales[1]
            sectSale106 = sect106 * sales[2]
            sectSale205 = sect205 * sales[3]
            sectSale203 = sect203 * sales[4]
            sectSale201 = sect201 * sales[5]

            totalSales = sectSale101 + sectSale108 + sectSale106 + sectSale205 + sectSale203 + sectSale201


            

        else:
            
            matineeFile = open("matinee_pricing.txt", "r")

            matinee_list = []

            dummy_list = matineeFile.readlines()

            element = '\n'

            for element in dummy_list:

                matinee_list.append(element.strip())

       
            matineeFile.close()
            

            sectSale101 = sect101 * matinee_list[0]
            sectSale108 = sect108 * matinee_list[1]
            sectSale106 = sect106 * matinee_list[2]
            sectSale205 = sect205 * matinee_list[3]
            sectSale203 = sect203 * matinee_list[4]
            sectSale201 = sect201 * matinee_list[5]
            

            totalSales = sectSale101 + sectSale108 + sectSale106 + sectSale205 + sectSale203 + sectSale201
            

        totalTickets = str(totalTicketsSold)
        
        sect101 = str(sect101)
        sect108 = str(sect108)
        sect106 = str(sect106)
        sect205 = str(sect205)
        sect203 = str(sect203)
        sect201 = str(sect201)

        
        sold_list = [sect101, sect108, sect106, sect205, sect203, sect201]
        x_pos = [i for i, _ in enumerate(x)]
        plt.bar(x_pos, seats, color='green')
        plt.xlabel("Sections")
        plt.ylabel("Tickets left")
        plt.title("Number of tickets left in each section")
        plt.figtext( 0.2,0.005 ,"Tickets sold: " + totalTickets, fontsize = 10)
        plt.figtext( 0.3,0.005 ,"Total sales: $" + f'{totalSales:,}', fontsize = 10)
        plt.text(0, 10, sect101 +' Sold', horizontalalignment='center')
        plt.text(1, 10, sect108 +' Sold', horizontalalignment='center')
        plt.text(2, 10, sect106 +' Sold', horizontalalignment='center')
        plt.text(3, 10, sect205 +' Sold', horizontalalignment='center')
        plt.text(4, 10, sect203 +' Sold', horizontalalignment='center')
        plt.text(5, 10, sect201 +' Sold', horizontalalignment='center')
        
        
        plt.xticks(x_pos, x)
        plt.show()
        

        
               
    def eveningGUI(log):
        

        eveningFile = open("evening_pricing.txt", "r")
        
        evening_list = []

        dummy_list = eveningFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            evening_list.append(element.strip())

       
        eveningFile.close()

        log.login_window.destroy()
        
        log.pri_win = tk.Toplevel()
        log.pri_win.title ("Theater Ticket System")
        log.pri_win.minsize (width = 600, height = 600)


        log.pri_win.columnconfigure (0, minsize = 100)
        log.pri_win.columnconfigure (1, minsize = 100)
        log.pri_win.columnconfigure (2, minsize = 100)
        log.pri_win.columnconfigure (3, minsize = 100)
        log.pri_win.columnconfigure (4, minsize = 100)
        log.pri_win.columnconfigure (5, minsize = 100)
        log.pri_win.rowconfigure (0, minsize = 80)
        log.pri_win.rowconfigure (1, minsize = 50)
        log.pri_win.rowconfigure (2, minsize = 50)
        log.pri_win.rowconfigure (3, minsize = 80)
        log.pri_win.resizable (height = False, width = False)


        now = (datetime.today().strftime("%I:%M %p"))

        
        log.time_label = tk.Label (log.pri_win, text = ('Current time:', now), \
                                      font = ("MS Sans Serif",18), fg=("black"))
        log.time_label.grid(row = 0, column = 0, columnspan = 1)
        

        if(datetime.today().strftime("%H%M") <= "1400"):
            log.time_label = tk.Label (log.pri_win, text = ('The next show time is 2:00 PM'), \
                                       font = ("MS Sans Serif",18), fg=("black"))
            log.time_label.grid (row = 0, column = 2, columnspan = 3)
        if(datetime.today().strftime("%H%M") >= "1400" and datetime.today().strftime("%H%M") <= "2000"):
            log.time_label = tk.Label (log.pri_win, text = ('The next show time is 8:00 PM'), \
                                       font = ("MS Sans Serif",18), fg=("black"))
            log.time_label.grid (row = 0, column = 2, columnspan = 3)
        else:
            log.time_label = tk.Label (log.pri_win, text = ('The next show time is 2:00 PM'), \
                                       font = ("MS Sans Serif",18), fg=("black"))
            log.time_label.grid (row = 0, column = 2, columnspan = 3)

            
                
        photo = tk.PhotoImage (file = "H:\Python39\Lib\idlelib\Theather Ticket System\Seating.gif")
        log.LabelGUI = tk.Label (log.pri_win, image = photo)
        log.LabelGUI.image = photo
        log.LabelGUI.grid(row = 1, column = 0, rowspan = 2, padx = 20)

        log.seating_txt = tk.Label(log.pri_win, text = " Select Seating from above sections ", \
                     font = ("MS Sans Serif",12))
        log.seating_txt.grid (row = 3, column = 3, columnspan = 2)

        log.purchase_button = tk.Button(log.pri_win, text = ' Purchase ', width = 16, \
                                        font = ("MS Sans Serif",12), state = DISABLED)
        log.purchase_button.grid(row = 3,column = 2, padx = 20, pady = 20)

        


        keyRow = 1
        keyCol = 2
        index = 0
        seatIndex = 0
        seatUnavailable = 0

        seatingFile = open("seat_availability.txt", "r")
        
        seating_list = []

        dummy_list = seatingFile.readlines()
        
        element = '\n'

        for element in dummy_list:  
            seating_list.append(element.strip())

       
        seatingFile.close()

        options_list = ('101 - 105', '108 - 110', '106, 107 & 111, 112', '205, 206, 207', '203, 204, & 208, 209', '201, 202 & 210, 211')

        options = list(range(len(options_list)))

        seats = list(range(len(seating_list)))

        seatAvaible = []

        for keyNum in options_list:

            seatAvailable = seating_list[seatIndex]

            if '0' == seatAvailable:
                
                cmd = lambda button = keyNum: print(button)
                options[index] = tk.Button(log.pri_win, text = keyNum, font=("Helvetica", 10), \
                                              height = 2, width=12, padx = 20, pady = 20, state = DISABLED)
                options[index].grid(row = keyRow, column = keyCol,  sticky = 'nesw')
                index = index + 1
                seatIndex = seatIndex + 1
                keyCol = keyCol + 1
                seatUnavailable = seatUnavailable + 1
                
              
                if(keyCol > 4):
                    
                  
                    keyCol = 2
                    keyRow = keyRow + 1
                    
                
                    

                
            else:
              cmd = lambda button = keyNum: print(button)
              options[index] = tk.Button(log.pri_win, text = keyNum, font=("Helvetica", 10), \
                                              height = 2, width=12, padx = 20, pady = 20, command = partial(log.evenprice_match, keyNum))
              options[index].grid(row = keyRow, column = keyCol,  sticky = 'nesw')
              index = index + 1
              seatIndex = seatIndex + 1
              keyCol = keyCol + 1
              
              if(keyCol > 4):
                  
                  keyCol = 2
                  keyRow = keyRow + 1

                  
        seatFile = open("seat.txt", "w")

        seatAvailabilityChecker = ' '.join([str(item) for item in seatAvailable])

        seatFile.write(seatAvailabilityChecker)

        seatFile.close()

        

     

    def matineeGUI(log):

        matineeFile = open("matinee_pricing.txt", "r")
        
        matinee_list = []

        dummy_list = matineeFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            matinee_list.append(element.strip())

       
        matineeFile.close()

        log.login_window.destroy()
        

        log.pri_win = tk.Toplevel()
        log.pri_win.title ("Theater Ticket Systems")
        log.pri_win.minsize (width = 600, height = 600)


   
        log.pri_win.columnconfigure (0, minsize = 100)
        log.pri_win.columnconfigure (1, minsize = 100)
        log.pri_win.columnconfigure (2, minsize = 100)
        log.pri_win.columnconfigure (3, minsize = 100)
        log.pri_win.columnconfigure (4, minsize = 100)
        log.pri_win.columnconfigure (5, minsize = 100)
        log.pri_win.rowconfigure (0, minsize = 80)
        log.pri_win.rowconfigure (1, minsize = 50)
        log.pri_win.rowconfigure (2, minsize = 50)
        log.pri_win.rowconfigure (3, minsize = 80)
        log.pri_win.resizable (height = False, width = False)
                      

        now = (datetime.today().strftime("%I:%M %p"))

        
        log.time_label = tk.Label (log.pri_win, text = ('Current time:', now), \
                                      font = ("MS Sans Serif",18), fg=("black"))
        log.time_label.grid (row = 0, column = 0, columnspan = 1)
        

        if(datetime.today().strftime("%H%M") <= "1400"):
            log.time_label = tk.Label (log.pri_win, text = ('The next show time is 2:00 PM'), \
                                       font = ("MS Sans Serif",18), fg=("black"))
            log.time_label.grid (row = 0, column = 2, columnspan = 3)
        if(datetime.today().strftime("%H%M") >= "1400" and datetime.today().strftime("%H%M") <= "2000"):
            log.time_label = tk.Label (log.pri_win, text = ('The next show time is 8:00 PM'), \
                                       font = ("MS Sans Serif",18), fg=("black"))
            log.time_label.grid (row = 0, column = 2, columnspan = 3)
        else:
            log.time_label = tk.Label (log.pri_win, text = ('The next show time is 2:00 PM'), \
                                       font = ("MS Sans Serif",18), fg=("black"))
            log.time_label.grid (row = 0, column = 2, columnspan = 3)
            
        
                  
        photo = tk.PhotoImage (file = "H:\Python39\Lib\idlelib\Theather Ticket System\Seating.gif")
        log.LabelGUI = tk.Label (log.pri_win, image = photo)
        log.LabelGUI.image = photo
        log.LabelGUI.grid(row = 1, column = 0, rowspan = 2, padx = 20)

        log.seating_txt = tk.Label(log.pri_win, text = " Select Seating from above sections ", \
                     font = ("MS Sans Serif",12))
        log.seating_txt.grid (row = 3, column = 3, columnspan = 2)

        log.purchase_button = tk.Button(log.pri_win, text = ' Purchase ', width = 16, \
                                        
                                            
                                        font = ("MS Sans Serif",12), state = DISABLED)
        log.purchase_button.grid(row = 3,column = 2, padx = 20, pady = 20)


        keyRow = 1
        keyCol = 2
        index = 0
        seatIndex = 0
        seatUnavailable = 0

        seatingFile = open("seat_availability.txt", "r")
        
        seating_list = []

        dummy_list = seatingFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            
                
            seating_list.append(element.strip())

       
        seatingFile.close()

        options_list = ('101 - 105', '108 - 110', '106, 107 & 111, 112', '205, 206, 207', '203, 204, & 208, 209', '201, 202 & 210, 211')

        options = list(range(len(options_list)))

        seats = list(range(len(seating_list)))

        seatAvaible = []

        for keyNum in options_list:

            seatAvailable = seating_list[seatIndex]

            if '0' == seatAvailable:
                
                cmd = lambda button = keyNum: print(button)
                options[index] = tk.Button(log.pri_win, text = keyNum, font=("Helvetica", 10), \
                                              height = 2, width=12, padx = 20, pady = 20, state = DISABLED)
                options[index].grid(row = keyRow, column = keyCol,  sticky = 'nesw')
                index = index + 1
                seatIndex = seatIndex + 1
                keyCol = keyCol + 1
                seatUnavailable = seatUnavailable + 1
                
              
                if(keyCol > 4):
                    
                  
                    keyCol = 2
                    keyRow = keyRow + 1
                    
                
                    

                
            else:
              cmd = lambda button = keyNum: print(button)
              options[index] = tk.Button(log.pri_win, text = keyNum, font=("Helvetica", 10), \
                                              height = 2, width=12, padx = 20, pady = 20, command = partial(log.matprice_match, keyNum))
              options[index].grid(row = keyRow, column = keyCol,  sticky = 'nesw')
              index = index + 1
              seatIndex = seatIndex + 1
              keyCol = keyCol + 1
              
              if(keyCol > 4):
                  
                  keyCol = 2
                  keyRow = keyRow + 1

        seatFile = open("seat.txt", "w")

        seatAvailabilityChecker = ' '.join([str(item) for item in seatAvailable])

        seatFile.write(seatAvailabilityChecker)

        seatFile.close()

        


    def evenprice_chosen(log):

        managerFile = open("manager_choice.txt", "w")

        managerFile.write('1')

        managerFile.close()

        log.eveningGUI()

    def matprice_chosen(log):

        managerFile = open("manager_choice.txt", "w")

        managerFile.write('0')

        managerFile.close()

        log.matineeGUI()

    def evenprice_match(log, choice):

        option_list = ('101 - 105', '108 - 110', '106, 107 & 111, 112', '205, 206, 207', '203, 204, & 208, 209', '201, 202 & 210, 211')

        eveningFile = open("evening_pricing.txt", "r")
        
        evening_list = []

        dummy_list = eveningFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            evening_list.append(element.strip())

       
        eveningFile.close()

        option_index = option_list.index(choice)

        

        for x, res in enumerate(evening_list):
            if(option_index == x):
                price = res
                
        log.price_label = tk.Label (log.pri_win,text = ('Price of seating: ', price), \
                                    font = ("MS Sans Serif",18), fg=("black"))
        log.price_label.grid (row = 3, column = 0, columnspan = 1)

        priceFile = open("price.txt", "w")

        priceFile.writelines(price)

        priceFile.close()

        choiceFile = open("choice.txt", "w")

        choiceFile.writelines(choice)

        choiceFile.close()
       
        seatFile = open("seat.txt", "r")

        seat_list = []

        dummy_list = seatFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            seat_list.append(element.strip())

       
        seatFile.close()
        
        

        if(seat_list == 6):
                      
           
            
            log.purchase_button = tk.Button(log.pri_win, text = ' Purchase ', width = 16, \
                                            
                                            font = ("MS Sans Serif",12), state = DISABLED)
            log.purchase_button.grid(row = 3,column = 2, padx = 20, pady = 20)
            
        else:
            
            log.purchase_button = tk.Button(log.pri_win, text = ' Purchase ', width = 16, \
                                            font = ("MS Sans Serif",12), command = log.purchase_complete)
            log.purchase_button.grid(row = 3,column = 2, padx = 20, pady = 20)
      
   


        
    def matprice_match(log, choice):

        option_list = ('101 - 105', '108 - 110', '106, 107 & 111, 112', '205, 206, 207', '203, 204, & 208, 209', '201, 202 & 210, 211')

        matineeFile = open("matinee_pricing.txt", "r")
        
        matinee_list = []

        dummy_list = matineeFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            matinee_list.append(element.strip())

       
        matineeFile.close()
        

        option_index = option_list.index(choice)

        for x, res in enumerate(matinee_list):
            if(option_index == x):
                price = res

        log.price_label = tk.Label (log.pri_win,text = ('Price of seating: ', price), \
                                    font = ("MS Sans Serif",18), fg=("black"))
        log.price_label.grid (row = 3, column = 0, columnspan = 1)

        priceFile = open("price.txt", "w")

        priceFile.writelines(price)

        priceFile.close()

        choiceFile = open("choice.txt", "w")

        choiceFile.writelines(choice)

        choiceFile.close()
       
        
                
        seatFile = open("seat.txt", "r")

        seat_list = []

        dummy_list = seatFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            seat_list.append(element.strip())

       
        seatFile.close()
        
        

        if(seat_list == 6):
            
           
            log.purchase_button = tk.Button(log.pri_win, text = ' Purchase ', width = 16, \
                                            
                                            font = ("MS Sans Serif",12), state = DISABLED)
            log.purchase_button.grid(row = 3,column = 2, padx = 20, pady = 20)
            
        else:
            
            log.purchase_button = tk.Button(log.pri_win, text = ' Purchase ', width = 16, \
                                            font = ("MS Sans Serif",12), command = log.purchase_complete)
            log.purchase_button.grid(row = 3,column = 2, padx = 20, pady = 20)
      
   
           
    def purchase_complete (log):

        priceFile = open("price.txt", "r")
        
        price = []

        dummy_list = priceFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            price.append(element.strip())

       
        priceFile.close()

        

        price = str(price)

        choiceFile = open("choice.txt", "r")
        
        choice = []

        dummy_list = choiceFile.readlines()
        
        element = '\n'

        for element in dummy_list:
            choice.append(element.strip())

       
        choiceFile.close()

        

        option_list = ['101 - 105', '108 - 110', '106, 107 & 111, 112', '205, 206, 207', '203, 204, & 208, 209', '201, 202 & 210, 211']

        
        index = 0

        while index < 6:
            if choice[0] == option_list[index]:

                seatingFile = open("seat_availability.txt", "r")
       
        
                seating_list = []

                dummy_list = seatingFile.readlines()
        
                element = '\n'

                for element in dummy_list:
                    seating_list.append(element.strip())
            
                seatingFile.close()
        

                integer_map = map(int, seating_list)

                seats = list(integer_map)

                newSeats = seats[index] - 1

                seats[index] = newSeats

                seatFile = open("seat_availability.txt", "w")

                seatAvailabilityChecker = ' \n'.join([str(item) for item in seats])

                seatFile.write(seatAvailabilityChecker)

               
                seatFile.close()

                choice = str(choice)

        
                tk.messagebox.showinfo( "Purchase Complete", "Ticket purchase stub \n \nSitting in section:  " + choice + "\nPrice:  " + price + \
                                        "\n\nSeating is general admission  for all sections. \nTo reserve seating or for special engagments," \
                                        "\nvist the theather manager.")

        
                                      
                log.pri_win.destroy()

            
            else:
                index = index + 1
            

        
        
            

        
    
           
        

       
                    
      
                
        
              
        
        
        
           
            
      
       


