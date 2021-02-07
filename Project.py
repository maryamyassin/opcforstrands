# importing tkinter
# time function used to calculate time 
import opc, time
import tkinter as tk
from tkinter import ttk

#Create a client object
client = opc.Client('localhost:7890')
bits = ( (80,0,0), (0,255,0) )

#Creating a window
win = tk.Tk()
win.title("Fadecandy")
win.geometry("450x70+10+10") #setting window size
win.resizable(0,0) #Prevents window from being resized


#Taking user input from terminal to assign to numLEDs
number = input ("Enter the number of LEDs you would like to display: ")
numberofLEDs = int(number)


'''Defining Button event handlers'''

#Rapidly fade all LEDs on and off
def strobeAction():
    #creating a loop
    i = 0
    while i < 6:
        #creating colours to be displayed in strobe
        black = [ (0,0,0) ] * numberofLEDs
        white = [ (255,255,255) ] * numberofLEDs
        pink = [ (255,0,255) ] * numberofLEDs
        blue = [ (100,149,237) ] * numberofLEDs
        green = [ (124,252,0) ] * numberofLEDs
        purple = [ (221,160,221) ] * numberofLEDs

        
        client.put_pixels(white)
        time.sleep(0.2) 
        client.put_pixels(black)
        time.sleep(0.2)
        client.put_pixels(pink)
        time.sleep(0.2)
        client.put_pixels(blue)
        time.sleep(0.2)
        client.put_pixels(green)
        time.sleep(0.2)
        client.put_pixels(purple)
        time.sleep(0.2)
        i += 1

#Light every LED one by one to create a pacman effect
def pacmanAction():
    j = 0
    while j < 6:
        for i in range(numberofLEDs):
                pixels = [ (0,0,0) ] * numberofLEDs
                pixels[i] = (254, 248, 51)
                client.put_pixels(pixels)
                time.sleep(0.02)
        j += 1

                
#Each LED strip glows dimly, and one strip at a time will briefly brighten                
def descendingAction():
    j = 0
    while j < 6:
        for strip in range(8):
                pixels = [ (90,90,90) ] * 512
                for i in range(32):
                        pixels[strip * 64 + i * 2] = (255,0,200)

                # Label all the strips 
                '''for s in range(8):
                        pixels[s * 64 + 0] = bits[(s >> 2) & 1]
                        pixels[s * 64 + 1] = bits[(s >> 1) & 1]
                        pixels[s * 64 + 2] = bits[(s >> 0) & 1]'''

                client.put_pixels(pixels)
                time.sleep(0.5)
        j += 1

#Alternate between 2 different colours on every other LED.
def blinkAction():
    
    numPairs = numberofLEDs//2

    j = 0
    while j < 6:
                black = [ (0,0,0), (255,255,255) ] * numPairs
                white = [ (255,0,255), (0,0,0) ] * numPairs

                client.put_pixels(black)
                time.sleep(0.5)
                client.put_pixels(white)
                time.sleep(0.5)
                j += 1

def scatteredAction():
    j = 0
    while j < 6:
                numStrings = numberofLEDs//6 

                string = [ (128, 128, 128) ] * 64
                for i in range(8):
                        string[7 * i] = (255, 0, 200)
                for i in range(5):
                        string[10 * i] = (0, 255, 0)	
                for i in range(2):
                        string[13 * i] = (255, 0, 0)	

                # Immediately display new frame
                pixels = string * numStrings
                client.put_pixels(pixels)
                client.put_pixels(pixels)

                j += 1
                

#adding label and placing in window using grid function
aLabel = ttk.Label(win, text="Which animation would you like?")
aLabel.grid(column=1, row=0)

#Creating buttons, adding button caption and assigning command 
action = ttk.Button(win, text="Strobe", command=strobeAction)
action.grid(column=0, row=4)    

action1 = ttk.Button(win, text="Pacman", command=pacmanAction)
action1.grid(column=1, row=4)

action2 = ttk.Button(win, text="Descending LEDs", command=descendingAction)
action2.grid(column=2, row=4)

action3 = ttk.Button(win, text="Blink", command=blinkAction)
action3.grid(column=0, row=5)

action3 = ttk.Button(win, text="Scattered", command=scatteredAction)
action3.grid(column=2, row=5)

#start the event loop
win.mainloop()
