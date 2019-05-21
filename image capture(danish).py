from PIL import ImageGrab
import os
import time

def screenGrab():
    box = ()

# this line creates a variable to hold the screenshot
    im = ImageGrab.grab()

# This command will save the screenshot into a time-stamped png file
# FYI - getcwd() is get Current Working Directory
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    im.show()
    #im.write()
screenGrab()