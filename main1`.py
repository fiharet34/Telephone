from tkinter import *
import shelve

def Add():
    with shelve.open("basa.db") as basa:
        basa[entry_name.get()] = entry_number.get()
        entry_name.delete(0, END)
        entry_number.delete(0, END)
       
def Find():
    number = 0
    if entry_find.get() != "":
        for lbl in labels:
            lbl["text"] = ""
        with shelve.open("basa.db") as basa:            
            for i in basa:
                if entry_find.get().lower() in i.lower() and number != 4:
                    labels[number]["text"] = f'Имя: {i}, Номер: {basa[i]}'
                    number += 1
root = Tk()
root.geometry("280x300")
with shelve.open("basa.db") as basa:
    basa.clear()
    
name = Label(root, text = "Имя:", font = 15)
telephone = Label(root, text = "Номер:", font = 15)
labels = [Label(root, font = 15) for i in range(5)]
btn_add = Button(root, text = "+", font = 28,
                 command = lambda:(Add()))
btn_find = Button(root, text = "Найти", font = 20,
                  command = lambda:(Find()))
entry_name = Entry(root)
entry_number = Entry(root)
entry_find = Entry(root)

for i in range(5):
    labels[i].place(x = 40, y = 220 + i * 20)
    
name.place(x = 25, y = 0)
telephone.place(x = 25, y = 25)
btn_add.place(x = 125, y = 60, width = 50, height = 50)
btn_find.place(x = 125, y = 150, width = 50, height = 50)
entry_name.place(x = 95, y = 5)
entry_number.place(x = 95, y = 30)
entry_find.place(x = 95, y = 130)


root.mainloop()