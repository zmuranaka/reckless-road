# File: recklessRoad.py
# Zachary Muranaka
# Allows the user to play a game of driving a taxi on a crazy road
# This website was helpful in the creation of this game https://pygame-zero.readthedocs.io/en/stable/

import pgzrun
import sys
from random import randint

rules = (
    "Welcome to RECKLESS ROAD!\n",
    "In this game, you control a taxi driving down a crazy road.",
    "Your objective is to get as far as you can without hitting another car or pedestrian along the way.",
    "You use the arrow keys to move, but you can't go backward, so be careful.",
    "Every time you completely cross the screen, you score a point, and either another car or pedestrian is added or one of the cars or pedestrians gets faster.",
    "The game ends when you hit into another car or pedestrian.\n",
    "Drive carefully and try to score the highest you can!"
)

# Check if a width and height were supplied as command-line arguments
if len(sys.argv) == 3:
    WIDTH = int(sys.argv[1]) # Get the width from the command-line arguments
    HEIGHT = int(sys.argv[2]) # Get the height from the command-line arguments
# Otherwise set a default width and height
else:
    WIDTH = 558
    HEIGHT = 528

# Constants dealing with the height and width of actors
TAXIHEIGHT = 35
OTHERCARHEIGHT = 31
CARWIDTH = 57
PERSONHEIGHT = 42
PERSONWIDTH = 15

# Determine the amount of times we have to repeat the background image
repeatX = int(WIDTH / 558) + 1 if WIDTH % 558 else int(WIDTH / 558)
repeatY = int(HEIGHT / 528) + 1 if HEIGHT % 528 else int(HEIGHT / 528)

# Create the taxi actor and set its initial position
taxi = Actor("taxi")
taxi.pos = 80, 110

# Array of the actors (other than the player) that can be generated
potentialActors = ["graycar", "redcar", "man", "woman"]

# Global variables that keep track of the state of the game
score = 0
activeActors = [] # Array of the actors (other than the player) that are currently active
speed = [] # Array of the active actors' speeds
startScreen = True
rulesScreen = False
songIsPlaying = False
gameOver = False

# Returns one of two values depending on if the actor is a car or person
def determineVal(actor, carVal, personVal):
    return carVal if actor.image == "graycar" or actor.image == "redcar" else personVal
    
# Resets the position of the actor
def resetPosition(actor):
    actor.x = WIDTH + determineVal(actor, CARWIDTH, PERSONWIDTH)
    actor.y = randint(determineVal(actor, OTHERCARHEIGHT, PERSONHEIGHT), HEIGHT - determineVal(actor, OTHERCARHEIGHT, PERSONHEIGHT))

# Sets up a new screen
def newScreen():
    global score
    
    score += 1 # The player scores a point

    if len(activeActors) == 0 or (randint(1, 4) > 1): # Generate a random new actor with a random speed
        activeActors.append(Actor(potentialActors[randint(0, 3)]))
        speed.append(randint(1, 4))
    else: # Double the speed of a random actor
        speed[randint(0, len(speed) - 1)] *= 2
        
    taxi.x = -CARWIDTH # Reset the position of the player

    # Reset the position of all of the other actors
    for member in activeActors:
        resetPosition(member)

def draw():
    if startScreen:
        screen.draw.textbox("RECKLESS ROAD", (WIDTH / 16, HEIGHT / 16, WIDTH * 7/8, HEIGHT / 8), color="yellow")
        screen.blit("taxi", (WIDTH / 2 - CARWIDTH, HEIGHT * 5/12))
        screen.draw.textbox("Press 1 to start the game or 2 to read the rules", (WIDTH / 4, HEIGHT * 5/8, WIDTH / 2, HEIGHT / 4))
    elif rulesScreen:
        screen.clear()
        screen.draw.textbox("Rules", (WIDTH / 16, HEIGHT / 16, WIDTH * 7/8, HEIGHT / 8), color="yellow")
        screen.draw.textbox(' '.join(rules), (WIDTH / 16, HEIGHT * 7/32, WIDTH * 7/8, HEIGHT * 5/8))
        screen.draw.textbox("Press 1 to start the game", (WIDTH / 16, HEIGHT * 7/8, WIDTH * 7/8, HEIGHT / 16), color="yellow")
    else:
        # Draw the background
        for x in range(repeatX):
            for y in range(repeatY):
                screen.blit("road", (558 * x, 528 * y))

        # Draw the score
        screen.draw.text("Score: " + str(score), (0, 0), color="black", background="yellow", fontsize=40)

        # Draw the actors
        taxi.draw()
        for member in activeActors:
            member.draw()

        # Display the game over screen
        if gameOver:
            screen.clear()
            screen.draw.textbox("GAME OVER", (WIDTH / 64, HEIGHT / 32, WIDTH * 31/32, HEIGHT / 2), color="yellow")
            screen.draw.textbox("Final Score: " + str(score), (WIDTH / 4, HEIGHT * 35/64, WIDTH / 2, HEIGHT / 4))
            screen.draw.textbox("Press 1 to play again or 2 to exit", (WIDTH / 16, HEIGHT * 7/8, WIDTH * 7/8, HEIGHT / 16), color="yellow")

def update():
    global startScreen
    global rulesScreen
    global songIsPlaying
    global gameOver
    global score
    global activeActors
    global speed

    if not gameOver:
        # The player wants to start the game
        if (keyboard.kp1 or keyboard.k_1) and (startScreen or rulesScreen):
            startScreen = False
            rulesScreen = False
        # The player wants to read the rules
        elif (keyboard.kp2 or keyboard.k_2) and startScreen:
            startScreen = False
            rulesScreen = True
        # The game has started
        elif not startScreen and not rulesScreen:
            # Start the song
            if not songIsPlaying:
                songIsPlaying = True
                playSong()
            
            # Handle the player's movement
            if keyboard.right:
                if taxi.x > WIDTH + CARWIDTH: # The taxi reached the far right of the screen
                    newScreen()
                else:
                    taxi.x += 4
            if keyboard.up:
                if taxi.y < TAXIHEIGHT: # Make sure the taxi doesn't leave the screen
                    taxi.y += 15
                else:
                    taxi.y -= 4
            if keyboard.down:
                if taxi.y > HEIGHT - TAXIHEIGHT: # Make sure the taxi doesn't leave the screen
                    taxi.y -= 15
                else:
                    taxi.y += 4

            # Handle the other actors' movement
            for i in range(len(activeActors)):
                if activeActors[i].x > -determineVal(activeActors[i], CARWIDTH, PERSONWIDTH):
                    activeActors[i].x -= speed[i]
                else:
                    resetPosition(activeActors[i])

                # The game ends if the player hits another actor
                if taxi.colliderect(activeActors[i]):
                    gameOver = True
                    songIsPlaying = False
                    # Play a final note
                    tone.create("C4", 1).play()
                    tone.create("E3", 1).play()
                    tone.create("G3", 1).play()

    else: # The game is over
        if keyboard.kp1 or keyboard.k_1: # Restarts the game
            score = 0
            activeActors = []
            speed= []
            taxi.pos = 80, 110
            gameOver = False
        elif keyboard.kp2 or keyboard.k_2: # Quits the game
            exit()
                

# Plays a randomly-generated "song" in C major
def playSong():
    if not gameOver:
        randomC = 'C' + str(randint(1, 5))
        tone.create(randomC, 0.2).play()
        randomE = 'E' + str(randint(1, 5))
        tone.create(randomE, 0.2).play()
        randomG = 'G' + str(randint(1, 5))
        tone.create(randomG, 0.2).play()
        clock.schedule_unique(playSong, 0.3)

pgzrun.go()
