from numpy import zeros
class jogo():

	def __init__(self, matrizzeros, turno, rodada):
		self.matriz = matrizzeros
		self.turno = turno
		self.rodada = rodada

	def recebe_jogada(self, linha, coluna):
		if self.turno == 1:
			self.matriz[linha][coluna] = 1
			self.turno = 2
			self.rodada += 1
		elif self.turno == 2:
			self.matriz[linha][coluna] = 5
			self.turno = 1
			self.rodada += 1