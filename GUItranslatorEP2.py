#GUItranslator
from tkinter import *
from tkinter import ttk
from googletrans import Translator
translator = Translator()

GUI = Tk()
GUI.geometry('500x300')
GUI.title('boykrap by chiangmai')

FONT = ('Angsana New',15)

L = ttk.Label(GUI,text='กรุรากรอกคำศัพท์ที่ต้องการ',font=FONT)
L.pack()

#Entry
v_vocab = StringVar()
E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)


#button
def Translate():
    vocab = v_vocab.get()
    meaning = translator.translate(vocab,dest='th')
    print(vocab+' '+meaning.text)
    v_result.set(vocab+' '+meaning.text)


B1 = ttk.Button(GUI,text='Translate',command=Translate)
B1.pack(ipadx=20,ipady=10)

L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack(pady=20)

v_result = StringVar()
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT)

GUI.mainloop()

