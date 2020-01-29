# game rule: the player has to enter color of the word that 
# appears on the screen within 30 seconds
# import the modules
import tkinter
import random

# list the possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 
		'Orange', 'White', 'Purple', 'Brown']
score = 0
# intial time 
timeleft = 30

# function that will start the game
def startGame(event):

	if timeleft == 30:
		# start the countdown
		countdown()
	# run function to choose the next color
	nextColor()
	reset()

def nextColor():
	# use the globally declared score and timeleft
	global score
	global timeleft

	# if the game is in play
	if timeleft > 0:

		# make the text entry box activie
		e.focus_set()
		# if the input is equal to the color, update score
		if e.get().lower() == colors[1].lower():

			score += 1

		# clear the text entry box
		e.delete(0, tkinter.END)
		# shuffle the colors array
		random.shuffle(colors)

		# change the color to type, by changing the
		# text _and_ the color to a random color value
		label.config(fg = str(colors[1]), text = str(colors[0]))

		# update the score
		scoreLabel.config(text = "Score: " + str(score))

# countdown timer function
def countdown(): 
	global timeleft
 	# if game is in play
	if timeleft > 0:
		# decrease time
		timeleft -= 1

		# update the time left label
		timeLabel.config(text = "Time left: " + str(timeleft))

		# run the function again after 1 second
		timeLabel.after(1000, countdown)

# reset game
def reset():
	global score
	global timeleft
	if timeleft == 0:
		if e.get().lower() == "restart":
			score = 0
			timeleft = 30
			label.config(text = "")
	e.delete(0, tkinter.END)
	timeLabel.config(text = "Time left: " + str(timeleft))
	scoreLabel.config(text = "Score: " + str(score))
# Driver code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("ColorGame")

#set the size
root.geometry("400x200")

# add an instructions label
instructions = tkinter.Label(root, text = "Type in the color of " 
                                                "the word, not the word text", 
                                                font = ('Helvetica', 12))

instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
                                        font = ('Helvetica', 12))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft),
							font = ('Helvetica', 12))
timeLabel.pack()

# add a label for displaying color
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

# add a text entry box for typing in colors
e = tkinter.Entry(root)

# run the startgame function when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
