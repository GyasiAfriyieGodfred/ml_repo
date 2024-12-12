import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
from datetime import datetime
import random, os,tempfile, smtplib #import temporary file,smtplib for sending mails

# functionalities

def clear():
    #this is part will make the entries set to 0
    Bath_soap_entry.delete(0,END)
    facecreame_entry.delete(0,END)
    facewash_entry.delete(0,END)
    Hairspray_entry.delete(0,END)
    hairgel_entry.delete(0,END)
    rice_entry.delete(0,END)
    oil_entry.delete(0,END)
    wheat_entry.delete(0,END)
    sugar_entry.delete(0,END)
    tea_entry.delete(0,END)
    mazaa_entry.delete(0,END)
    pepsi_entry.delete(0,END)
    sprite_entry.delete(0,END)
    dew_entry.delete(0,END)
    Coca_Cola_entry.delete(0,END)

    #this inserts zeros after deleting the entry
    Bath_soap_entry.insert(0,0)
    facecreame_entry.insert(0,0)
    facewash_entry.insert(0,0)
    Hairspray_entry.insert(0,0)
    hairgel_entry.insert(0,0)
    rice_entry.insert(0,0)
    oil_entry.insert(0,0)
    wheat_entry.insert(0,0)
    sugar_entry.insert(0,0)
    tea_entry.insert(0,0)
    mazaa_entry.insert(0,0)
    pepsi_entry.insert(0,0)
    sprite_entry.insert(0,0)
    dew_entry.insert(0,0)
    Coca_Cola_entry.insert(0,0)

    #this clears all the entries in the entries below
    cosmetic_entry.delete(0,END)
    grocery_entry.delete(0,END)
    cold_drink_entry.delete(0,END)

    cosmetic_tax_entry.delete(0,END)
    Grocery_tax_entry.delete(0,END)
    cold_drink_tax_entry.delete(0,END)

    name_entry.delete(0,END)
    phone_entry.delete(0,END)
    bill_number_entry.delete(0,END)

    textarea.delete(1.0,END)

def send_gmail(): # configuring the email send button
    try:
        object = smtplib.SMTP('smtp.gmail.com',587) # create an obj to send mail and a secured number
        object.starttls()
        object.login(sender_email_entry.get(),sender_password_entry.get())
        # provide your email and password to login, this get the info fron the sender_email_entry and the password entry
        message = email_text_area.get(1.0,END) # this gets the message
        object.sendmail(sender_email_entry.get(),reciver_email_entry.get(),message) # it takes the sender email, receiver email and the message u sending
        object.quit() # after message is sent
        messagebox.showinfo("sending mail", 'Email sent successfully',parent=root1)
        # pop up to notify your email is sent, the parent will make the message to be shown on the Toplevel instead of the main billing system
        # for the password we need to generate an application specific password follow video from 50 minutes
        root1.destroy() #this destroys the window or it closes the email window
    except:
        messagebox.showerror("Error",'Something went wrong try again',parent= root1)


def send_email():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror("Error", "Bill is empty") #this creates error if no bill is generated
    else:
        #create another GUI for the email
        root1= Toplevel()
        root1.grab_set() #this makes the current window active and the previous window inactive
        root1.title('Send email')
        root1.resizable(0,0)  # to minimize and maximize the window
        label1 = LabelFrame(root1,text='SENDER INFO',font=('Times New Roman',14,'bold'),relief=GROOVE)
        label1.grid(row=0,column=0)
        sender_email = Label(label1,text="Sender's Email",font=('Times New Roman',14,'bold'),relief=GROOVE,bd=6)
        sender_email.grid(row=0,column=0,padx=10,pady=5)
        sender_email_entry=Entry(label1,font=('Times New Roman',14,'bold'),relief=GROOVE)
        sender_email_entry.grid(row=0,column=1,padx=10,pady=5)
        sender_password = Label(label1,text="sender's password",font=('Times New Roman',14,'bold'),relief=GROOVE)
        sender_password.grid(row=1,column=0)
        sender_password_entry = Entry(label1,font=('Times New Roman',14,'bold'),relief=GROOVE,show='*')
        #show makes the password invisible by printing *
        sender_password_entry.grid(row=1,column=1)


        label2 = LabelFrame(root1, text='RECEIVER INFO', font=('Times New Roman', 14, 'bold'), relief=GROOVE)
        label2.grid(row=1, column=0)
        reciver_email = Label(label2,text="Receiver's Email",font=('Times New Roman',14,'bold'),relief=GROOVE)
        reciver_email.grid(row=0,column=0,padx=10,pady=5)
        reciver_email_entry = Entry(label2,font=('Times New Roman',14,'bold'),relief=GROOVE)
        reciver_email_entry.grid(row=0,column=1,padx=10,pady=5)
        message = Label(label2,text='Message',font=('Times New Roman',14,'bold'))
        message.grid(row=1,column=0)
        email_text_area = Text(label2,width=42,height=11,font=('Times New Roman',10,'bold'),relief=SUNKEN,bd=2)
        email_text_area.grid(row=2,column=0,columnspan=2)
        email_text_area.delete(1.0,END) # deletes the old entries
        email_text_area.insert(END,textarea.get(1.0,END).replace("="," ").replace("-","").replace("\t\t\t","\t\t"))
        # this inserts the info in the bill area,
        # .replace("="," ").replace("-","").replace("\t\t\t","\t\t") are used to replace the lines and tabs that disorganises the email insertion

        send_button = Button(root1,text='SEND',font=('Times New Roman',14,'bold'),width=12,command=send_gmail)
        send_button.grid(row=2,column=0,padx=10,pady=5)

        root1.mainloop()

def search_bills():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_number_entry.get():
            # i.split('.')[0] separates the number from the txt
            f = open(f"bills/{i}", 'r', encoding='utf-8')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close
            break
    else:
        messagebox.showerror("Error", "Invalid Bill Number")


if not os.path.exists('bills'):
    os.mkdir('bills')




def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save your bill?')
#     .askyesno is used to find out if the bill should be saved or not
    if result:
        bill_content = textarea.get(1.0,END) #copying all the entry in the bill area
        file=open(f'bills/{billnumber}.txt','w',encoding='utf-8') # saving the bill in the bills/bill_number folder as a test
        file.write(bill_content)
        file.close()
        messagebox.showinfo("message",f'Bill number:{billnumber}, saved successfully ')
        billnumber=random.randint(100,1000000)

def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror("Error", "Bill is empty")
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w',encoding='utf-8').write(textarea.get(1.0, END))
        os.startfile(file, 'print') # this part will print test



billnumber = random.randint(100,1000000)

def bill_area():
    if name_entry.get() == '' or phone_entry.get() == ''  or cashier_entry.get()=='':
        messagebox.showerror('Error', 'Enter Customer and  Cashier details')
    elif cosmetic_entry.get() == 'Gh₵ 0' and grocery_entry.get() == 'Gh₵ 0' and cold_drink_entry.get() == "Gh₵ 0":
        messagebox.showerror('Error', 'No Products selected')
    elif cosmetic_entry.get() == 'Gh₵ 0 ' and grocery_entry.get() == 'Gh₵ 0' and cold_drink_entry.get() == "Gh₵0":
        messagebox.showerror('Error', 'No Products selected')
    else:
        textarea.delete(1.0, END) #to delete previous entry,1.0 is start position, if not specified, previous bills will be shown in the textarea
        textarea.insert(END, 'ORIGINAL Sales Receipt \n')
        textarea.insert(END, '\t\t** TUBI COMPANY LIMITED **\n')
        textarea.insert(END, '\t\t\t P.O.BOX 2234 \n')
        textarea.insert(END, '\t\t--LOCATION: BANTAMA, KUMASI--')
        textarea.insert(END, f'\nDate:{date_entry.get()}')
        textarea.insert(END, f'\nBill Number:{billnumber}')
        textarea.insert(END, f'\nCustomer Name:{name_entry.get()}')
        textarea.insert(END, f'\nPhone Number:{phone_entry.get()}')
        textarea.insert(END, f'\nCashier_name: {cashier_entry.get()}')
        textarea.insert(END, f'\nCashier_Id: {cashier_id_entry.get()}')
        textarea.insert(END, '\n=================================================\n')
        textarea.insert(END, 'Product\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=================================================')
        if Bath_soap_entry.get() != '0':
            textarea.insert(END, f'\nBath Soap\t\t\t{Bath_soap_entry.get()}\t\t Gh₵{soapprice} ')

        if facecreame_entry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{facecreame_entry.get()}\t\tGh₵{facecream}')

        if facewash_entry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t\t{facewash_entry.get()}\t\tGh₵{facewash} ')

        if Hairspray_entry.get() != '0':
            textarea.insert(END, f'\nHairspray\t\t\t{Hairspray_entry.get()}\t\tGh₵{Hairspray} ')

        if hairgel_entry.get() != '0':
            textarea.insert(END, f'\nHairgel\t\t\t{hairgel_entry.get()}\t\tGh₵{hairgel} ')

        if rice_entry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{rice_entry.get()}\t\tGh₵{rice} ')

        if oil_entry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oil_entry.get()}\t\tGh₵{oil} ')

        if wheat_entry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheat_entry.get()}\t\tGh₵{wheat} ')

        if sugar_entry.get() != '0':
            textarea.insert(END, f'\nSugar\t\t\t{sugar_entry.get()}\t\tGh₵{sugar}')

        if tea_entry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{tea_entry.get()}\t\tGh₵{tea} ')

        if mazaa_entry.get() != '0':
            textarea.insert(END, f'\nMazaa\t\t\t{mazaa_entry.get()}\t\tGh₵{mazaa} ')

        if pepsi_entry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsi_entry.get()}\t\tGh₵{pepsi} ')

        if sprite_entry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{sprite_entry.get()}\t\tGh₵{sprite} ')

        if dew_entry.get() != '0':
            textarea.insert(END, f'\nDew\t\t\t{dew_entry.get()}\t\t Gh₵{dew}')

        if Coca_Cola_entry.get() != '0':
            textarea.insert(END, f'\nCoca Cola\t\t\t{Coca_Cola_entry.get()}\t\t{cocacola} Gh₵')
        textarea.insert(END, '\n-------------------------------------------------')

        if cosmetic_tax_entry.get() != '0.0 Gh cedis':
            textarea.insert(END, f'\nCosmetic Tax\t\t\t\t\t{cosmetic_tax_entry.get()}')

        if Grocery_tax_entry.get() != '0.0 Gh₵':
            textarea.insert(END, f'\nGrocery Tax\t\t\t\t\t{Grocery_tax_entry.get()}')

        if cold_drink_tax_entry.get() != '0.0 Gh₵':
            textarea.insert(END, f'\nCold Drink Tax\t\t\t\t\t{cold_drink_tax_entry.get()}')
        textarea.insert(END, '\n-------------------------------------------------')
        textarea.insert(END, f'\n\nTotal Bill\t\t\t\tGh₵ {total} ')
        textarea.insert(END, '\n-------------------------------------------------')
        textarea.insert(END, '\n Goods sold are returnable within seven days with ')
        textarea.insert(END, 'valid receipt only.\n')
        textarea.insert(END, '\n\t*** Software By Dolphwale Technologies***')
        textarea.insert(END, '\n\t Email: dolphwaletechnologies@gmail.com')
        textarea.insert(END, '\n\t\t --Tel:0245813293--')

        save_bill()

def get_datetime():

    new_date= datetime.now()
    formatted_date =new_date.strftime("%Y/%m/%d %H:%M:%S %p")
    date_entry.delete(0,END)
    date_entry.insert(0,formatted_date)


def total():
    global soapprice,facecream,facewash,Hairspray,hairgel,rice,oil,wheat,sugar,tea,mazaa,pepsi,sprite,dew,cocacola
    global total
    soapprice= int(Bath_soap_entry.get())*20  #Bath_soap_entry.get() returns a string then convert to numeric
    facecream = int(facecreame_entry.get())*10
    facewash= int(facewash_entry.get()) *20
    Hairspray=int(Hairspray_entry.get())*15
    hairgel=int(hairgel_entry.get())*10
    totalcosmeticprice= soapprice + facecream +facewash +Hairspray+hairgel
    cosmetic_entry.delete(0,END) #deletes the old input when new inputs are added
    cosmetic_entry.insert(0,f'Gh₵ {totalcosmeticprice}') #inserts 0 if no value entered in the cosmetic entry
    cometicstax= int(totalcosmeticprice)*0.12
    cosmetic_tax_entry.delete(0,END)
    cosmetic_tax_entry.insert(0,f'Gh₵ {cometicstax}')


    rice= int(rice_entry.get())*80
    oil= int(oil_entry.get())*45
    wheat= int(wheat_entry.get())*24
    sugar= int(sugar_entry.get())*8
    tea= int(tea_entry.get())*2
    totalgrocery = rice+oil+wheat+sugar+tea
    grocery_entry.delete(0,END)
    grocery_entry.insert(0, f'Gh₵ {totalgrocery}')
    grocerytax = int(totalgrocery )* 0.05
    Grocery_tax_entry.delete(0,END)
    Grocery_tax_entry.insert(0,f'Gh₵ {grocerytax} ')


    mazaa= int(mazaa_entry.get())*2.5
    pepsi= int(pepsi_entry.get())*2.5
    sprite= int(sprite_entry.get())*2.5
    dew = int(dew_entry.get())* 5
    cocacola= int(Coca_Cola_entry.get())* 3
    totalcolddrinkprice=mazaa+pepsi+sprite+dew+cocacola
    cold_drink_entry.delete(0, END)
    cold_drink_entry.insert(0,f'Gh₵ {totalcolddrinkprice}')
    colddrinkstax = int(totalcolddrinkprice) * 0.08
    cold_drink_tax_entry.delete(0, END)
    cold_drink_tax_entry.insert(0,f'Gh₵ {colddrinkstax}')

    total = totalcosmeticprice +totalgrocery+ totalcolddrinkprice+cometicstax+grocerytax+colddrinkstax

def balance_amount():
    global total_price,amount_paid_num
    global change
    amount = amount_paid.get()
    amount_paid_num = int(amount)
    total_price = total
    change ='{:,.2f}'.format( amount_paid_num - total_price)
    balance_entry.delete(0,END)
    balance_entry.insert(0,f'Gh₵ {change}')

# creating the GUI
root = Tk()
root.title("Billing Project")
root.minsize(800,700)
# root.iconbitmap(" ")
title = Label(root,text= "Customer Billing System",font=("Times New Roman",30,"bold"),bg="gold3",fg="white",relief=RAISED,bd=8)
title.pack(fill=X)
customer_info = LabelFrame(root,text="Customer Details",font=("Times New Roman",15,"bold"),fg="gold3")
customer_info.pack()

name_label= Label(customer_info,text="Customer Name",font=("Times New Roman",12,"bold"))
name_label.grid(row=0,column=0,padx=10,pady=10)

name_entry = Entry(customer_info,font=("Times New Roman",12))
name_entry.grid(row=0,column=1)

phone = Label(customer_info,text="Phone Number",font=("Times New Roman",12,"bold"))
phone.grid(row=0,column=2,padx=10,pady=10)
phone_entry = Entry(customer_info,font=("Times New Roman",12),relief=GROOVE)
phone_entry.grid(row=0,column=3)

bill_number = Label(customer_info,text="Bill Number",font=("Times New Roman",12,"bold"))
bill_number.grid(row=0,column=6,padx=10,pady=10)

bill_number_entry =Entry(customer_info,font=("Times New Roman",12),relief=GROOVE)
bill_number_entry.grid(row=0,column=7)

date_label = Button(customer_info,text="Date",font=("Times New Roman",12),command=get_datetime)
date_label.grid(row=0, column=4,padx=10,pady=10)

date_entry =Entry(customer_info,font=("Times New Roman",12),relief=GROOVE)
date_entry.grid(row=0,column=5)

search_button = Button(customer_info,text="SEARCH",font=("Times New Roman",12,"bold"),command=search_bills)
search_button.grid(row=0,column=8,padx=10,pady=10)

# frame to host the cosmetics,grocery and cold drinks label frame
frame2 = Frame(root)
frame2.pack()

cosmetics_frame = LabelFrame(frame2,text="Cosmetics",font=("Times New Roman",12,"bold"),fg="gold3")
cosmetics_frame.grid(row=0,column=0)

Bath_soap_label = Label(cosmetics_frame,text="Bath Soap",font=("Times New Roman",12,"bold"))
Bath_soap_label.grid(row=0,column=0,padx=10,pady=10)
Bath_soap_entry=Entry(cosmetics_frame,font=("Times New Roman",12,"bold"))
Bath_soap_entry.grid(row=0,column=1,padx=10,pady=10)
Bath_soap_entry.insert(0,0)

facecreame_label = Label(cosmetics_frame,text="Face Cream",font=("Times New Roman",12,"bold"))
facecreame_label.grid(row=1,column=0,padx=10,pady=10)
facecreame_entry=Entry(cosmetics_frame,font=("Times New Roman",12))
facecreame_entry.grid(row=1,column=1,padx=10,pady=10)
facecreame_entry.insert(0,0)

facewash_label = Label(cosmetics_frame,text="Face wash",font=("Times New Roman",12,"bold"))
facewash_label.grid(row=2,column=0,padx=10,pady=10)
facewash_entry=Entry(cosmetics_frame,font=("Times New Roman",12))
facewash_entry.grid(row=2,column=1,padx=10,pady=10)
facewash_entry.insert(0,0)

Hairspray_label = Label(cosmetics_frame,text="Hair Spray",font=("Times New Roman",12,"bold"))
Hairspray_label.grid(row=3,column=0,padx=10,pady=10)
Hairspray_entry=Entry(cosmetics_frame,font=("Times New Roman",12))
Hairspray_entry.grid(row=3,column=1,padx=10,pady=10)
Hairspray_entry.insert(0,0)


hairgel_label = Label(cosmetics_frame,text="Hair Gel",font=("Times New Roman",12,"bold"))
hairgel_label.grid(row=4,column=0,padx=10,pady=10)
hairgel_entry=Entry(cosmetics_frame,font=("Times New Roman",12))
hairgel_entry.grid(row=4,column=1,padx=10,pady=10)
hairgel_entry.insert(0,0)

# grocery frame
grocery_frame = LabelFrame(frame2,text="Grocery",font=("Times New Roman",12,"bold"),fg="gold3")
grocery_frame.grid(row=0,column=1,padx=10,pady=10)


rice_label = Label(grocery_frame,text="Rice",font=("Times New Roman",12,"bold"))
rice_label.grid(row=0,column=0,padx=10,pady=10)
rice_entry=Entry(grocery_frame,font=("Times New Roman",12,"bold"))
rice_entry.grid(row=0,column=1,padx=10,pady=10)
rice_entry.insert(0,0)


oil_label = Label(grocery_frame,text="Oil",font=("Times New Roman",12,"bold"))
oil_label.grid(row=1,column=0,padx=10,pady=10)
oil_entry=Entry(grocery_frame,font=("Times New Roman",12,"bold"))
oil_entry.grid(row=1,column=1,padx=10,pady=10)
oil_entry.insert(0,0)


wheat_label = Label(grocery_frame,text="Wheat",font=("Times New Roman",12,"bold"))
wheat_label.grid(row=2,column=0,padx=10,pady=10)
wheat_entry=Entry(grocery_frame,font=("Times New Roman",12,"bold"))
wheat_entry.grid(row=2,column=1,padx=10,pady=10)
wheat_entry.insert(0,0)

sugar_label = Label(grocery_frame,text="Sugar",font=("Times New Roman",12,"bold"))
sugar_label.grid(row=3,column=0,padx=10,pady=10)
sugar_entry=Entry(grocery_frame,font=("Times New Roman",12,"bold"))
sugar_entry.grid(row=3,column=1,padx=10,pady=10)
sugar_entry.insert(0,0)

tea_label = Label(grocery_frame,text="Tea",font=("Times New Roman",12,"bold"))
tea_label.grid(row=4,column=0,padx=10,pady=10)
tea_entry=Entry(grocery_frame,font=("Times New Roman",12,"bold"))
tea_entry.grid(row=4,column=1,padx=10,pady=10)
tea_entry.insert(0,0)

# cold drinks frame
cold_drinks_frame = LabelFrame(frame2,text="Cold Drinks",font=("Times New Roman",12,"bold"),fg="gold3")
cold_drinks_frame.grid(row=0,column=2)

mazaa_label = Label(cold_drinks_frame,text="Maaza",font=("Times New Roman",12,"bold"))
mazaa_label.grid(row=0,column=0,padx=10,pady=10)
mazaa_entry=Entry(cold_drinks_frame,font=("Times New Roman",12,"bold"))
mazaa_entry.grid(row=0,column=1,padx=10,pady=10)
mazaa_entry.insert(0,0)

pepsi_label = Label(cold_drinks_frame,text="Pepsi",font=("Times New Roman",12,"bold"))
pepsi_label.grid(row=1,column=0,padx=10,pady=10)
pepsi_entry=Entry(cold_drinks_frame,font=("Times New Roman",12,"bold"))
pepsi_entry.grid(row=1,column=1,padx=10,pady=10)
pepsi_entry.insert(0,0)

sprite_label = Label(cold_drinks_frame,text="Sprite",font=("Times New Roman",12,"bold"))
sprite_label.grid(row=2,column=0,padx=10,pady=10)
sprite_entry=Entry(cold_drinks_frame,font=("Times New Roman",12,"bold"))
sprite_entry.grid(row=2,column=1,padx=10,pady=10)
sprite_entry.insert(0,0)

dew_label = Label(cold_drinks_frame,text="Dew",font=("Times New Roman",12,"bold"))
dew_label.grid(row=3,column=0,padx=10,pady=10)
dew_entry=Entry(cold_drinks_frame,font=("Times New Roman",12,"bold"))
dew_entry.grid(row=3,column=1,padx=10,pady=10)
dew_entry.insert(0,0)

Coca_Cola_label = Label(cold_drinks_frame,text="Coca Cola",font=("Times New Roman",12,"bold"))
Coca_Cola_label.grid(row=4,column=0,padx=10,pady=10)
Coca_Cola_entry=Entry(cold_drinks_frame,font=("Times New Roman",12))
Coca_Cola_entry.grid(row=4,column=1,padx=10,pady=10)
Coca_Cola_entry.insert(0,0)

bill_frame = Frame(frame2)
bill_frame.grid(row=0,column=3,padx=5,pady=5)
bill_area_label = Label(bill_frame,text="Bill Area",font=("Times New Roman",12,"bold"),relief=GROOVE,bd=7)
bill_area_label.pack(fill=X)

# add scroll bar
scrollbar = Scrollbar(bill_frame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

# adding text area
textarea = Text(bill_frame,height=13,width=49,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

# bill manu frame
bill_menu = LabelFrame(root,text="Bill Menu",font=("Times New Roman",15,"bold"),fg="gold3")
bill_menu.pack()


cosmetic_price_label= Label(bill_menu,text="Cosmetic Price ",font=("Times New Roman",12,"bold"))
cosmetic_price_label.grid(row=0,column=0,padx=10,pady=10)
cosmetic_entry = Entry(bill_menu,font=("aerial",12))
cosmetic_entry.grid(row=0,column=1)

grocery_price_label= Label(bill_menu,text="Grocery Price ",font=("Times New Roman",12,"bold"))
grocery_price_label.grid(row=1,column=0,padx=10,pady=10)
grocery_entry = Entry(bill_menu,font=("aerial",12))
grocery_entry.grid(row=1,column=1)

cold_drink_price_label= Label(bill_menu,text="Cold Drink Price ",font=("Times New Roman",12,"bold"))
cold_drink_price_label.grid(row=2,column=0,padx=10,pady=10)
cold_drink_entry = Entry(bill_menu,font=("aerial",12))
cold_drink_entry.grid(row=2,column=1)

cosmetic_tax_label= Label(bill_menu,text="Cosmetic Tax ",font=("Times New Roman",12,"bold"))
cosmetic_tax_label.grid(row=0,column=2,padx=10,pady=10)
cosmetic_tax_entry = Entry(bill_menu,font=("aerial",12))
cosmetic_tax_entry.grid(row=0,column=3)

Grocery_tax_label= Label(bill_menu,text="Grocery Tax ",font=("Times New Roman",12,"bold"))
Grocery_tax_label.grid(row=1,column=2,padx=10,pady=10)
Grocery_tax_entry = Entry(bill_menu,font=("aerial",12))
Grocery_tax_entry.grid(row=1,column=3)

cold_drink_tax_label= Label(bill_menu,text="Cold Drink Tax ",font=("Times New Roman",12,"bold"))
cold_drink_tax_label.grid(row=2,column=2,padx=10,pady=10)
cold_drink_tax_entry = Entry(bill_menu,font=("aerial",12))
cold_drink_tax_entry.grid(row=2,column=3)

frame4 = Frame(bill_menu,relief=GROOVE,bd=8)
frame4.grid(row=0,column=4,rowspan=3,padx=5,pady=5)
total_button = Button(frame4,text="Total",font=("Times New Roman",20,"bold"),bg="white",bd=5,command=total)
total_button.grid(row=0,column=0,padx=10,pady=10)

bill_button = Button(frame4,text="Bill",font=("Times New Roman",20,"bold"),bg="white",bd=5,command=bill_area)
bill_button.grid(row=0,column=1,padx=10,pady=10)

email_button = Button(frame4,text="Email",font=("Times New Roman",20,"bold"),bg="white",bd=5,command=send_email)
email_button.grid(row=0,column=2,padx=10,pady=10)

clear_button = Button(frame4,text="Clear",font=("Times New Roman",20,"bold"),bg="white",bd=5,command=clear)
clear_button.grid(row=0,column=3,padx=10,pady=10)

print_button = Button(frame4,text="Print",font=("Times New Roman",20,"bold"),bg="white",bd=5,command=print_bill)
print_button.grid(row=0,column=4,sticky='news',padx=10,pady=10)

cashier_label_frame= LabelFrame(root,text="Cashier Details",font=("Aerial",12,"bold"),fg="gold3")
cashier_label_frame.pack()
cashier_label = Label(cashier_label_frame,text=" Name",font=("Times New Roman",12,"bold"))
cashier_label.grid(row=0,column=0,padx=10,pady=10)
cashier_entry = Entry(cashier_label_frame, font=("Times New Roman",12))
cashier_entry.grid(row=0,column=1,padx=10,pady=10)

cashier_sign_label = Label(cashier_label_frame,text=" Sign",font=("Times New Roman",12,"bold"))
cashier_sign_label.grid(row=0,column=2,padx=10,pady=10)
cashier_sign_entry = Entry(cashier_label_frame, font=("Times New Roman",12))
cashier_sign_entry.grid(row=0,column=3,padx=10,pady=10)

cashier_id_label = Label(cashier_label_frame,text=" Cashier ID",font=("Times New Roman",12,"bold"))
cashier_id_label.grid(row=0,column=4,padx=10,pady=10)
cashier_id_entry = Entry(cashier_label_frame, font=("Times New Roman",12))
cashier_id_entry.grid(row=0,column=5,padx=10,pady=10)

amount_l = LabelFrame(root,text='Amount and Balance',font=("Times New Roman",14,"bold"),fg="gold3")
amount_l.pack()
amount_paid_label= Label(amount_l,text="Amount",font=("Times New Roman",14,"bold"))
amount_paid_label.grid(row=0,column=0,padx=10,pady=5)
amount_paid = Entry(amount_l,font=("Times New Roman",14,"bold"))
amount_paid.grid(row=0,column=1)

balance_button = Button(amount_l,text="Balance",font=("Times New Roman",14,"bold"),command=balance_amount)
balance_button.grid(row=0,column=2,padx=10,pady=5)
balance_entry = Entry(amount_l,font=("Times New Roman",14,"bold"))
balance_entry.grid(row=0,column=3,padx=10,pady=5)

root.mainloop()
