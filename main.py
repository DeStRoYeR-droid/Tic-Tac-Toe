'''
Tic Tac Toe with GUI
Author - DeStRoYeR-droid
'''

import pygame 
import sys


#Global Variables
S_WIDTH = 720
S_HEIGHT = 720
LINE_WIDTH = 20

#Constant colors
BGCOLOR = (12 , 33 , 69)
LINE_COLOR = (12 , 32 , 49)
COLOR_X = (210 , 246 , 252)
COLOR_O = (0 , 120 , 212)
WHITE = (255 , 255 , 255)
TEXT_COLOR = (0 , 140 , 139 )

#Initialising pygame
pygame.init()

#Making Screen
SCREEN = pygame.display.set_mode((S_WIDTH , S_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
SCREEN.fill(BGCOLOR)
ICON = pygame.image.load('icon.jpeg')
pygame.display.set_icon(ICON)

#Drawing the base lines
def drawLines():
	pygame.draw.line(SCREEN , LINE_COLOR , (240 , 0) , (240 , S_WIDTH) , LINE_WIDTH)
	pygame.draw.line(SCREEN , LINE_COLOR , (480 , 0) , (480 , S_WIDTH) , LINE_WIDTH)
	pygame.draw.line(SCREEN , LINE_COLOR , (0 , 240) , (S_HEIGHT , 240) , LINE_WIDTH)
	pygame.draw.line(SCREEN , LINE_COLOR , (0 , 480) , (S_HEIGHT , 480) , LINE_WIDTH)
drawLines()
pygame.display.update()

def Update_Board(x : int , y : int , Board : list):
	global Turns
	Valid = ['O' ,'X']
	if valid_enter(x , y , Board) and not(isWon(Board)):
		Board[y][x] = Valid[Turns % 2]
		Turns += 1

def winner(Board):
	'''
	Takes in parameter board
	:if the board is winning for a player
	:returns the sign (X or O) used by player
	'''
	if Board[0][0] == Board[0][1] == Board[0][2] and Board[0][0].isalpha():
		return Board[0][0]

	if Board[0][0] == Board[1][1] == Board[2][2] and Board[0][0].isalpha():
		return Board[0][0]

	if Board[0][0] == Board[1][0] == Board[2][0] and Board[0][0].isalpha():
		return Board[0][0]

	if Board[1][0] == Board[1][1] == Board[1][2] and Board[1][0].isalpha():
		return Board[1][0]

	if Board[2][0] == Board[2][1] == Board[2][2] and Board[2][0].isalpha():
		return Board[1][0]

	if Board[2][0] == Board[1][1] == Board[0][2] and Board[2][0].isalpha():
		return Board[2][0]

	if Board[0][1] == Board[1][1] == Board[2][1] and Board[0][1].isalpha():
		return Board[0][1]

	if Board[0][2] == Board[1][2] == Board[2][2] and Board[0][2].isalpha():
		return Board[0][2]


def isWon(Board : list):
	if Board[0][0] == Board[0][1] == Board[0][2] and Board[0][0].isalpha():
		return True

	if Board[0][0] == Board[1][1] == Board[2][2] and Board[0][0].isalpha():
		return True

	if Board[0][0] == Board[1][0] == Board[2][0] and Board[0][0].isalpha():
		return True

	if Board[1][0] == Board[1][1] == Board[1][2] and Board[1][0].isalpha():
		return True

	if Board[2][0] == Board[2][1] == Board[2][2] and Board[2][0].isalpha():
		return True

	if Board[2][0] == Board[1][1] == Board[0][2] and Board[2][0].isalpha():
		return True

	if Board[0][1] == Board[1][1] == Board[2][1] and Board[0][1].isalpha():
		return True

	if Board[0][2] == Board[1][2] == Board[2][2] and Board[0][2].isalpha():
		return True

def Wincase(Board : list):
	if Board[0][0] == Board[0][1] == Board[0][2] and Board[0][0].isalpha():
		pygame.draw.line(SCREEN , WHITE , (0 , 120) , (720 , 120) , 10)

	if Board[0][0] == Board[1][1] == Board[2][2] and Board[0][0].isalpha():
		pygame.draw.line(SCREEN , WHITE , (0 , 0) , (720 , 720) , 10)

	if Board[0][0] == Board[1][0] == Board[2][0] and Board[0][0].isalpha():
		pygame.draw.line(SCREEN , WHITE , (120 , 0) , (120 , 720) , 10)

	if Board[1][0] == Board[1][1] == Board[1][2] and Board[1][0].isalpha():
		pygame.draw.line(SCREEN , WHITE , (0 , 360) , (720 , 360) , 10)

	if Board[2][0] == Board[2][1] == Board[2][2] and Board[2][0].isalpha():
		pygame.draw.line(SCREEN , WHITE , (0 , 600) , (720 , 600) , 10)

	if Board[2][0] == Board[1][1] == Board[0][2] and Board[2][0].isalpha():
		pygame.draw.line(SCREEN , WHITE , (0 , 720) , (720 , 0) , 10)

	if Board[0][1] == Board[1][1] == Board[2][1] and Board[0][1].isalpha():
		pygame.draw.line(SCREEN , WHITE , (360 , 0) , (360 , 720) , 10)

	if Board[0][2] == Board[1][2] == Board[2][2] and Board[0][2].isalpha():
		pygame.draw.line(SCREEN , WHITE , (600 , 0) , (600 , 720) , 10)

def valid_enter(x, y , Board):
	if Board[y][x].isspace():
		return True 
	else:
		return False

def clear(Board : list):
	New_Board = [[' ' , ' ' , ' '] , [' ' , ' ' , ' '] , [' ' , ' ' , ' ']]
	return New_Board

Board = [[' ' , ' ' , ' '] , [' ' , ' ' , ' '] , [' ' , ' ' , ' ']]
Turns = 0

CLOSED = False
while not(CLOSED):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			CLOSED = True 

		if event.type == pygame.MOUSEBUTTONDOWN:
			x , y = pygame.mouse.get_pos()
			x , y = x//240 , y//240
			Update_Board(x , y , Board)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				print ('Reset board')
				Board = clear(Board)
				Turns = 0

		D_Board = Board


		for i in range(3):
			for j in range(3):
				if D_Board[i][j] == 'O':
					pygame.draw.circle(SCREEN , COLOR_O , ((240*j + 120) , (240*i + 120)) , 100 , 12)
				elif D_Board[i][j] == 'X':
					pygame.draw.line(SCREEN , COLOR_X , ((240*j + 35) , (240*i + 35)) , ((240*j + 215) , (240*i + 215)) , 10)
					pygame.draw.line(SCREEN , COLOR_X , ((240*j + 35) , (240*i + 215)) , ((240*j + 215) , (240*i + 35)) , 10)
				else:
					pygame.draw.rect(SCREEN , BGCOLOR , (240 * j , 240 * i , 240 , 240))
					drawLines()

		if isWon(Board):
			Wincase(Board)
			pygame.font.init()
			FONT = pygame.font.SysFont('comicsans' , 120)

			WinText = FONT.render(winner(Board)+' is the winner' , 1 , TEXT_COLOR)
			SCREEN.blit(WinText , (75 , 320))


		pygame.display.update()

pygame.quit()
sys.exit()