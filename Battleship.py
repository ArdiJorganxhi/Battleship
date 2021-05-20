from tkinter import*
import random
root=Tk()
root.geometry('1200x800')
frm1=Frame(root,bg="black")
frm2=Frame(root,bg="black")
frm1.place(x=50,y=100,width=500,height=500)
frm2.place(x=650,y=100,width=500,height=500)
lbl1Score=Label(root,text='0',bg='brown',fg='white',font=('Arial',30,'italic'))
lbl2Score=Label(root,text='0',bg='brown',fg='white',font=('Arial',30,'italic'))
lblWinner=Label(root,text='',bg='brown',fg='white',font=('Arial',30,'italic'))

lblWinner.place(x=350,y=620,width=500,height=60)
lbl1Score.place(x=50,y=40,width=500,height=60)
lbl2Score.place(x=650,y=40,width=500,height=60)



pl1List=[]
pl2List=[]
ListShip1=[]
ListShip2=[]
pl1Score=0
pl2Score=0



def EnableDisable(btnL1,btnL2):
  for i in range(0,25):
     if(btnL1[i].cget('bg')!='red' and btnL1[i].cget('bg')!='blue'):
        btnL1[i].config(state='normal')
     btnL2[i].config(state='disable')


def hide():
  l=[]
  for i in range(0,5):
     x=random.randint(0,24)
     while(x in l):
        x=random.randint(0,24)
     l.append(x)
  return l


def Disable(L1,L2):
  for i in range(0,25):
     L1[i].config(state='disable')
     L2[i].config(state='disable')

# Me kontrollu nese qajo
def Control(btn,index,frm):
  global pl2Score
  global pl1Score


  if(frm==frm1):
     if(index in ListShip1):
        btn.config(bg='blue')
        pl1Score=pl1Score+1
        lbl2Score.config(text=pl1Score)

     else:
        btn.config(bg='red')
     EnableDisable(pl2List,pl1List)


  if(frm==frm2):
     if(index in ListShip2):
        btn.config(bg='blue',state='disable')
        pl2Score=pl2Score+1
        lbl1Score.config(text=pl2Score)
     else:
        btn.config(bg='red')
     EnableDisable(pl1List,pl2List)


  if(pl1Score==5):
     lblWinner.config(text='Player 2 Win!')
     Disable(pl1List,pl2List)

  if(pl2Score==5):
     lblWinner.config(text='Player 1 Win!')
     Disable(pl1List,pl2List)


def btnPlacement(frm,plList):
  xpos=0
  ypos=0
  for i in range(0,25):
     plList.append(Button(frm,bg="grey",bd=8))
     plList[i].place(x=xpos,y=ypos,width=99,height=99)
     plList[i].config(command=lambda x=plList[i],y=i,z=frm:Control(x,y,z))
     xpos=xpos+100
     if(xpos==500):
        xpos=0
        ypos=ypos+100

btnPlacement(frm1,pl1List)
btnPlacement(frm2,pl2List)
ListShip1=hide()
ListShip2=hide()

mainloop()
