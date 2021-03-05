from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Hello Chess")

def reset():
  pass



def btnClick(rowX, colY):
  def whichButtonClicked():
    processClick (rowX,colY)
  return whichButtonClicked


def processClick(rowX,colY):
  print(rowX, colY)
  


def drawBoard():
  label = Label(tk, text="White To Play:", font='Times 10 bold', bg='white', fg='black', height=1, width=20)
  label.grid(row=1, column=0)
  resetBtn = Button(tk, text="Reset Game", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=reset)
  resetBtn.grid(row=1, column=2)   
  for i in range(2,10):
    for j in range(8):
      if (i+j)%2!=0:
        bgcolor='#824023'
      else:
        bgcolor='#f5bea6'
      button = Button(tk, text=" ", font='Times 20 bold', bg=bgcolor, fg='white', height=4, width=8, command=btnClick(i-2,j-1))
      button.grid(row=i, column=j)

drawBoard()
tk.mainloop()


