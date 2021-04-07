from tkinter import *
from tkinter import messagebox as mb
import json

root= Tk()
#root.geometry('1050*800')
root.title("QUIZ")
root.configure(bg='light blue')


with open("quiz.json")as j:
    son=json.load(j)
question=(son["question"])
option=(son["option"])
answer=(son["answer"])
print(question)
print(option)
print(answer)

class Quiz:
    def __init__(self):
        self.qn=0
        self.opt_select=IntVar()
        #self.option=self.radioButton()
        self.question=self.question(self.qn)
        self.displayOption(self.qn)
        self.buttons()
        self.correct=0


def question(self,qn):
    t=label(root,text="QUIZ",width=60,bg="black",fg="white",font=("joker",28,"bold"))
    t.place("ceter")
    qn=label(root,text=q[qn],width=70,anchor="w")
    qn.place(x=50,y=50)
    return qn

def radioButton(self):
    val=0
    b=[]
    yp=150
    while val<4:
        button=RadioButton(root,text="",variable=self.opt_select,value=val+1,font=("arial",14))
        b.append(button)
        button.place(x=100,y=yp)
        val+=1
        yp+=40
    return b

def displayOption(self,qn):
    val=0
    self.opt_select.set(0)
    self.question["text"]=q[qn]
    for op in option[qn]:
        self.option[val]["text"]=op
        val+=1
def buttons(self):
    nextButton=Button(root,text="NEXT",width=10,bg="blue",fg="white",font=("times",16,"bold"))
    nextButton.place(x=180,y=380)
    skipButton=button(root,text="SKIP",width=10,bg="red",fg="white",font=("times",16,"bold"))
    skipButton.place(x=280,y=380)
    quitButton=Button(root,text="QUIT",command=root.desrtroy,width=10,bg="blue",fg="white",font=("times",16,"bold"))
    quitButton.place(x=380,y=380)

def chekAnswer(self,qn):
    if self.chekAnswer(self.qn):
        return True

def next_btn(self):
    if self.chekAnswer(self.qn):
        self.correct+=1
    self.qn+=1
    if self.qn==len(q):
        self.displayResult()
    else:
        self.displayOption(self.qn)

def displayResult(self):
    score=int(self.correct/len(q)*100)
    result="SCORE : "+ str(score)+"%"
    wa=len(q)-self.correct
    correct="no. of correct answers : " +str(self.correct)
    wrong="no. of wrong answers : " +str(wc)
    mb.showResult("Result","\n".join([result,correct,wrong]))


quiz=Quiz()
root.mainloop()


