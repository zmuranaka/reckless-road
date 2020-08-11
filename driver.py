# File: driver.py
# Zachary Muranaka
# Displays a menu that allows the user to choose the dimensions of the game

import pgzrun
import subprocess

# Coordinates of the boxes
promptBox = Rect(50, 25, 700, 150)
resBoxes = [ Rect(150, 225, 500, 50), Rect(150, 325, 500, 50), Rect(150, 425, 500, 50) ]

def draw():
    screen.draw.textbox("Choose the dimensions of the game", promptBox, color="yellow")
    screen.draw.textbox("960 x 540", resBoxes[0])
    screen.draw.textbox("1024 x 768", resBoxes[1])
    screen.draw.textbox("1280 x 800", resBoxes[2])

def on_mouse_down(pos):
    # Call recklessRoad.py when one of the boxes is clicked, passing the respective dimensions as command-line arguments
    if(resBoxes[0].collidepoint(pos)):
        subprocess.call(["python.exe", "recklessRoad.py", "960", "540"]) # 16/9 aspect ratio
    elif(resBoxes[1].collidepoint(pos)):
        subprocess.call(["python.exe", "recklessRoad.py", "1024", "768"]) # 4/3 aspect ratio
    elif(resBoxes[2].collidepoint(pos)):
        subprocess.call(["python.exe", "recklessRoad.py", "1280", "800"]) # 16/10 aspect ratio

pgzrun.go()
