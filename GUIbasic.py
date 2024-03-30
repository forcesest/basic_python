from tkinter import * #import all function inside main package
from tkinter import ttk , messagebox
import csv
import os

path = os.getcwd()

notebutton = os.path.join(path,'note.png')
noteicon = os.path.join(path,'noteicon.ico')

print('PATH',path)

def writecsv(data):
    #data = ['john',14,500]
    csvfile = os.path.join(path,'knowledge.csv')
    with open('knowledge.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #FW = File Writer
        fw.writerow(data)






GUI = Tk()
GUI.title('Program for Knowledge')
GUI.geometry('500x550')
GUI.iconbitmap(noteicon)


F1 = Frame(GUI)
F1.place(x=20,y=50)

L1 = ttk.Label(F1,text='หัวข้อความรู้',font=('Angsana New',18))
L1.pack()

v_title = StringVar()

E1 = ttk.Entry(F1,textvariable=v_title,font=('Angsana New',20),width=50)
E1.pack()

L2 = ttk.Label(F1,text='รายละเอียด',font=('Angsana New',20))
L2.pack()

T1 = Text(F1,font=('Angsana New',20),height=8,width=50)
T1.pack()

def save():
    title = v_title.get()
    textbox = T1.get(1.0,"end-1c")
    print('--------------')
    print(title)
    print('--------------')
    print(textbox)
    print('--------------')
    data = [title,textbox]
    writecsv(data)
    v_title.set('') #clear data after save
    T1.delete('1.0',END) #clear text box



B1 = ttk.Button(F1,text='บันทึก',command=save)
B1.pack(pady =10,ipadx=20,ipady=10)

#################################BUTTON Flashcard####################################
def readcsv():
    with open('knowledge.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data
    

knowledgelist = readcsv()
print(knowledgelist)
    


# try:
#     knowledgelist = readcsv()
#     print(knowledgelist)
# except:
#     messagebox.show('File not found CSV file,Please save data')

global countindex
countindex = 0


def Flashcard():
    GUI2 = Toplevel()
    GUI2.title('ทบทวนความรู้')
    GUI2.geometry('500x400')

    vtext_title = StringVar()
    vtext_detail = StringVar()
    title = ttk.Label(GUI2,textvariable=vtext_title,font=('Angsana New',20,'bold'))
    title.pack()
    vtext_title.set(knowledgelist[2][0])
    detail = ttk.Label(GUI2,textvariable=vtext_detail,font=('Angsana New',16))
    detail.pack()
    vtext_detail.set(knowledgelist[3][1].replace('\r',''))


    def Prev():
        global countindex
        if countindex == 0:
            countindex = countindex
        else:
            countindex = countindex -1

        #set text
        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1].replace('\r',''))


    def next():
        global countindex
        if countindex == (len(knowledgelist)-1):
            countindex = len(knowledgelist)-1
        else:
            countindex = countindex + 1

        #set text
        print('COUNT:',countindex)
        vtext_title.set(knowledgelist[countindex][0])
        vtext_detail.set(knowledgelist[countindex][1].replace('\r',''))


    Bprev = ttk.Button(GUI2,text='<',command=Prev)
    Bprev.place(x=170,y=350)
    Bnext = ttk.Button(GUI2,text='>',command=next)
    Bnext.place(x=260,y=350)
    


    GUI2.mainloop()

notebutton = os.path.join(path,'note.png')
noteicon = PhotoImage(file=notebutton)

BFlashcard = ttk.Button(GUI,image=noteicon,command=Flashcard)
BFlashcard.place(x=450,y=20)




GUI.mainloop()