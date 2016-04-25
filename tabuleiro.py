import tkinter as tk

class tabuleiro:

	def __init__(self):
		self.window=tk.Tk()
		self.window.title ('EP3 - Jogo da Velha')

		b1=tk.Button(self.window,width=15,height=8)
		b1.grid(row=0,column=0)

		b2=tk.Button(self.window,width=15,height=8)
		b2.grid(row=0,column=1)

		b3=tk.Button(self.window,width=15,height=8)
		b3.grid(row=0,column=2)

		b4=tk.Button(self.window,width=15,height=8)
		b4.grid(row=1,column=0)

		b5=tk.Button(self.window,width=15,height=8)
		b5.grid(row=1,column=1)

		b6=tk.Button(self.window,width=15,height=8)
		b6.grid(row=1,column=2)

		b7=tk.Button(self.window,width=15,height=8)
		b7.grid(row=2,column=0)

		b8=tk.Button(self.window,width=15,height=8)
		b8.grid(row=2,column=1)

		b9=tk.Button(self.window,width=15,height=8)
		b9.grid(row=2,column=2)

		proxima=tk.Label(self.window,text="Proxima jogada: ")

	def comeca(self):
		self.window.mainloop()


	rt=tabuleiro()
	rt.comeca()

