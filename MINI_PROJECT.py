from tkinter import *
import random
import pywhatkit as p
root=Tk()
First_Frame=LabelFrame(root,padx=400,pady=300)
def afterent():
    global First_Frame
    otp=random.randint(100000,999999)
    num="+91"+number.get()
    p.sendwhatmsg_instantly(num,str(otp),tab_close=True,close_time=3)
    def afterent_2():
        if str(otp)==otp1.get():
            First_Frame.grid_forget()

            def account(val):
                if val=="1":
                    Second_Frame.grid_forget()
                    Third_Frame=LabelFrame(root,padx=400,pady=300)
                    Fourth_Label=Label(Third_Frame,text="We are excited to open a bank account with you!!")

                    Third_Frame.grid(row=0,column=0,padx=200)
                    Fourth_Label.grid(row=0,column=0)


            todo=StringVar()
            todo.set("Bank Account")

            Second_Frame=LabelFrame(root,padx=400,pady=300)
                
            First_Rbutton=Radiobutton(Second_Frame,text="To open a bank account",variable=todo,value=1)
            Third_Button=Button(Second_Frame,text="Submit",command=lambda: account(todo.get()))

            Second_Frame.grid(row=0,column=0,padx=200)
            First_Rbutton.grid(row=0,column=0)
            Third_Button.grid(row=4,column=0)
        else:
            number.delete(0,END)
            Third_Label.grid_forget()
            otp1.grid_forget()
            Second_Button.grid_forget()
        return

    Third_Label=Label(First_Frame,text="One Time Password",font=("Helvetica 15 bold italic"))
    otp1=Entry(First_Frame)
    Second_Button=Button(First_Frame,text="Enter",font=("Helvetica 15 bold italic"),command=afterent_2)

    Third_Label.grid(row=4,column=0)
    otp1.grid(row=4,column=1)
    Second_Button.grid(row=5,column=0)
    return

First_Label=Label(First_Frame,text="LOGIN",font=("Helvetica 25 bold italic"))
Second_Label=Label(First_Frame,text="Phone Number: ",font=("Helvetica 15 bold italic"))


number=Entry(First_Frame)


First_Button=Button(First_Frame,text="Enter",font=("Helvetica 15 bold italic"),command=afterent)


First_Frame.grid(row=0,column=0,padx=200)

First_Label.grid(row=0,column=0)
Second_Label.grid(row=1,column=0)
number.grid(row=1,column=1)
First_Button.grid(row=3,column=0)

mainloop()