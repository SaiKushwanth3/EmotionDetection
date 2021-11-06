import tkinter
from tkinter import *
import matplotlib.pyplot as plt
from using_naive_bayes.py import *
base = Tk()
base.title("Emotion Detection")
base.geometry("600x500")
base.resizable(width=False, height=False)

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    if msg != '':
        msg=msg.lower()
        msg_data = cleaning(msg)
        in_text = []
        in_text.append(msg_data)
        text_area.config(state=NORMAL)
        output=callmodel1(in_text)
        emotion = output[0]
        statement=output[2]
        maxim = output[1]
        text_area.insert(END, "EMOTION" + emotion[0] + '\t\t'+"strength:"+ maxim+'\n\n')
        x = list(statement.keys())
        y = list(statement.values())
        plt.figure(figsize=(30,20))
        plt.bar(x,y,width=0.7,color="#0BE7CA")
        plt.show()
        text_area.config(foreground="#442265", font=("Verdana", 12 ))
        text_area.config(state=DISABLED)
        text_area.yview(END)
def clean():
    EntryBox.delete('1.0', END)

#create window
text_area = Text(base, bd=1, bg="#F4D03F", font="Serif",)
EntryBox = Text(base, bd=1, bg="white", font="Serif", fg="#2E4053")
EntryBox.insert(END, "Text Your FeedBack Here")
senbutton=Button(base,font=("verdana", 12,'bold'),text="Analyze",bd=0, bg="#E67E22"
                 , activebackground="#F39C12", fg='white',command=send)
w = Label(base, text="\t\tText your Feedback Here\t\t")
text_area.place(x=6,y=10, height=202, width=580)
w.place(x=145,y=210)
EntryBox.place(x=6,y=232, height=200,width=580)
senbutton.place(x=250,y=435, height=50, width=100)
clean()
base.mainloop()
