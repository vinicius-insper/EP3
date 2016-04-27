import tkinter as tk
from Jogo import jogo
from numpy import zeros
import tkinter.messagebox

class tabuleiro:
    
    def __init__(self):
        self.window=tk.Tk()
        self.window.title ('EP3 - Jogo da Velha')
        objeto_jogo = jogo(zeros((3,3)), 1, 0)
        self.jogo = objeto_jogo
        
        self.b1=tk.Button(self.window,width=15,height=8, command = self.callback1)
        self.b1.grid(row=0,column=0)

        self.b2=tk.Button(self.window,width=15,height=8, command = self.callback2)
        self.b2.grid(row=0,column=1)
        
        self.b3=tk.Button(self.window,width=15,height=8, command = self.callback3)
        self.b3.grid(row=0,column=2)
        
        self.b4=tk.Button(self.window,width=15,height=8, command = self.callback4)
        self.b4.grid(row=1,column=0)
        
        self.b5=tk.Button(self.window,width=15,height=8, command = self.callback5)
        self.b5.grid(row=1,column=1)
        
        self.b6=tk.Button(self.window,width=15,height=8, command = self.callback6)
        self.b6.grid(row=1,column=2)
        
        self.b7=tk.Button(self.window,width=15,height=8, command = self.callback7)
        self.b7.grid(row=2,column=0)
        
        self.b8=tk.Button(self.window,width=15,height=8, command = self.callback8)
        self.b8.grid(row=2,column=1)
        
        self.b9=tk.Button(self.window,width=15,height=8, command = self.callback9)
        self.b9.grid(row=2,column=2)

        self.proxima=tk.Label(self.window,text="Proxima jogada: X")
        self.proxima.grid(row=3, column=0)

    def comeca(self):
        self.window.mainloop()
    
    def limpa(self):
        self.b1.configure(text = "", state = "active")
        self.b2.configure(text = "", state = "active")
        self.b3.configure(text = "", state = "active")
        self.b4.configure(text = "", state = "active")
        self.b5.configure(text = "", state = "active")
        self.b6.configure(text = "", state = "active")
        self.b7.configure(text = "", state = "active")
        self.b8.configure(text = "", state = "active")
        self.b9.configure(text = "", state = "active")

        
        
    def callback1(self):
        if self.jogo.turno == 1:
            self.b1.configure(text = "X")
        else:
            self.b1.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(0,0)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa() 
        else:
            self.b1.configure(state="disabled")
    
    def callback2(self):
        if self.jogo.turno == 1:
            self.b2.configure(text = "X")
        else:
            self.b2.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(0,1)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa()  
        else:
            self.b2.configure(state="disabled")
        
    def callback3(self):
        if self.jogo.turno == 1:
            self.b3.configure(text = "X")
        else:
            self.b3.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(0,2)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa()
        else:
            self.b3.configure(state="disabled") 
        
    def callback4(self):
        if self.jogo.turno == 1:
            self.b4.configure(text = "X")
        else:
            self.b4.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(1,0)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa() 
        else:
            self.b4.configure(state="disabled")
            
    def callback5(self):
        if self.jogo.turno == 1:
            self.b5.configure(text = "X")
        else:
            self.b5.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(1,1)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa() 
        else:
            self.b5.configure(state="disabled")
            
    def callback6(self):
        if self.jogo.turno == 1:
            self.b6.configure(text = "X")
        else:
            self.b6.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(1,2)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa() 
        else:
            self.b6.configure(state="disabled")
        
    def callback7(self):
        if self.jogo.turno == 1:
            self.b7.configure(text = "X")
        else:
            self.b7.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(2,0)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa()
        else:
            self.b7.configure(state="disabled")
            
    def callback8(self):
        if self.jogo.turno == 1:
            self.b8.configure(text = "X")
        else:
            self.b8.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(2,1)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa()  
        else:
            self.b8.configure(state="disabled")
        
    def callback9(self):
        if self.jogo.turno == 1:
            self.b9.configure(text = "X")
        else:
            self.b9.configure(text = "O")
        if self.jogo.rodada % 2 == 1:
            self.proxima.configure(text = "Proxima jogada: X")
        else:
            self.proxima.configure(text = "Proxima jogada: O")
        self.jogo.recebe_jogada(2,2)
        x = self.jogo.verifica_ganhador()
        if x == 2:
            tkinter.messagebox.showinfo("Jogo da Velha", "X ganhou")
        elif x == 1:
            tkinter.messagebox.showinfo("Jogo da Velha", "O ganhou")
        elif x == 0:
            tkinter.messagebox.showinfo("Jogo da Velha", "Empate")
        if x == 2 or x == 1 or x == 0:
            self.jogo.limpa_jogadas()
            self.limpa()   
        else:
            self.b9.configure(state="disabled")


rt=tabuleiro()
rt.comeca()
