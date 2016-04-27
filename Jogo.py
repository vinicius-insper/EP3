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

	def verifica_ganhador(self):
		a = self.matriz[0][0] + self.matriz[0][1] + self.matriz[0][2]
		b = self.matriz[1][0] + self.matriz[1][1] + self.matriz[1][2]
		c = self.matriz[2][0] + self.matriz[2][1] + self.matriz[2][2]
		d = self.matriz[0][0] + self.matriz[1][0] + self.matriz[2][0]
		e = self.matriz[0][1] + self.matriz[1][1] + self.matriz[2][1]
		f = self.matriz[0][2] + self.matriz[1][2] + self.matriz[2][2]
		g = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
		h = self.matriz[2][0] + self.matriz[1][1] + self.matriz[0][2]

		if a == 3 or b == 3 or c == 3 or d == 3 or e == 3 or f == 3 or g == 3 or h == 3:
			return 2
		elif a == 15 or b == 15 or c == 15 or d == 15 or e == 15 or f == 15 or g == 15 or h == 15:
			return 1
		elif self.rodada == 9:
			return 0
		else:
			return -1

	def limpa_jogadas(self):
		self.matriz = zeros((3,3))
		self.rodada = 0
