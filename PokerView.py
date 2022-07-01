import pygame
import os,sys
import PokerModel
import cardcode

HEIGHT = 720    #game canvas height
WIDTH = 1280    #game canvas width

#Global constants here
BLACK = (255,255,255)
BLACK = (0,0,0)        #real number is 0,0,0
GREY  = (50,50,50)
RED  = (207,0,0)

class Control:
	def __init__(self):
		deck = PokerModel.Deck()
		self.images = {}
		self.scale = .5
		self.cardSize = (WIDTH / 7, WIDTH / 5)
		self.buffer = 50
		self.background = pygame.image.load('img/background.jpg').convert_alpha()
		self.cardBack = pygame.image.load('img/back.png').convert_alpha()
		self.cardBack = pygame.transform.scale(self.cardBack,(int(self.scale * self.cardSize[0]), int(self.scale * self.cardSize[1])))

		cc=cardcode.cardcode(3)

		font = pygame.font.Font('font/CoffeeTin.ttf', 50)
		loadText = font.render("Loading...", 1, BLACK)
		loadSize = font.size("Loading...")
		loadLoc = (WIDTH/2 - loadSize[0]/2, HEIGHT/2 - loadSize[1]/2)

		self.scores = [0,0,0,0]

		SCREEN.blit(self.background, (-320,-100))

		SCREEN.blit(loadText, loadLoc)

		pygame.display.flip()

		for card in deck:
			print(cc.imagePath(card))
			self.images[card] = pygame.image.load(cc.imagePath(card)).convert_alpha()
			self.images[card] = pygame.transform.scale(self.images[card], (int(self.scale * self.cardSize[0]), int(self.scale * self.cardSize[1])))

		self.start_up_init()

	def start_up_init(self):
		#intitialize items for the startup section of the game
		self.poker = PokerModel.Poker(self.scores)

		self.font = pygame.font.Font('font/CoffeeTin.ttf',150)
		self.font2 = pygame.font.Font('font/IndianPoker.ttf', 75)
		self.font2.set_bold(True)

		self.startText = self.font2.render("Welcome to Poker!", 1, BLACK)
		self.startSize = self.font2.size("Welcome to Poker!")
		self.startLoc = (WIDTH/2 - self.startSize[0]/2, self.buffer)

		self.startButton = self.font.render(" Start ", 1, BLACK)
		self.buttonSize =self.font.size(" Start ")
        #button Start Location
		self.buttonLoc = (WIDTH/2 - self.buttonSize[0]/2, HEIGHT/2 - self.buttonSize[1]/2)

		self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
		self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

		self.state = 0

	def main(self):
		if self.state == 0:
			self.start_up()
		elif self.state == 1:
			self.play()
		elif self.state == 2:
			self.results()
		elif self.state == 3:
			self.new_game()

	def start_up(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()

			#when the user clicks the start button, change to the playing state
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouseRect = pygame.Rect(event.pos, (1,1))
					if mouseRect.colliderect(self.buttonRect):
						self.state += 1
						self.play_init()
						return

		#draw background
		SCREEN.blit(self.background, (-320,-100))

		#draw welcome text
		SCREEN.blit(self.startText, self.startLoc)

		#draw the start button
		pygame.draw.rect(SCREEN, RED, self.buttonRect)
		pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
		SCREEN.blit(self.startButton, self.buttonLoc)

		pygame.display.flip()

	def play_init(self):
		#create the new variables
		self.cardLoc = {}
		self.round = 0

		#setup the locations for each card in the hand
		x = 4.5 * int(self.scale * self.cardSize[0])
		#self.youLoc = (x - 150, self.buffer)    #yaccDL switch hand and AI up and down
		self.youLoc = (x - 150, HEIGHT - self.scale * self.cardSize[1] - self.buffer)    #yaccDL switch hand and AI up and down

		for index in range(len(self.poker.playerHand)):
			#self.cardLoc[index] = (x, self.buffer)        #yaccDL switch hand and AI up and down
			self.cardLoc[index] = (x, HEIGHT - self.scale * self.cardSize[1] - self.buffer)        #yaccDL switch hand and AI up and down
			x += int(self. scale * self.cardSize[0])/6    #yaccDL overlap cards

		#setup the text that will be printed to the screen
		self.font = pygame.font.Font('font/IndianPoker.ttf', 25)
		self.font.set_bold(True)
		self.font2 = pygame.font.Font('font/CoffeeTin.ttf', 60)
		self.youText = self.font.render("Your Hand", 1, BLACK)
		self.youSize = self.font.size("Your Hand")

		self.youLoc = (self.cardLoc[0][0],self.cardLoc[0][1] - 30)#(self.youLoc[0], self.buffer + self.scale * self.cardSize[1]/2 - self.youSize[1]/2)

		self.replaceButton = self.font2.render(" Replace ", 1, BLACK)
		self.buttonSize =self.font2.size(" Replace ")

		#yaccDL set replace button one card right
		#self.buttonLoc = (x + self.scale * self.cardSize[0] + 30, self.buffer + self.scale * self.cardSize[1]/2 - self.buttonSize[1]/2)
		#yaccDL put the replace button downside // Replace button location
		#self.buttonLoc = (x + self.scale * self.cardSize[0] + 30, HEIGHT - self.buffer - self.scale * self.cardSize[1]/2 + self.buttonSize[1]/2)
		#yaccDL put the replace button rightside
		self.buttonLoc = (WIDTH - self.buffer-self.buttonSize[0], HEIGHT - self.buffer - self.scale * self.cardSize[1]/2 + self.buttonSize[1]/2)

		self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
		self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

	def play(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()

			#when the user clicks on a card, change its color to signify a selection has occurred
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					#create a rectangle for the mouse click and for each card.  check for intersection
					mouseRect = pygame.Rect(event.pos, (1,1))
					#this minus thirty fixes a minor bug, do not remove
					#yaccDL make it reversed to adopt to verlaped card
					for index in reversed(range(len(self.poker.playerHand))):	
						cardRect = pygame.Rect(self.cardLoc[index], (int(self.scale * self.cardSize[0]), int(self.scale * self.cardSize[1])))
						if cardRect.colliderect(mouseRect):
							#self.poker.playerHand[index].selected = not self.poker.playerHand[index].selected
							#yaccDL mirro selected to x000 bit
							if self.poker.playerHand[index]//1000 >3:
								self.poker.playerHand[index] -= 4000
							else:
								self.poker.playerHand[index] += 4000
							break

					#check if we clicked the replaceButton
					if mouseRect.colliderect(self.buttonRect):
						self.poker.replace(self.poker.playerHand)
						self.poker.computerReplace()
						self.round += 1
						if self.round == 2:
							self.state += 1
							self.results_init()
							return

		#display background	
		SCREEN.blit(self.background, (-320,-100))

		#display the player's hand
		for index in range(len(self.poker.playerHand)):
			#if not self.poker.playerHand[index].selected:
			#yaccDL mirro selected to x000 bit
			if self.poker.playerHand[index]//1000 <4:
				SCREEN.blit(self.images[self.poker.playerHand[index]], self.cardLoc[index])    #yaccDL switch hand and AI up and down 
			else:
				#make the card a little big higher to signify the chosed card
				#SCREEN.blit(self.cardBack, (self.cardLoc[index][0],self.cardLoc[index][1]-10))
				#and do not backside the card, only move the card when chosed                       #yaccDL switch hand and AI up and down
				SCREEN.blit(self.images[self.poker.playerHand[index] - 4000], (self.cardLoc[index][0],self.cardLoc[index][1]-10))

		#display the text
		SCREEN.blit(self.youText, self.youLoc)
		pygame.draw.rect(SCREEN, RED, self.buttonRect)
		pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
		SCREEN.blit(self.replaceButton, self.buttonLoc)

		#display the scoreboard
		self.display_scoreboard()

		pygame.display.flip()

	def results_init(self):
		#initialize variables for the button
		# self.font = pygame.font.Font('font/IndianPoker.ttf', 25)
		self.replaceButton = self.font2.render(" New Game ", 1, BLACK)
		self.buttonSize =self.font2.size(" New Game ")

		#self.buttonLoc = (self.buttonLoc[0], self.buffer + self.scale * self.cardSize[1]/2 - self.buttonSize[1]/2)
		#yaccDL put the replace button downside // New Game button location
		#self.buttonLoc = (self.buttonLoc[0], HEIGHT - self.buffer - self.scale * self.cardSize[1]/2 + self.buttonSize[1]/2)
		#yaccDL put the replace button rightside
		self.buttonLoc = (WIDTH - self.buffer-self.buttonSize[0], HEIGHT - self.buffer - self.scale * self.cardSize[1]/2 + self.buttonSize[1]/2)

		self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
		self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

		#initialize variables for drawing the hands
		self.comp1Loc = (WIDTH - int(5 * self.scale * self.cardSize[0]) - self.buffer, HEIGHT / 2 - self.scale * self.cardSize[1]/2)    #123-312
		#yaccDL switch hand and AI up and down
		#self.comp2Loc = ( 4.5 * int(self.scale * self.cardSize[0]), HEIGHT - self.scale * self.cardSize[1] - self.buffer)
		self.comp2Loc = ( 4.5 * int(self.scale * self.cardSize[0]), self.buffer)    #123-312
		self.comp3Loc = (self.buffer, HEIGHT / 2 - self.scale * self.cardSize[1]/2)    #123-312

		self.result = self.poker.play_round()

		#initialize variables for labeling the hands
		playerScore = "You:" + self.poker.convert_score(self.result[0])
		self.youText = self.font.render(playerScore, 1, BLACK)
		self.youSize = self.font.size(playerScore)
		self.youLoc = (self.cardLoc[0][0],self.cardLoc[0][1] - 30)    #yaccDL switch hand and AI up and down

		comp1Score = "C1:" + self.poker.convert_score(self.result[1])
		self.comp1Label = self.font.render(comp1Score, 1, BLACK)
		self.comp1LabelSize = self.font.size(comp1Score)
		self.comp1LabelLoc = (self.comp1Loc[0], self.comp1Loc[1] - 30)

		comp2Score = "C2:" + self.poker.convert_score(self.result[2])
		self.comp2Label = self.font.render(comp2Score, 1, BLACK)
		self.comp2LabelSize = self.font.size(comp2Score)
		self.comp2LabelLoc = (self.comp2Loc[0], self.comp2Loc[1] - 30)    #yaccDL switch hand and AI up and down

		comp3Score = "C3:" + self.poker.convert_score(self.result[3])
		self.comp3Label = self.font.render(comp3Score, 1, BLACK)
		self.comp3LabelSize = self.font.size(comp3Score)
		self.comp3LabelLoc = (self.comp3Loc[0], self.comp3Loc[1] - 30)

	def results(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();sys.exit()

			#when the user clicks the start button, change to the playing state
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouseRect = pygame.Rect(event.pos, (1,1))
					if mouseRect.colliderect(self.buttonRect):
						# self.start_up_init()
						self.state = 1
						self.play_init()
						self.poker = PokerModel.Poker(self.scores)
						return

		#display background
		SCREEN.blit(self.background, (-320,-100))

		#print player hand in the top
		self.display_hand(self.poker.playerHand, self.cardLoc[0][0], self.cardLoc[0][1])

		#print computer 1 on the right
		self.display_hand(self.poker.comp1Hand,self.comp1Loc[0], self.comp1Loc[1])

		#print computer 2 on the bottom
		self.display_hand(self.poker.comp2Hand, self.comp2Loc[0], self.comp2Loc[1])

		#print computer 3 on the left
		self.display_hand(self.poker.comp3Hand, self.comp3Loc[0], self.comp3Loc[1])

		#print labels saing what each hand was
		SCREEN.blit(self.youText, self.youLoc)             
		SCREEN.blit(self.comp1Label, self.comp1LabelLoc)   
		SCREEN.blit(self.comp2Label, self.comp2LabelLoc)   
		SCREEN.blit(self.comp3Label, self.comp3LabelLoc)   

		#display a score screen
		self.display_scoreboard()

		#display a play again button
		pygame.draw.rect(SCREEN, RED, self.buttonRect)
		pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
		SCREEN.blit(self.replaceButton, self.buttonLoc)

		pygame.display.flip()

	def display_hand(self, hand, x, y):    #yaccDL switch hand and AI up and down//display_hand
		for card in hand:
			SCREEN.blit(self.images[card], (x, y))    #yaccDL switch hand and AI up and down
			x += int(self.scale * self.cardSize[0])/6    #yaccDL overlap cards

	def display_scoreboard(self):
		#create labels for each player
		self.playerScoreLabel = self.font.render("You: " + str(self.poker.scores[0]), 1, BLACK)
		self.comp1ScoreLabel = self.font.render("Computer 1: "  +str(self.poker.scores[1]), 1, BLACK)
		self.comp2ScoreLabel = self.font.render("Computer 2: "  +str(self.poker.scores[2]), 1, BLACK)
		self.comp3ScoreLabel = self.font.render("Computer 3: "  +str(self.poker.scores[3]), 1, BLACK)

		SCREEN.blit(self.playerScoreLabel, (10, 10))
		SCREEN.blit(self.comp1ScoreLabel, (10, 40))
		SCREEN.blit(self.comp2ScoreLabel, (10, 70))
		SCREEN.blit(self.comp3ScoreLabel, (10, 100))

#############################################################
if __name__ == "__main__":
	os.environ['SDL_VIDEO_CENTERED'] = '1' #center screen
	pygame.init()
	pygame.display.set_caption("Poker")
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0 ,32)
	
	Runit = Control()
	Myclock = pygame.time.Clock()
	while 1:
		Runit.main()
		Myclock.tick(64)