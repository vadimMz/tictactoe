# -*- coding: utf-8 -*-
"""
Created on Thu May 10 19:55:51 2018

@author: VadimMz
"""

from tkinter import *

def Quit(event):
    global root
    root.destroy()

  
root = Tk()
root.title('Tic Tac Toe')
root.geometry("180x250")
root.CurrentTurn = True
root.NumberOfTurns = 0
root.ListOfX = []
root.ListOfO = []
Combination
WinCombinations = ((11,12,13),(21,22,23),(31,32,33),(11,22,33),(13,22,31))

def GetCombination(Comb):
    global Combination
    Combination = Comb   

class MyButton(Button):
    def MakeTurn(self, *args):
        if self["text"] == "" and (root.CurrentTurn):
            root.CurrentTurn = False
            root.NumberOfTurns += 1
            root.ListOfX.append(Combination)
            print(root.ListOfX)
            return self.config(text = "X")
        elif self["text"] == "" and (root.CurrentTurn == False):
            root.CurrentTurn = True
            root.NumberOfTurns += 1
            root.ListOfO.append(Combination)
            print(root.ListOfO)
            return self.config(text = "O")

    
btn11 = MyButton(root, text = '', command = lambda: GetCombination(11))
btn11.place(x = 0, y = 0, width = 60, height = 60)
btn12 = MyButton(root, text = '', command = lambda: GetCombination(12))
btn12.place(x = 60, y = 0, width = 60, height = 60)
btn13 = MyButton(root, text = '', command = lambda: GetCombination(13))
btn13.place(x = 120, y = 0, width = 60, height = 60)
btn21 = MyButton(root, text = '', command = lambda: GetCombination(21))
btn21.place(x = 0, y = 60, width = 60, height = 60)
btn22 = MyButton(root, text = '', command = lambda: GetCombination(22))
btn22.place(x = 60, y = 60, width = 60, height = 60)
btn23 = MyButton(root, text = '', command = lambda: GetCombination(23))
btn23.place(x = 120, y = 60, width = 60, height = 60)
btn31 = MyButton(root, text = '', command = lambda: GetCombination(31))
btn31.place(x = 0, y = 120, width = 60, height = 60)
btn32 = MyButton(root, text = '', command = lambda: GetCombination(32))
btn32.place(x = 60, y = 120, width = 60, height = 60)
btn33 = MyButton(root, text = '', command = lambda: GetCombination(33))

btn33.place(x = 120, y = 120, width = 60, height = 60)
btnQuit = MyButton(root, text = 'Quit')
btnQuit.place(x = 0, y = 180, width = 120, height = 30)

TictacDict = {'11': btn11, '12': btn12, '13': btn13,
           '21': btn21, '22': btn22, '23': btn23,
           '31': btn31, '32': btn32, '33': btn33 }

btnQuit.bind("<Button-1>", Quit)
btn11.bind("<Button-1>", btn11.MakeTurn)
btn12.bind("<Button-1>", btn12.MakeTurn)
btn13.bind("<Button-1>", btn13.MakeTurn)    
btn21.bind("<Button-1>", btn21.MakeTurn)    
btn22.bind("<Button-1>", btn22.MakeTurn)    
btn23.bind("<Button-1>", btn23.MakeTurn)    
btn31.bind("<Button-1>", btn31.MakeTurn)    
btn32.bind("<Button-1>", btn32.MakeTurn)    
btn33.bind("<Button-1>", btn33.MakeTurn)         

        
     




root.mainloop()