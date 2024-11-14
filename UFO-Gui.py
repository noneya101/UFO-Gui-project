from tkinter import *
import pygame
import time

# Define constants
WIDTH = 500
HEIGHT = 500
xVelocity = 2
yVelocity = 3

# Initialize Pygame mixer and load the sound file
pygame.mixer.init()
sound_file = "example.mp3"
pygame.mixer.music.load(sound_file)
pygame.mixer.music.play(-1)# -1 to loop the music indefinitely

# Set up the Tkinter window
Window = Tk()
Window.geometry(f"{WIDTH}x{HEIGHT}")  # Set the window size
Window.resizable(False, False)# Lock the width and height
Window.title("UFO-Gui")

# Create the canvas
Canvas = Canvas(Window,width=WIDTH,height=HEIGHT)
Canvas.pack()

# Load background and moving object images
background_photo = PhotoImage(file='space.png')
background = Canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='ufo.png')
my_image = Canvas.create_image(0,0,image=photo_image,anchor=NW)


# Get dimensions of the moving image
image_width = photo_image.width()
image_height = photo_image.height()

# Check for boundaries and reverse direction if needed
while True:
    coordinates = Canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    Canvas.move(my_image,xVelocity,yVelocity)
    Window.update()

    # Check if music is still playing, otherwise stop the loop
    if not pygame.mixer.music.get_busy():
        is_running = False
    time.sleep(0.01)

Window.mainloop()