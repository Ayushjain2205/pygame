from tkinter import *
from PIL import ImageTk , Image

root=Tk()
root.title("ESCAPE ROOM GAME")

books= ImageTk.PhotoImage(Image.open("book1.jpg"))
clocks2= ImageTk.PhotoImage(Image.open("clocks1.jpg"))
key1= ImageTk.PhotoImage(Image.open("key1.jpg"))
key2= ImageTk.PhotoImage(Image.open("key2.jpg"))
key3= ImageTk.PhotoImage(Image.open("key3.jpg"))
mainroom= ImageTk.PhotoImage(Image.open("mainroom.jpg"))
maze1= ImageTk.PhotoImage(Image.open("maze.jpg"))
switchoff1= ImageTk.PhotoImage(Image.open("switchoff1.jpg"))
switchon1= ImageTk.PhotoImage(Image.open("switchon1.jpg"))
txt='''This is the Escape room. Here, in this game you are locked in a room,
        filled with items you can interact with, and all you have to do is
        explore all the objects and find the clues and connect the dots to 
        find the key and open the door to escape the room.
        The rules are simple, there is a broken key on the table near the 
        door, one of three pieces.Find the remaining two, and combine them to 
        get a whole key, and open the door!!'''

booktxt="Pages on war of China? Must contain something important"
clockstxt1="Is it 12:30??"
switchontxt="What happens when I switch it off"
emptyboardtxt="Toggle the switches it might help"


labelText = StringVar()
labelText.set(txt)

my_label_image=Label(image=mainroom)
my_label_image.grid(row=10,column=10)

my_label_text=Label(textvariable=labelText)
my_label_text.grid(row=10,column=800)


def books_shelf_open():
    global my_label_image
    global my_label_text
    global bookstxt
    global books
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label(image=books)
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(booktxt)
    my_label_text=Label(textvariable=labelText)
    my_label_text.grid(row=10,column=800)

def brokenkey_open():
    global my_label_image
    global my_label_text
    global bookstxt
    global key1
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label(image=key1)
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(booktxt)
    my_label_text=Label()
    my_label_text.grid(row=10,column=800)   


def clocks_open():
    global my_label_image
    global my_label_text
    global clockstxt1
    global clocks2
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label(image=clocks2)
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(clockstxt1)
    my_label_text=Label(textvariable=labelText)
    my_label_text.grid(row=10,column=800)

def back_mainroom():
    global my_label_image
    global my_label_text
    global mainroom
    global txt
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label(image=mainroom)
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(txt)
    my_label_text=Label()
    my_label_text.grid(row=10,column=800)


def switchon_open():
    global my_label_image
    global my_label_text
    global switchontxt
    global switchon1
    
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label(image=switchon1)
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(switchontxt)
    my_label_text=Label(textvariable=labelText)
    my_label_text.grid(row=10,column=800)


def switchoff_open():
    global my_label_image
    global my_label_text
    #global switchontxt
    global switchoff1
    
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label(image=switchoff1)
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(switchontxt)
    my_label_text=Label()
    my_label_text.grid(row=10,column=800)


def empty_open():
    global my_label_image
    global my_label_text
    global emptyboardtxt
    global switchoff1
    
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label()
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(emptyboardtxt)
    my_label_text=Label(textvariable=labelText)
    my_label_text.grid(row=10,column=800)


def maze_open():
    global my_label_image
    global my_label_text
    global maze1
    #global switchoff1
    
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label(image=maze1)
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(emptyboardtxt)
    my_label_text=Label()
    my_label_text.grid(row=10,column=800)

u=0
donetxt="Code Accepted!"
notdonetxt="INCORRECT CODE"
entertxt=" ENTER CODE IN SECRET TEXT BOX BELOW"

def take():
    global u
    c=b.get()
    if c=="123055":
        u=1

def enter():
    global my_label_image
    global my_label_text
    my_label_image.grid_forget()
    my_label_text.grid_forget()
    my_label_image=Label()
    my_label_image.grid(row=10,column=10)
    labelText = StringVar()
    labelText.set(entertxt)
    my_label_text=Label(textvariable=labelText)
    my_label_text.grid(row=10,column=800)


def check():
    global my_label_image
    global my_label_text
    global donetxt
    global notdonetxt
    global u
    if u ==0:
        my_label_image.grid_forget()
        my_label_text.grid_forget()
        my_label_image=Label()
        my_label_image.grid(row=10,column=10)
        labelText = StringVar()
        labelText.set(notdonetxt)
        my_label_text=Label(textvariable=labelText)
        my_label_text.grid(row=10,column=800)
    else:
        my_label_image.grid_forget()
        my_label_text.grid_forget()
        my_label_image=Label()
        my_label_image.grid(row=10,column=10)
        labelText = StringVar()
        labelText.set(donetxt)
        my_label_text=Label(textvariable=labelText)
        my_label_text.grid(row=10,column=800)


unlocktxt='''Congratualtions You have completed all the puzzles and unlocked the main door !
              Well played!!!'''
locktxt='''Not yet! You have not completed all the puzzles!
            '''
def done():
    global my_label_image
    global my_label_text
    global unlocktxt
    global locktxt
    if u ==0:
        my_label_image.grid_forget()
        my_label_text.grid_forget()
        my_label_image=Label()
        my_label_image.grid(row=10,column=10)
        labelText = StringVar()
        labelText.set(locktxt)
        my_label_text=Label(textvariable=labelText)
        my_label_text.grid(row=10,column=800)
    else:
        my_label_image.grid_forget()
        my_label_text.grid_forget()
        my_label_image=Label()
        my_label_image.grid(row=10,column=10)
        labelText = StringVar()
        labelText.set(unlocktxt)
        my_label_text=Label(textvariable=labelText)
        my_label_text.grid(row=10,column=800)




#Category Buttons
bookshelf = Button(root, text = 'BOOK SHELF', bd = '5' , command=books_shelf_open)  
bookshelf.place(x=0,y=405)

clocks = Button(root, text = 'CLOCKS', bd = '5',command=clocks_open)  
clocks.place(x=130,y=405)

emptyswitch = Button(root, text = 'EMPTY BOARD ', bd = '5',command=empty_open )  
emptyswitch.place(x=250,y=405)

emptyswitch = Button(root, text = 'SWITCH ON', bd = '5',command=switchon_open)  
emptyswitch.place(x=250,y=455)

emptyswitch = Button(root, text = 'SWITCH OFF', bd = '5',command=switchoff_open)  
emptyswitch.place(x=250,y=505)

maze = Button(root, text = 'MAZE', bd = '5',command=maze_open)  
maze.place(x=380,y=405)

locker = Button(root, text = 'LOCKER', bd = '5', command=enter)  
locker.place(x=450,y=405)

checkval=Button(root,text='CHECK',bd='5',command=check)
checkval.place(x=450,y=450)

brokenkey = Button(root, text = 'BROKEN KEY', bd = '5',command=brokenkey_open)  
brokenkey.place(x=550,y=405)

maindoor = Button(root, text = 'MAIN DOOR', bd = '5',command=done)  
maindoor.place(x=650,y=405)

back = Button(root, text = 'BACK TO MAIN ROOM', bd = '5' , command=back_mainroom)  
back.place(x=1000,y=405)

secret=Label(text="Secret TEXTBOX")
secret.place(x=900,y=505)

b=StringVar()
text=Entry(textvariable=b)
text.place(x=1000, y=505)


unlock=Button(root, text="UNLOCK",bd='5',command=take)
unlock.place(x=1150,y=505)

root.mainloop()
