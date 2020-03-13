from tkinter import*
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

root=Tk()
root.geometry("1350x750+0+0")
root.title("Food Billing System")
root.configure(background='light blue')


Tops = Frame(root,bg='Green',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('arial',60,'bold'),text='Dominos Pizzza',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)
#WE NEED SOME FRAME

BottomMainFrame=Frame(root,width=1350,height=650,bd=12,relief="raise")#THESE BOTTOM FRAME
BottomMainFrame.pack(side=BOTTOM)

f1=Frame (BottomMainFrame,width=450,height=650,bd=12,relief="raise")
f1.pack(side=LEFT)
f2=Frame (BottomMainFrame,width=450,height=650,bd=12,relief="raise")
f2.pack(side=LEFT)
f2TOP=Frame (f2,width=450,height=350,bd=4,relief="raise")
f2TOP.pack(side=TOP)
f2BOTTOM=Frame (f2,width=450,height=300,bd=4,relief="raise")
f2BOTTOM.pack(side=BOTTOM)
 
f3=Frame (BottomMainFrame,width=450,height=650,bd=12,relief="raise")
f3.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23 =IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

varVeg_Loaded=StringVar()
varPaneer_Makhani=StringVar()


varKadhai_Paneer= StringVar()
varDeluxe_Veggie=StringVar()
varExtravaganza=StringVar()
varChicken_Sausage=StringVar()
varNon_Veg_Supreme=StringVar()
varDominator=StringVar()

varTea=StringVar()
varCola=StringVar()
varCoffee=StringVar()
varOrange=StringVar()
vaBottleWater=StringVar()

varVanillaCone=StringVar()
varVanillaShake=StringVar()
varStrawberryShake=StringVar()
varCake =StringVar()
varIce_Cream =StringVar()
varPepsi =StringVar()
varMirinda =StringVar()
varLipton_Ice_Tea=StringVar()
varChange=StringVar()
varSubTotal=StringVar()
varTax=StringVar()
varTotal=StringVar()
varVat=StringVar()
varIce_Cream.set("0")
varPepsi.set("0") 
varMirinda.set("0") 
varLipton_Ice_Tea.set("0") 

varVeg_Loaded.set("0")
varPaneer_Makhani.set("0")
varKadhai_Paneer.set("0")
varDeluxe_Veggie.set("0")
varExtravaganza.set("0")
varChicken_Sausage.set("0")
varNon_Veg_Supreme.set("0")
varDominator.set("0")
varTax.set("0")
varVat.set("")
varCake.set("0") 
varChange.set("2.5")
varSubTotal.set("0")

varTotal.set("0")

def iExit():
    qExit=messagebox.askyesno("Dominos Pizza","Do you want to quit?")
    if qExit>0:
        root.destroy()
        return

def Reset():
    varIce_Cream.set("0")
    varPepsi.set("0") 
    varMirinda.set("0") 
    varLipton_Ice_Tea.set("0") 
    varVeg_Loaded.set("0")
    varPaneer_Makhani.set("0")
    varKadhai_Paneer.set("0")
    varDeluxe_Veggie.set("0")
    varExtravaganza.set("0")
    varChicken_Sausage.set("0")
    varNon_Veg_Supreme.set("0")
    varDominator.set("0")
    varTax.set("0")
  
   
    varCake.set("0") 
    varSubTotal.set("0")
    varTotal.set("0")

    
    txtVeg_Loaded.configure(state=DISABLED)
    txtPaneer_Makhani.configure(state=DISABLED)
    txtKadhai_Paneer.configure(state=DISABLED)
    txtDeluxe_Veggie.configure(state=DISABLED)
    txtExtravaganza.configure(state=DISABLED)
    txtChicken_Sausage.configure(state=DISABLED)
    txtNon_Veg_Supreme.configure(state=DISABLED)
    txtDominator.configure(state=DISABLED)
    txtCake.configure(state=DISABLED)
    txtIce_Cream.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtMirinda.configure(state=DISABLED)
    txtLipton_Ice_Tea.configure(state=DISABLED)
    
    txtTax.configure(state=DISABLED)
   
    txtSubTotal.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)

def chkVeg_Loaded():
    if(var1.get()==1):
        txtVeg_Loaded.configure(state=NORMAL)
        varVeg_Loaded.set("")
    elif(var1.get()==0):
        txtVeg_Loaded.configure(state=DISABLED)
        varVeg_Loaded.set("0")

def chkPaneer_Makhani():
    if(var2.get()==1):
        txtPaneer_Makhani.configure(state=NORMAL)
        varPaneer_Makhani.set("")
    elif(var2.get()==0):
        txtPaneer_Makhani.configure(state=DISABLED)
        varPaneer_Makhani.set("0")

def chkKadhai_Paneer():
    if(var3.get()==1):
        txtKadhai_Paneer.configure(state=NORMAL)
        varKadhai_Paneer.set("")
    elif(var3.get()==0):
        txtKadhai_Paneer.configure(state=DISABLED)
        varKadhai_Paneer.set("0")

def chkDeluxe_Veggie():
    if(var4.get()==1):
        txtDeluxe_Veggie.configure(state=NORMAL)
        varDeluxe_Veggie.set("")
    elif(var4.get()==0):
        txtDeluxe_Veggie.configure(state=DISABLED)
        varDeluxe_Veggie.set("0")

def chkExtravaganza():
    if(var5.get()==1):
        txtExtravaganza.configure(state=NORMAL)
        varExtravaganza.set("")
    elif(var5.get()==0):
        txtExtravaganza.configure(state=DISABLED)
        varExtravaganza.set("0")

def chkChicken_Sausage ():
    if(var6.get()==1):
        txtChicken_Sausage .configure(state=NORMAL)
        varChicken_Sausage .set("")
    elif(var6.get()==0):
        txtChicken_Sausage .configure(state=DISABLED)
        varChicken_Sausage .set("0")


def chkNon_Veg_Supreme():
    if(var7.get()==1):
        txtNon_Veg_Supreme.configure(state=NORMAL)
        varNon_Veg_Supreme.set("")
    elif(var7.get()==0):
        txtNon_Veg_Supreme.configure(state=DISABLED)
        varNon_Veg_Supreme.set("0")

def chkDominator():
    if(var8.get()==1):
        txtDominator.configure(state=NORMAL)
        varDominator.set("")
    elif(var8.get()==0):
        txtDominator.configure(state=DISABLED)
        varDominator.set("0")


def chkCake():
    if(var9.get()==1):
        txtCake.configure(state=NORMAL)
        varCake.set("")
    elif(var9.get()==0):
        txtCake.configure(state=DISABLED)
        varCake.set("0")

def chkIce_Cream():
    if(var10.get()==1):
        txtIce_Cream.configure(state=NORMAL)
        varIce_Cream.set("")
    elif(var10.get()==0):
        txtIce_Cream.configure(state=DISABLED)
        varIce_Cream.set("0")

def chkPepsi():
    if(var11.get()==1):
        txtPepsi.configure(state=NORMAL)
        varPepsi.set("")
    elif(var11.get()==0):
        txtPepsi.configure(state=DISABLED)
        varPepsi.set("0")

def chkMirinda():
    if(var12.get()==1):
        txtMirinda.configure(state=NORMAL)
        varMirinda.set("")
    elif(var12.get()==0):
        txtMirinda.configure(state=DISABLED)
        varMirinda.set("0")

def chkLipton_Ice_Tea():
    if(var13.get()==1):
        txtLipton_Ice_Tea.configure(state=NORMAL)
        varLipton_Ice_Tea.set("")
    elif(var13.get()==0):
        txtLipton_Ice_Tea.configure(state=DISABLED)
        varLipton_Ice_Tea.set("0")

def costofmeal():
    cgst=float(varChange.get())
    sgst=float(varTax.get())
    meal1=float(varVeg_Loaded.get())
    meal2=float(varPaneer_Makhani.get())
    meal3=float(varKadhai_Paneer.get())
    meal4=float(varDeluxe_Veggie.get())
    meal5=float(varExtravaganza.get())
    meal6=float(varChicken_Sausage.get())
    meal7=float(varNon_Veg_Supreme.get())
    meal8=float(varDominator.get())
    meal9=float(varCake.get())
    meal10=float(varIce_Cream.get())
    meal11=float(varPepsi.get())
    meal12=float(varMirinda.get())
    meal13=float(varLipton_Ice_Tea.get())

    iTotal1=((meal1*100) + (meal2*150) + (meal3*150) + (meal4*140)+ (cgst*2.5))
    iTotal2=((meal5*200) + (meal6*150) + (meal7*200) + (meal8*270)+(sgst*2.5))
    iTotal3=((meal9*100) + (meal10*85) + (meal11*60) + (meal12*60)+(meal13*120))

    iCost=(iTotal1+iTotal2+iTotal3)
    iTax=(iCost*2.5)/100
    varSubTotal.set(iCost)
    varTotal.set(iCost+iTax)


###########################################################################################################################################################################

lblMeal=Label(f1, font=("arial",16, "bold"), text="VEG PIZZA")
lblMeal.grid(row=0, column=0)

Veg_Loaded =Checkbutton(f1, text="Veg Loaded \t100", variable=var1, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkVeg_Loaded).grid(row=1,column=0,sticky=W)
txtVeg_Loaded=Entry(f1,font=("arial",16,"bold"),textvariable=varVeg_Loaded, width=6,justify="center", state=DISABLED)
txtVeg_Loaded.grid(row=1,column=1)

Paneer_Makhani =Checkbutton(f1, text="Paneer Makhani \t150", variable=var2, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkPaneer_Makhani).grid(row=2,column=0,sticky=W)
txtPaneer_Makhani=Entry(f1,font=("arial",16,"bold"),textvariable=varPaneer_Makhani, width=6,justify="center", state=DISABLED)
txtPaneer_Makhani.grid(row=2,column=1)

Kadhai_Paneer=Checkbutton(f1, text="Kadhai Paneer \t150", variable=var3, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkKadhai_Paneer).grid(row=3,column=0,sticky=W)
txtKadhai_Paneer=Entry(f1,font=("arial",16,"bold"),textvariable=varKadhai_Paneer, width=6,justify="center", state=DISABLED)
txtKadhai_Paneer.grid(row=3,column=1)

Deluxe_Veggie =Checkbutton(f1, text="Deluxe Veggie \t140 ", variable=var4, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkDeluxe_Veggie).grid(row=4,column=0,sticky=W)
txtDeluxe_Veggie=Entry(f1,font=("arial",16,"bold"),textvariable=varDeluxe_Veggie, width=6,justify="center" ,state=DISABLED)
txtDeluxe_Veggie.grid(row=4,column=1)

Extravaganza=Checkbutton(f1, text="Extravaganza \t200", variable=var5, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkExtravaganza).grid(row=5,column=0,sticky=W)
txtExtravaganza=Entry(f1,font=("arial",16,"bold"),textvariable=varExtravaganza, width=6,justify="center" ,state=DISABLED)
txtExtravaganza.grid(row=5,column=1)

lblNon_Veg=Label(f1, font=("arial", 16, "bold"), text="\nNon Veg\n")
lblNon_Veg.grid(row=6, column=0)

Chicken_Sausage =Checkbutton(f1, text="Chicken Sausage \t150", variable=var6, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkChicken_Sausage ).grid(row=7,column=0,sticky=W)
txtChicken_Sausage=Entry(f1,font=("arial",16,"bold"),textvariable=varChicken_Sausage, width=6,justify="center", state=DISABLED)
txtChicken_Sausage.grid(row=7,column=1)

Non_Veg_Supreme =Checkbutton(f1, text="Non Veg Supreme \t200", variable=var7, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkNon_Veg_Supreme).grid(row=8,column=0,sticky=W)
txtNon_Veg_Supreme=Entry(f1,font=("arial",16,"bold"),textvariable=varNon_Veg_Supreme, width=6,justify="center", state=DISABLED)
txtNon_Veg_Supreme.grid(row=8,column=1)

Dominator =Checkbutton(f1, text="Dominator \t270", variable=var8, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkDominator ).grid(row=9,column=0,sticky=W)
txtDominator =Entry(f1,font=("arial",16,"bold"),textvariable=varDominator , width=6,justify="center", state=DISABLED)
txtDominator .grid(row=9,column=1)

lbllblspace=Label(f1,text="\n\n\n\n\n")
lbllblspace.grid(row=10,column=0)

########################frame2#####################################################################################################################################
lblMeal=Label(f2TOP, font=("arial", 16, "bold"), text="Beverages and Dessert")
lblMeal.grid(row=0, column=0)

Cake =Checkbutton(f2TOP, text="Cake\t\t100", variable=var9, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkCake).grid(row=1,column=0,sticky=W)
txtCake=Entry(f2TOP,font=("arial",16,"bold"),textvariable=varCake, width=6,justify="center", state=DISABLED)
txtCake.grid(row=1,column=1)

Ice_Cream =Checkbutton(f2TOP, text="Ice Cream \t85", variable=var10, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkIce_Cream ).grid(row=2,column=0,sticky=W)
txtIce_Cream =Entry(f2TOP,font=("arial",16,"bold"),textvariable=varIce_Cream , width=6,justify="center", state=DISABLED)
txtIce_Cream .grid(row=2,column=1)

Pepsi=Checkbutton(f2TOP, text="Pepsi\t\t60", variable=var11, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkPepsi).grid(row=3,column=0,sticky=W)
txtPepsi=Entry(f2TOP,font=("arial",16,"bold"),textvariable=varPepsi, width=6,justify="center", state=DISABLED)
txtPepsi.grid(row=3,column=1)

Mirinda =Checkbutton(f2TOP, text="Mirinda\t \t60", variable=var12, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkMirinda).grid(row=4,column=0,sticky=W)
txtMirinda=Entry(f2TOP,font=("arial",16,"bold"),textvariable=varMirinda, width=6,justify="center" ,state=DISABLED)
txtMirinda.grid(row=4,column=1)

Lipton_Ice_Tea=Checkbutton(f2TOP, text="Lipton Ice Tea \t120", variable=var13, onvalue=1,offvalue=0,
                   font=("arial",16,"bold"),command=chkLipton_Ice_Tea).grid(row=5,column=0,sticky=W)
txtLipton_Ice_Tea=Entry(f2TOP,font=("arial",16,"bold"),textvariable=varLipton_Ice_Tea, width=6,justify="center" ,state=DISABLED)
txtLipton_Ice_Tea.grid(row=5,column=1)

###################################################################################################################################################################
lblPaymentMethod=Label(f2BOTTOM, font=("arial", 16, "bold"), text="Payment method",bd=10,width=16,anchor="w")     
lblPaymentMethod.grid(row=0, column=0)

lblChange=Label(f2BOTTOM, font=("arial", 16, "bold"), text="CGST @ 9%",bd=10,anchor="w")     
lblChange.grid(row=0, column=1)
txtChange=Entry(f2BOTTOM,font=("arial",16,"bold"),textvariable=varChange, width=6,justify="center", state=DISABLED)
txtChange.grid(row=0,column=2)

cmbPaymentMethod=ttk.Combobox(f2BOTTOM,textvariable=var22,state="readonly",font=("arial",18,"bold"),width=20)
cmbPaymentMethod["value"]=("cash")
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1,column=0)

lblTax=Label(f2BOTTOM, font=("arial", 16, "bold"), text="SGST/UTGST 9%",bd=10,anchor="w")     
lblTax.grid(row=1, column=1)
txtTax=Entry(f2BOTTOM,font=("arial",16,"bold"),textvariable=varTax, width=6,justify="center", state=DISABLED)
txtTax.grid(row=1,column=2)

#txtPayment=Entry(f2BOTTOM,font=("arial",16,"bold"),textvariable=varChange, width=6,justify="center", state=DISABLED)
#txtPayment.grid(row=2,column=0)
lblSubTotal=Label(f2BOTTOM, font=("arial", 16, "bold"), text="Sub total",bd=10,anchor="w")     
lblSubTotal.grid(row=2, column=1)
txtSubTotal=Entry(f2BOTTOM,font=("arial",16,"bold"),textvariable=varSubTotal, width=6,justify="center", state=DISABLED)
txtSubTotal.grid(row=2,column=2)


lblTotal=Label(f2BOTTOM, font=("arial", 16, "bold"), text="Total",bd=10,anchor="w")     
lblTotal.grid(row=3, column=1)
txtTotal=Entry(f2BOTTOM,font=("arial",16,"bold"),textvariable=varTotal, width=6,justify="center", state=DISABLED)
txtTotal.grid(row=3,column=2)
###############################################################################################################################################################
btnTotal=Button(f2BOTTOM,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
                text="Total ",command= costofmeal).grid(row=4,column=0)
btnReset=Button(f2BOTTOM,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
                text="RESET",command=Reset).grid(row=4,column=1)

btnExit=Button(f2BOTTOM,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
                text="Exit",command=lambda: iExit()).grid(row=4,column=2)
lblspace=Label(f2BOTTOM, text="\n\n\n\n\n\n")
lblspace.grid(row=5,column=0)
root.mainloop()
