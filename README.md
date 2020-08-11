# RECKLESS ROAD

## What is this Project?

This project is a game I made with [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/) where you control a taxi driving down a crazy road. Your objective is to get as far as you can without hitting another car or pedestrian along the way.

## How do I Start the Game?

First of all, you need Python3 and Pygame Zero installed to run the game. You can find instructions on how to install Pygame Zero [here](https://pygame-zero.readthedocs.io/en/stable/installation.html). After that, all you need to do to run the game is double click the driver.py file, which will launch a GUI menu that allows you to choose the dimensions of the game. Another way to start the game is by double clicking the recklessRoad.py file, which sets the dimensions to the default of 558 x 528. The final way to run the game is by launching a command prompt from the folder where the files are located and typing either ```driver.py```, which will launch the GUI menu, or ```recklessRoad.py``` followed by the dimensions you want (width x height). For example, to launch the game with a width of 1000 and a height of 600, you would type ```recklessRoad.py 1000 600``` into the command prompt and press enter.

## How do I Play the Game?

You use the arrow keys to move the taxi - up moves the taxi up, right moves the taxi forward, and down moves the taxi down. You *cannot* go backward, so drive carefully. Every time you completely cross the screen, you score a point and the game gets harder because either another car or pedestrian is added, or one of the existing cars or pedestrians increases in speed!

## When Does the Game End?

The game ends when you hit into another car or a pedestrian, and your final score is equal to the number of times you completely crossed the screen.

## Files:

driver.py  
&nbsp;&nbsp;&nbsp;&nbsp;This file contains the GUI menu that allows you to choose the dimensions of the game. The three options are 960 x 540 (16/9 aspect ratio), 1024 x 768 (4/3 aspect ratio), and 1280 x 800 (16/10 aspect ratio). When one of the dimension boxes is clicked, recklessRoad.py is called from the command prompt using the dimensions as arguments.  
recklessRoad.py  
&nbsp;&nbsp;&nbsp;&nbsp;This file is the actual game. It draws the window depending on the given command-line argument dimensions (or 558 x 528 if no dimensions were given) and handles the gameplay, including the movement of the taxi and all other cars and pedestrians. It also detects collisions between the taxi and the other cars or pedestrians to determine when the game is over, and plays a simple "song" randomly generated using Pygame Zero's built-in tone generator. Finally, it gives the player the option to read the rules before the game starts and restart it once it's over.

## Sources:

I created the images using [Piskel](https://www.piskelapp.com/), an [open source](https://github.com/piskelapp/piskel) sprite editor.  
Sources that helped me create the project:  
https://pygame-zero.readthedocs.io/en/stable/  
&nbsp;&nbsp;&nbsp;&nbsp;The Pygame Zero documentation was very helpful during the creation of this game.

## Author:

Zachary Muranaka  
&nbsp;&nbsp;&nbsp;&nbsp;zacharymuranaka@mail.weber.edu  
&nbsp;&nbsp;&nbsp;&nbsp;https://zmuranaka.github.io
