
#-----------------------------
#Import things here
from tkinter import* #Used to add all widgets and tkinter GUI features
import random #Used in all random functions
from PIL import ImageTk,Image #Allows for opening of images in different formats
#-----------------------------


root = Tk() #Used to create a root window
root.title("Mime Story Generator") # Establishes the title of the program
root.geometry("610x300") # Establishes the size of the windows
root.resizable(width=False, height=False) #Make the window non-resizable

canvas = Canvas(root,height=300,width=600) # Establishes the size of the canva
canvas.grid(row=5,column=0) # Places the canvas on a certain place in the program

MimeList = ['Play Tennis','Pull Rope','Watch TV','Sing in the Shower','Dance','Wash Car','Trapped in Box','Play Football','Listen to Music','Make a Cake','Wash your Hands','Play the Piano','Play Basketball']
# The list in which all of the different stories are held

def gen_story():
    scene = MimeList[random.randint(0,len(MimeList)-1)] #Code that randomly chooses a string from the list
    scene1 = MimeList[random.randint(0,len(MimeList)-1)]#Code that randomly chooses a string from the list
    scene2 = MimeList[random.randint(0,len(MimeList)-1)]#Code that randomly chooses a string from the list

    while scene == scene1 or scene == scene2 or scene1 == scene2 or scene == scene1 == scene2:
    #While loop that checks if more than 2 of the strings are the same
    #If True than move to code below
        
        scene = "" 
        scene1 = ""
        scene2 = ""
    #Sets all scenes back to their original value(nothing)
        scene = MimeList[random.randint(0,len(MimeList)-1)]
        scene1 = MimeList[random.randint(0,len(MimeList)-1)]
        scene2 = MimeList[random.randint(0,len(MimeList)-1)]
    #Randomly generates strings from MimeList one more time
    #Goes back and runs while loop again, if true it repeats, if false it moves on
        
    story = scene + ", " + scene1 + ", " + scene2
    #Puts all scenes into one variable(story), and places commas and spaces in between each of them

    l1.config(text=story)
    #Places the variable story into the textbox

    myimg = scene.replace(" ","") + ".jpg"
    #Replaces the space in between the strings with nothing and adds .jpg
    #This changes the string into its corresponding picture file and places it into myimg
    try:
        myimage = Image.open(myimg) #Makes myimage equal to myimg in its open state
    except:
        print("can't find file")
    #Error checking statement prints a statement if the image is not found
    
    myimage = myimage.resize((200, 150))
    #Resizes myimage to allow it to fit in the GUI window
    myimg = ImageTk.PhotoImage(myimage)
    #Displays the image
    
    canvas.create_image(0, 0, image=myimg, anchor = NW)
    #Creates the image, positions it and anchors it to a specific point


    myimg1 = scene1.replace(" ","") + ".jpg"
    try:
        myimage1 = Image.open(myimg1)
    except:
        print("can't find file")
    myimage1 = myimage1.resize((200, 150))
    myimg1 = ImageTk.PhotoImage(myimage1)
    canvas.create_image(200, 0, image=myimg1, anchor = NW)
 
    #Block of code above is same as code above, but corresponds to the second scene
    
    myimg2 = scene2.replace(" ","") + ".jpg"
    try:
        myimage2 = Image.open(myimg2)
    except:
        print("can't find file")
    myimage2 = myimage2.resize((200, 150))
    myimg2 = ImageTk.PhotoImage(myimage2)
    canvas.create_image(400, 0, image=myimg2, anchor = NW)
    try:
        canvas.itemconfig(canvas.create_image,image=myimg2)
    except:
        print("I understand that this error is here, I am fixing it and it will be gone in version 2.0 - Stay Tuned")
        canvas.itemconfig(canvas.create_image, image=myimg2)
    
        
        
    #Block of code above is same as code above, but corresponds to the third scene


b1 = Button(text="Generate Story", command=gen_story)
#Creates the button used to generate the story, adds text and sets its command to gen_story, which is defined above

b1.grid(row=4,column=0, padx=25, pady=20)
#Places the button in a specific place and creates space around it using padx and pady

l1 = Label(text="", borderwidth=2, relief="solid")
#Creates the label, sets text to nothing since it will be filled during gen_story and gives it a label
l1.grid(row=3,column=0, pady=10)
#Places the label in a specific place and creates space around it using padx and pady


#Runs Code
mainloop()


