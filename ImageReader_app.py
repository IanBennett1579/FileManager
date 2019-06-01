import os #probably don't even need these lines, they seem pretty useless
import functools
from PIL import Image, ImageTk
import tkinter as tk

class reader(): #what's a class?
    def all(): #for any image type. Does not work if you have more than image files in the directory. Will fix later though
        directory = input('directory(LAST to open last save): ') #directory, duh

        with open('config.txt', 'r+') as config: #opening the last laved usage and/or saving
            try: #will fix later but this will do
                if directory == 'LAST': #load dir
                    directory = config.readlines()
                    directory = str(directory[0]).rstrip('\n')
                    config.seek(0)

                    pagenum = config.readlines() #load pagenum
                    pagenum = int(str(pagenum[1]).rstrip('/n'))
                    config.seek(0)
            except: 
                print('error, probably no saves')
            dirsave = config.readlines() #save directory
            dirsave[0] = (directory + '\n')
            config.seek(0)
            config.writelines(dirsave)

        images = [] #setting up important variables. the global variables are a result of me being to lazy to make an innit or finding a way to do it without globals
        global imageamount 
        imageamount = -1
        global imagenumber
        try:
            imagenumber = pagenum
        except:
            imagenumber = 0

        def opendir(images, directory): #recusive function to load all the images
            for file in os.listdir(os.fsencode(directory)):
                filename = os.fsdecode(file) #just the name of the file in the working directory
                print(filename) #cute lil print to terminal to make you think it's a cool hacker program
                if os.path.isfile(directory + '\\' + filename): #if file, loads to images. I need to make it so it only loads images
                    images.append(Image.open(directory + '\\' + filename))
                    global imageamount
                    imageamount += 1
                elif os.path.isdir(directory + '\\' + filename): #if directory, recurses function but the working directory is now that directory
                    opendir(images, (directory + '\\' + filename))
        opendir(images, directory) #wow, wonder what this does

        root = tk.Tk() #absolutely useless line, I should just delete it
        
        root.attributes("-fullscreen", True) #fullscreen

        images[imagenumber].thumbnail((1920, 1080))
        tkimage = ImageTk.PhotoImage(images[imagenumber]) #just loads the first image
        panel = tk.Label(root, image=tkimage)
        panel.pack()

        def Left(event): #cycle to previous image
            global imagenumber
            if imagenumber > 0: #to make sure you dont try to go to the -1 value in a list
                imagenumber -= 1 #just changes the image to the one before
                images[imagenumber].thumbnail((1920, 1080))
                tkimage = ImageTk.PhotoImage(images[imagenumber])
                panel.configure(image=tkimage)
                panel.image = tkimage
                
                with open('config.txt', 'r+') as config: #saving pagenum
                    pagesave = config.readlines()
                    pagesave[1] = (str(imagenumber) + '\n')
                    config.seek(0)
                    config.writelines(pagesave)


        def Right(event): #cycle to next image
            global imagenumber
            global imageamount
            if imagenumber < imageamount: #to make sure program doesn't try to go over the amount of images availiable
                imagenumber += 1 #just changes the image to the next one
                images[imagenumber].thumbnail((1920, 1080))
                tkimage = ImageTk.PhotoImage(images[imagenumber])
                panel.configure(image=tkimage)
                panel.image = tkimage
                with open('config.txt', 'r+') as config: #saving pagenum
                    pagesave = config.readlines()
                    pagesave[1] = (str(imagenumber) + '\n')
                    config.seek(0)
                    config.writelines(pagesave)

        def F11(event): #toggles fullscreen
            if root.attributes('-fullscreen'):
                root.attributes('-fullscreen', False)
            else:
                root.attributes('-fullscreen', True)

        def Escape(event): #destroys window
            root.destroy()

        root.bind("<Left>", Left) #bindings
        root.bind("<Right>", Right)
        root.bind("<F11>", F11)
        root.bind("<Escape>", Escape)

        root.focus_force() #in focus for keypress
        root.mainloop() #no idea what this is doing
    

