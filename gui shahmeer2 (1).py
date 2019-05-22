#!/usr/bin/env python
# coding: utf-8

# In[1]:



from tkinter import *
 
window = Tk()
 
window.title("Remote Scren Viewer Taking SS")

window.geometry('220x430')
#heading k lie.......................
 
lbl = Label(window, text="Welcome to  Remote Screen Viewer", font=("Arial Bold", 50))

 
lbl.grid(column=3, row=7)
#-------------------------------
#space add.. line break....

lbl = Label(window, text="  ")

 
lbl.grid(column=3, row=9)
#_________________________________

_
# socket server connection
def serverconn():
 
    lbl.configure(text=" You have to enter ip address of Pc2 ")
 
btn = Button(window, text="Connect to Pc2", font=("Arial Bold", 20), bg="blue", fg="white", command=serverconn)
 
btn.grid(column=3, row=11)

#____________________________

#space add.. line break....

lbl = Label(window, text="  ")

 
lbl.grid(column=3, row=13)
#________________________
#socket progrming of client
def clientconn():
 
    lbl.configure(text=" You have to enter ip address of Pc1 ")
 
btn = Button(window, text="Connect to Pc1", font=("Arial Bold", 20), bg="blue", fg="white", command=clientconn)
 
btn.grid(column=3, row=15)

#space add.. line break....

lbl = Label(window, text="  ")

 
lbl.grid(column=3, row=17)



#--------------
#img grab buttons k lie
 
def coonection():
 
    lbl.configure(text=" Your pc will be connected after you ener ip adress and port")
 
btn = Button(window, text="Connect with other computer", font=("Arial Bold", 20), bg="blue", fg="white", command=coonection)
 
btn.grid(column=3, row=19)

#___________________________________________

lbl = Label(window, text="  ")

 
lbl.grid(column=3, row=21)
#----------------------------------------
#img grab buttons k lie
 
def imagegrab():
    from PIL import ImageGrab
    import os
    import time


    box = ()

# this line creates a variable to hold the screenshot
    im = ImageGrab.grab()

# This command will save the screenshot into a time-stamped png file
# FYI - getcwd() is get Current Working Directory
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    im.show()
    
    
    lbl.configure(text=" Image has been grabbed!!")
    
    #im.write()
 
    lbl.configure(text=" Image has been captured!!!")
 
btn = Button(window, text="Image Grab", font=("Arial Bold", 20), bg="blue", fg="white", command=imagegrab)
 
btn.grid(column=3, row=23)

imagegrab()

#def k function saryy github k codes hain .


lbl = Label(window, text="  ")

 
lbl.grid(column=3, row=25)
#----------------------------
#chat box

def serverc():
    import socket
    import sys
    import time


    s = socket.socket()
    host = socket.gethostname()
    print("server will start on host : ",host)
    port = 8080
    s.bind((host,port))
    print("")
    print("server done binding to host and port successfully")
    print("")
    print("Server is waiting for incoming connections")
    print("")
    s.listen(1)
    conn,addr = s.accept()
    print(addr," Has connected to the server and is now online...")
    print("")
    while 1:
            message = input(str(">>"))
            message = message.encode()
            conn.send(message)
            print("Message has been sent...")
            print("")
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print("Client : ",incoming_message)
            print("") 



    lbl.configure(text="server messages !!")
 
btn = Button(window, text="Server Chat . To send mess to client", font=("Arial Bold", 20) , bg="blue", fg="white", command=serverc)
 
btn.grid(column=3, row=32)


lbl = Label(window, text="  ")

 
lbl.grid(column=3, row=37)

#line break
lbl = Label(window, text="  ")

 
lbl.grid(column=3, row=39)
def clientc():
    lbl.configure(text="client messages !!")
 
btn = Button(window, text="mess box", font=("Arial Bold", 20) , bg="black", fg="white", command=clientc)
 
btn.grid(column=3, row=42)

 
window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




