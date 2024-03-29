from tkinter import * #import all function inside main package
from tkinter import ttk

GUI = Tk()
GUI.title('Program for Knowledge')
GUI.geometry('600x600')

L1 = ttk.Label(GUI,text='หัวข้อความรู้',font=('Angsana New',18))
L1.pack()

E1 = ttk.Entry(GUI,font=('Angsana New',20),width=50)
E1.pack()

L2 = ttk.Label(GUI,text='รายละเอียด',font=('Angsana New',20))
L2.pack()

T1 = Text(GUI,font=('Angsana New',20),height=8,width=50)
T1.pack()

B1 = ttk.Button(GUI,text='บันทึก')
B1.pack(pady =10,ipadx=20,ipady=10)


GUI.mainloop()