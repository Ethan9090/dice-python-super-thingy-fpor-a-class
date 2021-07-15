from tkinter import *
from PIL import ImageTk, Image
import random



root = Tk()

root.title("DIce game")

root.geometry("800x550")

root.configure(background="gray")

Dicepicutre6 = ImageTk.PhotoImage(Image.open("dice6.jpg"))


labeltitle = Label(root,text="dice game",bg="pink",fg="blue")

labeltitle.place(relx=0.5,rely=0.1,anchor=CENTER)


labeldisplay = Label(root,text="",bg="pink",fg="blue")

labeldisplay.place(relx=0.5,rely=0.5,anchor=CENTER)


labelplayer1 = Label(root,text="player1",bg="pink",fg="blue")

labelplayer1.place(relx=0.5,rely=0.2,anchor=CENTER)


labelscore1 = Label(root,text="",bg="pink",fg="blue")

labelscore1.place(relx=0.5,rely=0.3,anchor=CENTER)



labelplayer2 = Label(root,text="player2",bg="pink",fg="blue")

labelplayer2.place(relx=0.9,rely=0.5,anchor=CENTER)


labelscore2 = Label(root,text="",bg="pink",fg="blue")

labelscore2.place(relx=0.9,rely=0.6,anchor=CENTER)


labelplayer3 = Label(root,text="player3",bg="pink",fg="blue")

labelplayer3.place(relx=0.5,rely=0.8,anchor=CENTER)


labelscore3 = Label(root,text="",bg="pink",fg="blue")

labelscore3.place(relx=0.5,rely=0.9,anchor=CENTER)


labelplayer4 = Label(root,text="player4",bg="pink",fg="blue")

labelplayer4.place(relx=0.1,rely=0.5,anchor=CENTER)


labelscore4 = Label(root,text="",bg="pink",fg="blue")

labelscore4.place(relx=0.1,rely=0.6,anchor=CENTER)

turn = 1

player1_score = 0
player2_score = 0
player3_score = 0
player4_score = 0

def start():
    
    global turn
    

    global player1_score  
    
    global player2_score  
    
    global player3_score  
    
    global player4_score  
    
    print("working")
    
    randomnumber = random.randint(1,6)
    
    if turn == 1:
    
        player1_score = player1_score + randomnumber
    
        labelscore1["text"]=str(player1_score)
    
        labeldisplay["text"]="player 1 rolled a " + str(randomnumber) + " and it makes their total score " + str(player1_score)
        
        turn = 2
        
    elif turn == 2:
    
        player2_score = player2_score + randomnumber
    
        labelscore2["text"]=str(player2_score)
    
        labeldisplay["text"]="player 2 rolled a " + str(randomnumber) + " and it makes their total score " + str(player2_score)
        
        turn = 3
        
    elif turn == 3:
    
        player3_score = player3_score + randomnumber
    
        labelscore3["text"]=str(player3_score)
    
        labeldisplay["text"]="player 3 rolled a " + str(randomnumber) + " and it makes their total score " + str(player3_score)
        
        turn = 4
        
    elif turn == 4:
    
        player4_score = player4_score + randomnumber
    
        labelscore4["text"]=str(player4_score)
    
        labeldisplay["text"]="player 4 rolled a " + str(randomnumber) + " and it makes their total score " + str(player4_score)
        
        turn = 1
    
button1 = Button(root,image=Dicepicutre6,command=start)

button1.place(relx=0.5,rely=0.6,anchor=CENTER)



root.mainloop()