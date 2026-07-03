import tkinter as tk

cal=tk.Tk()
cal.geometry("500x300")
cal.title("Calculatrice")

res=tk.StringVar()

tk.Label(cal,text="nombre 1: ").pack()
n1=tk.Entry(cal).pack(pady=5)

tk.Label(cal,text="nombre 2: ").pack()
n2=tk.Entry(cal).pack(pady=5)

def calculer(op):
     if not n1.get() or not n2.get():
            res.set("Erreur : Champs vides")
            return

        # Convert to float
        val1 = float(n1.get())
        val2 = float(n2.get())
        
        res = 0
        if op == "add":
            res = val1 + val2
        elif op == "sub":
            res = val1 - val2
        elif op == "mul":
            res = val1 * val2
        elif op == "div":
            if val2 == 0:
                raise ZeroDivisionError
            res = val1 / val2
            
        res.set(f"Résultat : {res}")

cal.mainloop()