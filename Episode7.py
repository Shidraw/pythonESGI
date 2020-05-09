from functools import partial
from tkinter import Tk, Label,Entry, Button, StringVar

def checkvalue(label,StringVar,StringVar1,StringVar2):
    line=StringVar.get()
    words = line.split("\\")
    label.config(text=text)
    StringVar2.set(words[2])
    StringVar1.set(words[3])



root = Tk() # Création de la fenêtre racine
text = StringVar(root)
text1 = StringVar(root)
text2 = StringVar(root)
label = Label(root, text='')
label1 = Label(root, text="Source")
label2 = Label(root, text="Destination")
entry_name1 = Entry(root, textvariable=text2)
entry_name2 = Entry(root, textvariable=text1)
entry_name = Entry(root, textvariable=text)
button = Button(root, text='CLEAN',
                command=partial(checkvalue, label, text,text1,text2))


label1.grid(column=3, row=4)
label2.grid(column=3, row=0)
label.grid(column=0, row=0)
entry_name.grid(column=3, row=2)
button.grid(column=3, row=3)
entry_name1.grid(column=0, row=6)
entry_name2.grid(column=4, row=6)

root.mainloop() # Lancement de la boucle principale