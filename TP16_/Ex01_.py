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
    
btn_frame=tk.Frame(cal)
btn_frame.grid(row=1,column=0)

sub_btnF_1=tk.Frame(btn_frame)
sub_btnF_1.grid(row=0,column=0)

sub_btnF_2=tk.Frame(btn_frame)
sub_btnF_2.grid(row=0,column=1)

tk.Button(sub_btnF_1, text="+", command=lambda: calculer("add")).grid(row=0, column=0)
tk.Button(sub_btnF_1, text="-", command=lambda: calculer("sub")).grid(row=0,column=1)
tk.Button(sub_btnF_1, text="x", command=lambda: calculer("mul")).grid(row=1, column=0)
tk.Button(sub_btnF_1, text="/", command=lambda: calculer("div")).grid(row=1,column=1)
tk.Button(sub_btnF_2, text="^", command=lambda: calculer("pui")).grid(row=0, column=0)
tk.Button(sub_btnF_2, text="%", command=lambda: calculer("mod")).grid(row=1,column=0)


resZone=tk.Label(cal, textvariable=res)
resZone.grid(row=1,column=1)

cal.mainloop()