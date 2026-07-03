import tkinter as tk

cal=tk.Tk()
cal.geometry("500x300")
cal.title("Calculatrice")

res=tk.StringVar()

#tk.Label(cal,text="nombre 1: ").pack()
n1=tk.Entry(cal)
n1.grid(row=0,column=0)

#tk.Label(cal,text="nombre 2: ").pack()
n2=tk.Entry(cal)
n2.grid(row=0,column=1)

def calculer(op):
    if not n1.get() or not n2.get():
        res.set("Error: Champs vides!!")
        return
    
    val1=float(n1.get())
    val2=float(n2.get())
    result=0
    if op=="add":
        result=val1+val2
    elif op=="sub":
        result=val1-val2
    elif op=="mul":
        result=val1*val2
    elif op=="div":
        if val2==0:
            raise ZeroDivisionError
        result=val1/val2
    elif op=="mod":
        result=val1%val2
    elif op=="pui":
        result=val1**val2
    
    res.set(result)

    if result>0:
        resZone.config(fg="green")
    elif result<0:
        resZone.config(fg="red")
    else:
        resZone.config(fg="blue")


def effacer():
    n1.delete(0,tk.END)
    n2.delete(0,tk.END)
    res.set("")
    

def quitter():
    cal.destroy()


btn_frame=tk.Frame(cal)
btn_frame.grid(row=1,column=0)

sub_btnF_1=tk.Frame(btn_frame)
sub_btnF_1.grid(row=0,column=0)

sub_btnF_2=tk.Frame(btn_frame)
sub_btnF_2.grid(row=0,column=1)

util_btnF=tk.Frame(cal)
util_btnF.grid(row=1,column=1)

tk.Button(sub_btnF_1, text="+", command=lambda: calculer("add")).grid(row=0, column=0)
tk.Button(sub_btnF_1, text="-", command=lambda: calculer("sub")).grid(row=0,column=1)
tk.Button(sub_btnF_1, text="x", command=lambda: calculer("mul")).grid(row=1, column=0)
tk.Button(sub_btnF_1, text="/", command=lambda: calculer("div")).grid(row=1,column=1)
tk.Button(sub_btnF_2, text="^", command=lambda: calculer("pui")).grid(row=0, column=0)
tk.Button(sub_btnF_2, text="%", command=lambda: calculer("mod")).grid(row=1,column=0)

tk.Button(util_btnF, text="Effacer", command=lambda: effacer()).grid(row=1, column=0)
tk.Button(util_btnF, text="Quitter", command=lambda: quitter()).grid(row=1,column=1)

resZone=tk.Label(util_btnF, textvariable=res)
resZone.grid(row=0,column=0)

cal.mainloop()