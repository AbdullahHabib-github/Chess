import pygame

from data.classes.Board import Board


def draw(display):
	display.fill('white')
	board.draw(display)
	pygame.display.set_caption('Chess')
	pygame.display.update()



pygame.init()


WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])


if __name__ == '__main__':
	pl1 = input("Enter the name of player 1")
	pl2 = input("Enter the name of plater 2")
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN: 
				if event.button == 1:
					mx, my = pygame.mouse.get_pos()
					#print(mx,my)
					board.handle_click(mx, my)
		if board.is_in_checkmate('black'): 
			print('{} wins!'.format(pl1))
			running = False
		elif board.is_in_checkmate('white'):
			print('{} wins!'.format(pl2))
			running = False
			
		# Draw the board
		draw(screen)