from tkinter import *
import random
import socket
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port=3006,
  password="",
  database='mini'
)
mycursor = mydb.cursor()
root=Tk()
First_Frame=LabelFrame(root,padx=400,pady=300)
def afterent():
    global First_Frame
    num="+91"+number.get()
    a,otp=['0','1','2','3','4','5','6','7','8','9'],""
    for i in range(6):
        otp+=a[random.randint(0,9)]

    host = '192.168.0.101'
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    data_to_send = num
    client_socket.send(data_to_send.encode())

    port = 3007

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    data_to_send = str(otp)
    client_socket.send(data_to_send.encode())

    client_socket.close()
    def afterent_2():

        if otp==otp1.get():
            First_Frame.grid_forget()

            def account(val):
                if val=="1":
                    Second_Frame.grid_forget()

                    def detail1():
                        gen.get()
                        nat.get()
                        mar.get()
                        namof.get()
                        mycursor.execute(f"insert into info values('{bname.get()}','{bcode.get()}','{C_Id.get()}','{prop.get()}','{AccNo.get()}','{type.get()}')")
                        #mycursor.execute(f"insert into info values('dokw','owdj','cknce','New','{a}','Minor')")
                        mydb.commit()
                        return

                    Fourth_Label=Label(root,text="Branch Name: ")
                    bname=Entry()

                    Fifth_Label=Label(root,text="Branch Code: ")
                    bcode=Entry()

                    Sixth_Label=Label(root,text="Customer Id: ")
                    C_Id=Entry()

                    Seventh_Label=Label(root,text="Application Type")
                    prop=StringVar()
                    prop.set("Unknown")
                    Opt1=Radiobutton(root,text="New",variable=prop,value="New")
                    Opt2=Radiobutton(root,text="Update",variable=prop,value="Update")

                    Eighth_Label=Label(root,text="Account Number: ")
                    AccNo=Entry()

                    Ninth_Label=Label(root,text="Account Type")
                    type=StringVar()
                    type.set("Unknown")
                    Opt3=Radiobutton(root,text="Normal",variable=type,value="Normal")
                    Opt4=Radiobutton(root,text="Small",variable=type,value="Small")
                    Opt5=Radiobutton(root,text="Minor",variable=type,value="Minor")

                    Tenth_Label=Label(root,text="1. Name: ")
                    name=Entry()

                    Label_11=Label(root,text="2. Maiden Name: ")
                    mname=Entry()

                    Label_12=Label(root,text="3. Date of Birth: ")
                    dob=Entry()

                    Label_14=Label(root,text="4. Gender: ")
                    gen=StringVar()
                    gen.set("Unknown")
                    Opt6=Radiobutton(root,text="Male",variable=gen,value="Male")
                    Opt7=Radiobutton(root,text="Female",variable=gen,value="Female")
                    Opt8=Radiobutton(root,text="Other",variable=gen,value="Other")
                    

                    Label_15=Label(root,text="5. Marital Status: ")
                    mar=StringVar()
                    mar.set("Unknown")
                    Opt9=Radiobutton(root,text="Married",variable=mar,value="Married")
                    Opt10=Radiobutton(root,text="Unmarried",variable=mar,value="Unmarried")
                    Opt11=Radiobutton(root,text="Others",variable=mar,value="Others")

                    Label_16=Label(root,text="6. Number of Dependers: ")
                    dep=Entry()

                    Label_17=Label(root,text="7. Name of: ")
                    namof=StringVar()
                    namof.set("Unknown")
                    Opt12=Radiobutton(root,text="Father",variable=namof,value="Father")
                    Opt13=Radiobutton(root,text="Mother",variable=namof,value="Mother")
                    Opt14=Radiobutton(root,text="Spouse",variable=namof,value="Spouse")

                    namerel=Entry()

                    Label_18=Label(root,text="8. Name of Guardian: ")
                    nameg=Entry()

                    Label_19=Label(root,text="9. Nationality: ")
                    nat=StringVar()
                    nat.set("Unknown")
                    Opt15=Radiobutton(root,text="In-Indian",variable=nat,value="In-Indian")
                    Opt16=Radiobutton(root,text="Others",variable=nat,value="Others")
                    
                    Label_20=Label(root,text="10. Country Name: ")
                    countn=Entry()

                    Label_21=Label(root,text="11. Citizenship: ")
                    citi=Entry()

                    Label_9_1=Label(root,text="Presonal Details")

                    Label_22=Label(root,text="11. Occupation Type Service: ")
                    ocp=StringVar()
                    ocp.set('Unknown')
                    Opt17=Radiobutton(root,text='State Govt.',variable=ocp,value='State Govt.')
                    Opt18=Radiobutton(root,text='Central Govt.',variable=ocp,value='Central Govt.')
                    Opt19=Radiobutton(root,text='Public Sector Undertaking',variable=ocp,value='Public Sector Undertaking')
                    Opt20=Radiobutton(root,text='Defence',variable=ocp,value='Defence')
                    Opt21=Radiobutton(root,text='Private Sector',variable=ocp,value='Private Sector')

                    Label_23=Label(root,text="Place of Posting")
                    pop=Entry()

                    Label_24=Label(root,text="Business")
                    Opt22=Radiobutton(root,text='Industrialist',variable=ocp,value='Industrialist')
                    Opt23=Radiobutton(root,text='Trade Sector',variable=ocp,value='Trade Sector')
                    Opt24=Radiobutton(root,text='Service Sector',variable=ocp,value='Service Sector')
                    Opt25=Radiobutton(root,text='Migrant Labour',variable=ocp,value='Migrant Labour')
                    Opt26=Radiobutton(root,text='Contractor',variable=ocp,value='Contractor')
                    Opt27=Radiobutton(root,text='Jeweller',variable=ocp,value='Jeweller')
                    Opt28=Radiobutton(root,text='Pawn Shop',variable=ocp,value='Pawn Shop')
                    Opt29=Radiobutton(root,text='Import/Export Customer',variable=ocp,value='Import/Export Customer')
                    Opt30=Radiobutton(root,text='Other Self Employed',variable=ocp,value='Other Self Employed')

                    Label_25=Label(root,text="Other")
                    Opt31=Radiobutton(root,text='Medical Prof.',variable=ocp,value='Medical Prof.')
                    Opt32=Radiobutton(root,text='Legal Prof.',variable=ocp,value='Legal Prof.')
                    Opt33=Radiobutton(root,text='CA/ICWA/Taxation/Finance',variable=ocp,value='CA/ICWA/Taxation/Finance')
                    Opt34=Radiobutton(root,text='Eng./Architect/Tech Consultant',variable=ocp,value='Eng./Architect/Tech Consultant')
                    Opt35=Radiobutton(root,text='Retired',variable=ocp,value='Retired')
                    Opt36=Radiobutton(root,text='Journalist',variable=ocp,value='Journalist')
                    Opt37=Radiobutton(root,text='Housewife',variable=ocp,value='Housewife')
                    Opt38=Radiobutton(root,text='Student',variable=ocp,value='Student')
                    Opt39=Radiobutton(root,text='Share and Stock broker',variable=ocp,value='Share and Stock broker')
                    Opt40=Radiobutton(root,text='Oth. Proffesional',variable=ocp,value='Oth. Proffesional')
                    Opt41=Radiobutton(root,text='Agriculture',variable=ocp,value='Agriculture')
                    Opt42=Radiobutton(root,text='Political and Social Worker',variable=ocp,value='Political and Social Worker')

                    Label_26=Label(root,text='Not Categorized Please Specify: ')
                    prof=Entry()

                    
                    Fourth_Button=Button(root,text="Submit",command=detail1)
                    
                    Fourth_Label.grid(row=0,column=0)
                    bname.grid(row=0,column=1)
                    Fifth_Label.grid(row=0,column=2)
                    bcode.grid(row=0,column=3)
                    Sixth_Label.grid(row=1,column=0)
                    C_Id.grid(row=1,column=1)
                    Seventh_Label.grid(row=1,column=2)
                    Opt1.grid(row=1,column=3)
                    Opt2.grid(row=1,column=4)
                    Eighth_Label.grid(row=2,column=0)
                    AccNo.grid(row=2,column=1)
                    Ninth_Label.grid(row=2,column=2)
                    Opt3.grid(row=2,column=3)
                    Opt4.grid(row=2,column=4)
                    Opt5.grid(row=2,column=5)
                    Label_9_1.grid(row=3,column=0)
                    Tenth_Label.grid(row=4,column=0)
                    name.grid(row=4,column=1)
                    Label_11.grid(row=5,column=0)
                    mname.grid(row=5,column=1)
                    Label_12.grid(row=6,column=0)
                    dob.grid(row=6,column=1)
                    Label_14.grid(row=6,column=2)
                    Opt6.grid(row=6,column=3)
                    Opt7.grid(row=6,column=4)
                    Opt8.grid(row=6,column=5)
                    Label_15.grid(row=7,column=0)
                    Opt9.grid(row=7,column=1)
                    Opt10.grid(row=7,column=2)
                    Opt11.grid(row=7,column=3)
                    Label_16.grid(row=7,column=4)
                    dep.grid(row=7,column=5)
                    Label_17.grid(row=8,column=0)
                    Opt12.grid(row=8,column=1)
                    Opt13.grid(row=8,column=2)
                    Opt14.grid(row=8,column=3)
                    namerel.grid(row=9,column=0)
                    Label_18.grid(row=10,column=0)
                    Label_19.grid(row=11,column=0)
                    Opt15.grid(row=11,column=1)
                    Opt16.grid(row=11,column=2)
                    Label_20.grid(row=11,column=3)
                    countn.grid(row=11,column=4)
                    Label_21.grid(row=11,column=5)
                    citi.grid(row=11,column=6)
                    Label_22.grid(row=12,column=0)
                    Opt17.grid(row=12,column=1)
                    Opt18.grid(row=12,column=2)
                    Opt19.grid(row=12,column=3)
                    Opt20.grid(row=12,column=4)
                    Opt21.grid(row=12,column=5)
                    Label_23.grid(row=13,column=0)
                    pop.grid(row=13,column=1)
                    Label_24.grid(row=14,column=0)
                    Opt22.grid(row=14,column=1)
                    Opt23.grid(row=14,column=2)
                    Opt24.grid(row=14,column=3)
                    Opt25.grid(row=14,column=4)
                    Opt26.grid(row=14,column=5)
                    Opt27.grid(row=14,column=6)
                    Opt28.grid(row=14,column=7)
                    Opt29.grid(row=14,column=8)
                    Opt30.grid(row=15,column=1)
                    Label_25.grid(row=16,column=0)
                    Opt31.grid(row=16,column=1)
                    Opt32.grid(row=16,column=2)
                    Opt33.grid(row=16,column=3)
                    Opt34.grid(row=16,column=4)
                    Opt35.grid(row=16,column=5)
                    Opt36.grid(row=16,column=6)
                    Opt37.grid(row=16,column=7)
                    Opt38.grid(row=16,column=8)
                    Opt39.grid(row=17,column=1)
                    Opt40.grid(row=17,column=2)
                    Opt41.grid(row=17,column=3)
                    Opt42.grid(row=17,column=4)
                    Label_26.grid(row=18,column=0)
                    prof.grid(row=18,column=1)
                    Fourth_Button.grid(row=19,column=0)


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
