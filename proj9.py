# import pygame
# import sys
# pygame.init()

# WINDOW_WIDTH = 1200
# WINDOW_HEIGHT = 600
# FPS = 20
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# ADD_NEW_FLAME_RATE = 25
# cactus_img = pygame.image.load('cactus_bricks.png')
# cactus_img_rect = cactus_img.get_rect()
# cactus_img_rect.left = 0
# fire_img = pygame.image.load('fire_bricks.png')
# fire_img_rect = fire_img.get_rect()
# fire_img_rect.left = 0
# CLOCK = pygame.time.Clock()
# font = pygame.font.SysFont('forte', 20)

# canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption('Mario')


# class Topscore:
#     def __init__(self):
#         self.high_score = 0
#     def top_score(self, score):
#         if score > self.high_score:
#             self.high_score = score
#         return self.high_score

# topscore = Topscore()


# class Dragon:
#     dragon_velocity = 10

#     def __init__(self):
#         self.dragon_img = pygame.image.load('dragon.png')
#         self.dragon_img_rect = self.dragon_img.get_rect()
#         self.dragon_img_rect.width -= 10
#         self.dragon_img_rect.height -= 10
#         self.dragon_img_rect.top = WINDOW_HEIGHT/2
#         self.dragon_img_rect.right = WINDOW_WIDTH
#         self.up = True
#         self.down = False

#     def update(self):
#         canvas.blit(self.dragon_img, self.dragon_img_rect)
#         if self.dragon_img_rect.top <= cactus_img_rect.bottom:
#             self.up = False
#             self.down = True
#         elif self.dragon_img_rect.bottom >= fire_img_rect.top:
#             self.up = True
#             self.down = False

#         if self.up:
#             self.dragon_img_rect.top -= self.dragon_velocity
#         elif self.down:
#             self.dragon_img_rect.top += self.dragon_velocity


# class Flames:
#     flames_velocity = 20

#     def __init__(self):
#         self.flames = pygame.image.load('fireball.png')
#         self.flames_img = pygame.transform.scale(self.flames, (20, 20))
#         self.flames_img_rect = self.flames_img.get_rect()
#         self.flames_img_rect.right = dragon.dragon_img_rect.left
#         self.flames_img_rect.top = dragon.dragon_img_rect.top + 30


#     def update(self):
#         canvas.blit(self.flames_img, self.flames_img_rect)

#         if self.flames_img_rect.left > 0:
#             self.flames_img_rect.left -= self.flames_velocity


# class Mario:
#     velocity = 10

#     def __init__(self):
#         self.mario_img = pygame.image.load('maryo.png')
#         self.mario_img_rect = self.mario_img.get_rect()
#         self.mario_img_rect.left = 20
#         self.mario_img_rect.top = WINDOW_HEIGHT/2 - 100
#         self.down = True
#         self.up = False

#     def update(self):
#         canvas.blit(self.mario_img, self.mario_img_rect)
#         if self.mario_img_rect.top <= cactus_img_rect.bottom:
#             game_over()
#             if SCORE > self.mario_score:
#                 self.mario_score = SCORE
#         if self.mario_img_rect.bottom >= fire_img_rect.top:
#             game_over()
#             if SCORE > self.mario_score:
#                 self.mario_score = SCORE
#         if self.up:
#             self.mario_img_rect.top -= 10
#         if self.down:
#             self.mario_img_rect.bottom += 10


# def game_over():
#     pygame.mixer.music.stop()
#     music = pygame.mixer.Sound('mario_dies.wav')
#     music.play()
#     topscore.top_score(SCORE)
#     game_over_img = pygame.image.load('end.png')
#     game_over_img_rect = game_over_img.get_rect()
#     game_over_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
#     canvas.blit(game_over_img, game_over_img_rect)
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#                 music.stop()
#                 game_loop()
#         pygame.display.update()


# def start_game():
#     canvas.fill(BLACK)
#     start_img = pygame.image.load('start.png')
#     start_img_rect = start_img.get_rect()
#     start_img_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
#     canvas.blit(start_img, start_img_rect)
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     pygame.quit()
#                     sys.exit()
#                 game_loop()
#         pygame.display.update()


# def check_level(SCORE):
#     global LEVEL
#     if SCORE in range(0, 10):
#         cactus_img_rect.bottom = 50
#         fire_img_rect.top = WINDOW_HEIGHT - 50
#         LEVEL = 1
#     elif SCORE in range(10, 20):
#         cactus_img_rect.bottom = 100
#         fire_img_rect.top = WINDOW_HEIGHT - 100
#         LEVEL = 2
#     elif SCORE in range(20, 30):
#         cactus_img_rect.bottom = 150
#         fire_img_rect.top = WINDOW_HEIGHT - 150
#         LEVEL = 3
#     elif SCORE > 30:
#         cactus_img_rect.bottom = 200
#         fire_img_rect.top = WINDOW_HEIGHT - 200
#         LEVEL = 4





# def game_loop():
#     while True:
#         global dragon
#         dragon = Dragon()
#         flames = Flames()
#         mario = Mario()
#         add_new_flame_counter = 0
#         global SCORE
#         SCORE = 0
#         global  HIGH_SCORE
#         flames_list = []
#         pygame.mixer.music.load('mario_theme.wav')
#         pygame.mixer.music.play(-1, 0.0)
#         while True:
#             canvas.fill(BLACK)
#             check_level(SCORE)
#             dragon.update()
#             add_new_flame_counter += 1

#             if add_new_flame_counter == ADD_NEW_FLAME_RATE:
#                 add_new_flame_counter = 0
#                 new_flame = Flames()
#                 flames_list.append(new_flame)
#             for f in flames_list:
#                 if f.flames_img_rect.left <= 0:
#                     flames_list.remove(f)
#                     SCORE += 1
#                 f.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         mario.up = True
#                         mario.down = False
#                     elif event.key == pygame.K_DOWN:
#                         mario.down = True
#                         mario.up = False
#                 if event.type == pygame.KEYUP:
#                     if event.key == pygame.K_UP:
#                         mario.up = False
#                         mario.down = True
#                     elif event.key == pygame.K_DOWN:
#                         mario.down = True
#                         mario.up = False

#             score_font = font.render('Score:'+str(SCORE), True, GREEN)
#             score_font_rect = score_font.get_rect()
#             score_font_rect.center = (200, cactus_img_rect.bottom + score_font_rect.height/2)
#             canvas.blit(score_font, score_font_rect)

#             level_font = font.render('Level:'+str(LEVEL), True, GREEN)
#             level_font_rect = level_font.get_rect()
#             level_font_rect.center = (500, cactus_img_rect.bottom + score_font_rect.height/2)
#             canvas.blit(level_font, level_font_rect)

#             top_score_font = font.render('Top Score:'+str(topscore.high_score),True,GREEN)
#             top_score_font_rect = top_score_font.get_rect()
#             top_score_font_rect.center = (800, cactus_img_rect.bottom + score_font_rect.height/2)
#             canvas.blit(top_score_font, top_score_font_rect)

#             canvas.blit(cactus_img, cactus_img_rect)
#             canvas.blit(fire_img, fire_img_rect)
#             mario.update()
#             for f in flames_list:
#                 if f.flames_img_rect.colliderect(mario.mario_img_rect):
#                     game_over()
#                     if SCORE > mario.mario_score:
#                         mario.mario_score = SCORE
#             pygame.display.update()
#             CLOCK.tick(FPS)


# start_game()



# quiz = {
#     1 : {
#         "question" : "What is the first name of Iron Man?",
#         "answer" : "Tony"
#     },
#     2 : {
#         "question" : "Who is called the god of lightning in Avengers?",
#         "answer" : "Thor"
#     },
#     3 : {
#         "question" : "Who carries a shield of American flag theme in Avengers?",
#         "answer" : "Captain America"
#     },
#     4 : {
#         "question" : "Which avenger is green in color?",
#         "answer" : "Hulk"
#     },
#     5 : {
#         "question" : "Which avenger can change it's size?",
#         "answer" : "AntMan"
#     },
#     6 : {
#         "question" : "Which Avenger is red in color and has mind stone?",
#         "answer" : "Vision"
#     }
# }


# Python program to create a simple GUI
# Simple Quiz using Tkinter

#import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json

#class to define the components of the GUI
class Quiz:
	# This is the first method which is called when a
	# new object of the class is initialized. This method
	# sets the question count to 0. and initialize all the
	# other methoods to display the content and make all the
	# functionalities available
	def __init__(self):
		
		# set question number to 0
		self.q_no=0
		
		# assigns ques to the display_question function to update later.
		self.display_title()
		self.display_question()
		
		# opt_selected holds an integer value which is used for
		# selected option in a question.
		self.opt_selected=IntVar()
		
		# displaying radio button for the current question and used to
		# display options for the current question
		self.opts=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=len(question)
		
		# keep a counter of correct answers
		self.correct=0


	# This method is used to display the result
	# It counts the number of correct and wrong answers
	# and then display them at the end as a message Box
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# This method checks the Answer after we click on Next.
	def check_ans(self, q_no):
		
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True

	# This method is used to check the answer of the
	# current question by calling the check_ans and question no.
	# if the question is correct it increases the count by 1
	# and then increase the question number by 1. If it is last
	# question then it calls display result to show the message box.
	# otherwise shows next question.
	def next_btn(self):
		
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		
		# Moves to next Question by incrementing the q_no counter
		self.q_no += 1
		
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			gui.destroy()
		else:
			# shows the next question
			self.display_question()
			self.display_options()


	# This method shows the two buttons on the screen.
	# The first one is the next_button which moves to next question
	# It has properties like what text it shows the functionality,
	# size, color, and property of text displayed on button. Then it
	# mentions where to place the button on the screen. The second
	# button is the exit button which is used to close the GUI without
	# completing the quiz.
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(gui, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		next_button.place(x=350,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(gui, text="Quit", command=gui.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_button.place(x=700,y=50)


	# This method deselect the radio button on the screen
	# Then it is used to display the options available for the current
	# question which we obtain through the question number and Updates
	# each of the options for the current question of the radio button.
	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# This method shows the current Question on the screen
	def display_question(self):
		
		# setting the Question properties
		q_no = Label(gui, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)


	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(gui, text="Raaj's QUIZ",
		width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
		
		# place of the title
		title.place(x=0, y=2)


	# This method shows the radio buttons to select the Question
	# on the screen at the specified position. It also returns a
	# list of radio button which are later used to add the options to
	# them.
	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button properties
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list

# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("800x450")

# set the title of the Window
gui.title("Raaj's Quiz")

# get the data from the json file
with open('data.json') as f:
	data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

# create an object of the Quiz Class.
quiz = Quiz()

# Start the GUI
gui.mainloop()

# END OF THE PROGRAM
