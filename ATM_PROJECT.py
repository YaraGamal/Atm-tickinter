'''
/*******************************************************************************
/*  AUTHORS:        YARA GAMAL SAAD                                              *
                                                   *
/*  DESCRIPTION:    ATM Application                                            *
/*******************************************************************************
'''

import tkinter as tk
from tkinter.messagebox import showinfo
import tkinter.font as font

##withdraw()###
#Removes the window from the screen, without destroying it##
##deiconify()##
# WE Call it to restore the window.#

                            
i = 0
users={2222:{"Balance":"3500166","Password":'1783','Name':"Ahmed Abdelrazek Mohamed"},
203659302214:{"Balance":"520001","Password":'1390','Name':'Salama Mohamed Foaad'},
126355700193:{"Balance":"111000","Password":'1214','Name':'Abdel Khaled Abdelrahman'}}
def main_window():        
    global main_win
    global entry1
    main_win= tk.Tk()
    main_win.title("login")
    main_win.geometry('300x300')
    main_win.config(bg = '#68B0AB')
    myFont = font.Font(size=20) 
    user_label1 = tk.Label(main_win,text="ATM SYSTEM ",bg ='#26547D')
    user_label2 = tk.Label(main_win,text="account number: ")
    entry1 = tk.Entry(main_win)
    button = tk.Button(main_win,text="ENTER", command=check_user)
    user_label1['font'] = myFont
    user_label1.place(x=60,y=14)
    user_label2.place(x=20,y=80)
    entry1.place(x=50,y=130)
    button.place(x=120,y=200)
                                ##########################
def check_user():
    global ID
    ID= int(entry1.get())
    if ID in users:
        global pass_user
        global entry2
        global  pass_win
        pass_win= tk.Toplevel()
        pass_win.title("User password")
        pass_win.geometry("300x300")
        pass_win.config(bg = '#68B0AB')
        user_label3 = tk.Label(pass_win,text="ATM SYSTEM ",bg ='#26547D')
        myFont = font.Font(size=20) 
        user_label3['font'] = myFont
        user_label3.place(x=60,y=14)
        pass_label = tk.Label(pass_win, text="Password: ").place(x=20, y=80)
        entry2 = tk.Entry(pass_win, show="*")
        entry2.place(x=50, y=130)  
        pass_button = tk.Button(pass_win, text="Login", command=check_password).place(x=120, y=200) 
        main_win.withdraw()
    else:
        showinfo("sorry", "User not found")


                            ##########################
def check_password():
    global i
    i += 1
    if i <= 3:
        if users[ID]["Password"] == entry2.get():
            global menu
            i = 0
            pass_win.withdraw()
            menu = tk.Toplevel()
            menu.title("ATM_PASSWORD")
            menu.geometry("400x400")
            menu.config(bg = '#68B0AB')  
            user_label3 = tk.Label(menu,text="ATM SYSTEM ",bg ='#26547D')
            myFont = font.Font(size=26) 
            user_label3['font'] = myFont
            user_label3.place(x=60,y=14)            
            name = tk.Label(menu, text= users[ID]['Name']).place(x=100, y=100)
            balance = tk.Button(menu, text="Balance", command=Balance_Inquiry,bg='#77BFC7').place(x=145, y=140)
            withdraw = tk.Button(menu, text="Cash Withdraw", command=Cash_Withdraw,bg='#66CDAA').place(x=130, y=170)
            change = tk.Button(menu, text="Change Password", command=Password_Change,bg='#20B2AA').place(x=125, y=200)
            fawry = tk.Button(menu, text="Fawry Service", command=Fawry_Service,bg='#00A36C').place(x=130, y=230)
            exit = tk.Button(menu, text="Exit", command=main_win.destroy,bg='#307D7E').place(x=160, y=280)
        else:
            showinfo("warn", "Wrong Password")
    else:
	    showinfo("sorry", "This account is locked, please go to the branch")

                        ###################################
def Balance_Inquiry():
    bal =users[ID]["Balance"]
    v1="Your balance is  "
    v2=" .LE"
    v=v1+bal+v2
    tk.messagebox.showinfo("Balance",v)
                        ####################################  
def Password_Change():
    menu.withdraw()
    global change_win
    global new_pass
    global confrim
    change_win = tk.Toplevel()
    change_win.title("Change password ")
    change_win.geometry("400x400")
    change_win.config(bg = '#68B0AB')  
    user_label3 = tk.Label(change_win,text="ATM SYSTEM ",bg ='#26547D')
    myFont = font.Font(size=26) 
    user_label3['font'] = myFont
    user_label3.place(x=60,y=14)
    change_label = tk.Label(change_win, text="Enter your new password: ").place(x=10, y=120)
    new_pass = tk.Entry(change_win)
    new_pass.place(x=10, y= 150)
    confrim_label = tk.Label(change_win, text="Confirm your new password: ").place(x=10, y=180)
    confrim = tk.Entry(change_win)
    confrim.place(x=10, y=210)
    change_button = tk.Button(change_win, text="Change", command=change_password_check,bg='#66CDAA').place(x=120, y=300)

def change_password_check():
    new_password = new_pass.get()
    confrim_password = confrim.get()
    if new_password == confrim_password:
        users[ID]["Password"] = new_password
        showinfo("Success", "Password has been changed successfully")
        change_win.destroy()
        pass_win.deiconify()
    else:
        tk.messagebox.showerror("Error", "Password doesn't match")


                                ################################
def Cash_Withdraw():
    menu.withdraw()
    global withdraw_win
    global cash
    withdraw_win = tk.Toplevel()
    withdraw_win.title("ATM-Withdraw")
    withdraw_win.geometry("300x300")
    withdraw_win.config(bg = '#68B0AB')  
    user_label3 = tk.Label(withdraw_win,text="ATM SYSTEM ",bg ='#26547D')
    myFont = font.Font(size=20) 
    user_label3['font'] = myFont
    user_label3.place(x=60,y=14)
    withdraw_label = tk.Label(withdraw_win, text="Enter the amount,please : ").place(x=20, y=80)
    cash = tk.Entry(withdraw_win)
    cash.place(x=50, y=130)
    withdraw_button = tk.Button(withdraw_win, text="Withdraw", command=withdraw_check,bg='#3B9C9C').place(x=120, y=200)

def withdraw_check():
    amount =int(cash.get()) 
    if amount % 100 == 0:
        if amount <= 5000:
            if amount <= int(users[ID]["Balance"]):
                bal =int(users[ID]["Balance"])
                bal = str(bal- amount)
                v1="operation accomplished successfully,Now Your balance is  "
                v2=" .LE"
                v=v1+bal+v2
                tk.messagebox.showinfo("Balance",v)
                users[ID]["Balance"]=bal
                withdraw_win.destroy()
                menu.deiconify()
            else:
                tk.messagebox.showerror("Error", "Balance is not enough")
                withdraw_win.destroy()
                menu.deiconify()
        else:
            tk.messagebox.showerror("Error", "withdraw more than 5000LE")
            withdraw_win.destroy()
            menu.deiconify()
    else:
        tk.messagebox.showerror("Error", "You can only withdraw hundreds")
        withdraw_win.destroy()
        menu.deiconify()
                                ###############################        
def Fawry_Service():
    global fawry_win
    global r_check
    menu.withdraw()
    #####Tkinter IntVar() Function#####
    #tkinter contains built-in programming types which work like a normal 
    # python type with additional features used to manipulate values of widgets
    #  like Label and Entry more effectively, 
    # which makes them different from python data types
    r_check=tk.IntVar()
    fawry_win = tk.Toplevel()
    fawry_win.title("ATM-fawry")
    fawry_win.geometry("400x400") 
    fawry_win.config(bg = '#68B0AB')  
    user_label3 = tk.Label(fawry_win,text="ATM Fawry",bg ='#26547D')
    myFont = font.Font(size=33) 
    user_label3['font'] = myFont
    user_label3.place(x=65,y=14)
    label1 = tk.Label(fawry_win, text="Choose your mobile line: ").place(x=10, y=100)
    Orange_button = tk.Radiobutton(fawry_win, text="Orange", variable=r_check, value=1).place(x=145, y=150)
    Etisalat_button = tk.Radiobutton(fawry_win, text="Etisalat", variable=r_check, value=2).place(x=145, y=180)
    Vodafone_button = tk.Radiobutton(fawry_win, text="Vodafone", variable=r_check, value=3).place(x=145, y=210)
    We_button = tk.Radiobutton(fawry_win, text="We", variable=r_check, value=4).place(x=145, y=240)
    Recharge_button = tk.Button(fawry_win, text="Recharge option", command=charge_check,bg='#3B9C9C').place(x=120, y=310)
#################################
#checking the company selected
def charge_check():
    global charge_win
    global phoneno
    global amount_charge
    arg = r_check.get()
    fawry_win.withdraw()
    charge_win= tk.Toplevel()
    charge_win.title("ATM- charge fawry")
    charge_win.geometry("300x300")
    charge_win.config(bg = '#68B0AB')
    user_label3 = tk.Label(charge_win,text="ATM Fawry ",bg ='#26547D')
    myFont = font.Font(size=20) 
    user_label3['font'] = myFont
    user_label3.place(x=60,y=14)
    if arg == 1:
        label1 = tk.Label(charge_win, text="Enter your phone number: must begin with 012 ").place(x=10, y=100)
    elif arg == 2:
        label1 = tk.Label(charge_win, text="Enter your phone number: must begin with 011 ").place(x=10, y=100)  
    elif arg == 3:
        label1 = tk.Label(charge_win, text="Enter your phone number: must begin with 010 ").place(x=10, y=100)
    elif arg == 4:
        label1 = tk.Label(charge_win, text="Enter your phone number: must begin with 015 ").place(x=10, y=100)
    phoneno = tk.Entry(charge_win)
    phoneno.place(x=10, y=130)
    amount_label = tk.Label(charge_win, text="Enter the amount you want to recharge: ").place(x=10, y=160)
    amount_charge = tk.Entry(charge_win)
    amount_charge.place(x=10, y=190)
    charge_button = tk.Button(charge_win, text="Recharge", command=number_check).place(x=100, y=250)
##########################
# checking if the phone number and the balance is avilable 
def number_check():
    global phone_no
    global phoneno
    global amount_charge
    phone_no =phoneno.get()
    amount = amount_charge.get()
    if len(phone_no) == 12:
        amount = int(amount)
        if amount <= int(users[ID]["Balance"]):
            bal =int(users[ID]["Balance"])
            bal = str(bal- amount)
            v1="operation accomplished successfully,Now Your balance is  "
            v2=" .LE"
            v=v1+bal+v2
            tk.messagebox.showinfo("Balance",v)
            users[ID]["Balance"]=bal
            charge_win.destroy()
            menu.deiconify()
        else:
            tk.messagebox.showerror("Error", "Balance is not enough")
            charge_win.destroy()
            menu.deiconify()
    else:
        tk.messagebox.showerror("Error", "invalid number")
        charge_win.destroy()
        menu.deiconify()
                                    #################################
main_window()        
main_win.mainloop()        
