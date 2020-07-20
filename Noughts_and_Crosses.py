import pygame
import math

WIDTH = 600
RECT_WIDTH = 200
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Noughts and Crosses")

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)
GREEN = (0,255,0)
RED = (255,0,0)

BOARD = [[0,0,0],[0,0,0],[0,0,0]]

def check_win(val):
	for row in BOARD:
		for tile in row:
			if tile == val:
				continue
			else: 
				break
		else:
			return True
	
	for col in range(3):
		for row in BOARD:
			if row[col] == val:
				continue
			else:
				break
		else:
			return True

	for tile in range(3):
		if BOARD[tile][2-tile] == val:
			continue
		else:
			break
	else:
		return True

def main():
	
	first = pygame.draw.rect(WIN, WHITE, (0,0,RECT_WIDTH,RECT_WIDTH))
	second = pygame.draw.rect(WIN, WHITE, (200,0,RECT_WIDTH,RECT_WIDTH))
	third = pygame.draw.rect(WIN, WHITE, (400,0,RECT_WIDTH,RECT_WIDTH))
	fourth = pygame.draw.rect(WIN, WHITE, (0,200,RECT_WIDTH,RECT_WIDTH))
	fifth = pygame.draw.rect(WIN, WHITE, (200,200,RECT_WIDTH,RECT_WIDTH))
	sixth = pygame.draw.rect(WIN, WHITE, (400,200,RECT_WIDTH,RECT_WIDTH))
	seventh = pygame.draw.rect(WIN, WHITE, (0,400,RECT_WIDTH,RECT_WIDTH))
	eigth = pygame.draw.rect(WIN, WHITE, (200,400,RECT_WIDTH,RECT_WIDTH))
	ninth = pygame.draw.rect(WIN, WHITE, (400,400,RECT_WIDTH,RECT_WIDTH))

	pygame.draw.line(WIN, GREY,(200,0),(200,600),10)
	pygame.draw.line(WIN, GREY,(400,0),(400,600),10)
	pygame.draw.line(WIN, GREY,(0,200),(600,200),10)
	pygame.draw.line(WIN, GREY,(0,400),(600,400),10)

	running = True
	xturn = True
	winner = False

	first_open = True
	second_open = True
	third_open = True
	fourth_open = True
	fifth_open = True
	sixth_open = True
	seventh_open = True
	eigth_open = True
	ninth_open = True
	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if winner != True:
					if first.collidepoint(pos) and first_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (20,20), (180,180), 10)
							pygame.draw.line(WIN, BLACK, (180,20), (20,180), 10)
							xturn = False
							BOARD[0][0] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(100,100), 80, 10)
							xturn = True
							BOARD[0][0] = 2
						first_open = False

					if second.collidepoint(pos) and second_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (220,20), (380,180), 10)
							pygame.draw.line(WIN, BLACK, (220,180), (380,20), 10)
							xturn = False
							BOARD[0][1] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(300,100), 80, 10)
							xturn = True
							BOARD[0][1] = 2
						second_open = False

					if third.collidepoint(pos) and third_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (420,20), (580,180), 10)
							pygame.draw.line(WIN, BLACK, (420,180), (580,20), 10)
							xturn = False
							BOARD[0][2] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(500,100), 80, 10)
							xturn = True
							BOARD[0][2] = 2
						third_open = False
					
					if fourth.collidepoint(pos) and fourth_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (20,220), (180,380), 10)
							pygame.draw.line(WIN, BLACK, (20,380), (180,220), 10)
							xturn = False
							BOARD[1][0] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(100,300), 80, 10)
							xturn = True
							BOARD[1][0] = 2
						fourth_open = False

					if fifth.collidepoint(pos) and fifth_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (220,220), (380,380), 10)
							pygame.draw.line(WIN, BLACK, (380,220), (220,380), 10)
							xturn = False
							BOARD[1][1] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(300,300), 80, 10)
							xturn = True
							BOARD[1][1] = 2
						fifth_open = False

					if sixth.collidepoint(pos) and sixth_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (420,220), (580,380), 10)
							pygame.draw.line(WIN, BLACK, (420,380), (580,220), 10)
							xturn = False
							BOARD[1][2] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(500,300), 80, 10)
							xturn = True
							BOARD[1][2] = 2
						sixth_open = False

					if seventh.collidepoint(pos) and seventh_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (20,420), (180,580), 10)
							pygame.draw.line(WIN, BLACK, (20,580), (180,420), 10)
							xturn = False
							BOARD[2][0] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(100,500), 80, 10)
							xturn = True
							BOARD[2][0] = 2
						seventh_open = False

					if eigth.collidepoint(pos) and eigth_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (220,420), (380,580), 10)
							pygame.draw.line(WIN, BLACK, (220,580), (380,420), 10)
							xturn = False
							BOARD[2][1] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(300,500), 80, 10)
							xturn = True
							BOARD[2][1] = 2
						eigth_open = False

					if ninth.collidepoint(pos) and ninth_open:
						if xturn:
							pygame.draw.line(WIN, BLACK, (420,420), (580,580), 10)
							pygame.draw.line(WIN, BLACK, (420,580), (580,420), 10)
							xturn = False
							BOARD[2][2] = 1
						else:
							pygame.draw.circle(WIN,BLACK,(500,500), 80, 10)
							xturn = True
							BOARD[2][2] = 2
						ninth_open = False
		if check_win(1):
			winner = True
		if check_win(2):
			winner = True
	
		pygame.display.update()
	pygame.quit()

main()