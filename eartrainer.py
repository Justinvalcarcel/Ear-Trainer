import winsound
import math
import random
import time
from tkinter import *

#Base frequency, everything is based off of Concert C
frequency = 528

###change frequency

scalestring = ('Key:  C')
def changefrequency(x):
    global frequency
    global scalestring
    global scaletext
    frequency = x
    geneven(x)
    genharmonic(x)
    genpythag(x)
    if x==528:
        scalestring=('Key:  C')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==559:
        scalestring=('Scale: Db')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==583:
        scalestring=('Scale: D')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==628:
        scalestring=('Scale: Eb')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==665:
        scalestring=('Scale: E')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==705:
        scalestring=('Scale: F')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==747:
        scalestring=('Scale: Gb')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==791:
        scalestring=('Scale: G')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==838:
        scalestring=('Scale: Ab')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==888:
        scalestring=('Scale: A')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    elif x==941:
        scalestring=('Scale: Bb')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)
    else:
        scalestring=('Scale: B')
        scaletext.place_forget()
        scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
        scaletext.place(x=135, y=50)





###create frequencies - even temp
eventemp = []

def geneven(frequency):
    global play_scale
    global eventemp
    even_factor = math.pow (2, 1.0/12)

    eventemp1 = [frequency]

    counter = 0

    while counter <= 11:
        eventemp1.append(eventemp1[counter]*even_factor)
        counter +=1
    
    eventemp1 = [int(float(x)+.5) for x in eventemp1]
    eventemp = eventemp1
    
    play_scale = eventemp

#Initializes Even Temp
geneven(frequency)


###create frequencies - harmonic
harmonic = []
def genharmonic(frequency):
    global harmonic
    global play_scale
    harmonic_factor = [1.0, 17.0/16,9.0/8,19.0/16,5.0/4,21.0/16,11.0/8,
                     3.0/2,25.0/16,27.0/16, 7.0/4,15.0/8,2.0]
    harmonic1 = [frequency]

    counter = 1

    while counter <=12:
        harmonic1.append(harmonic1[0]*harmonic_factor[counter])
        counter+=1

    counter = 0

    while counter <=12:
        if harmonic1[counter] > frequency * 2:
            harmonic1[counter] = harmonic1[counter] / 2  
        else:
            counter +=1

    harmonic1.sort()
    harmonic1 = [int(float(x)+.5) for x in harmonic1]
    harmonic=harmonic
    
    play_scale = harmonic


####frequencies - Pythag
pythag =[]
def genpythag(frequency):
    global pythag
    global play_scale
    pythag_factor = [1.0, 256.0/243, 9.0/8,32.0/27,81.0/64,4.0/3,729.0/512,1.5,
                     128.0/81,27.0/16, 16.0/9, 243.0/128, 2.0]
    
    pythag = [frequency]
    counter = 1

    while counter <=12:
        pythag.append(frequency*pythag_factor[counter])
        counter +=1
    pythag = [int(float(x)+.5) for x in pythag]

    
    play_scale = pythag

    

##### Scale to play - even temp is default

play_scale = eventemp
keystring = ('Scale: Even Temp')
def setpythag():
    global keystring
    global keytext
    play_scale = pythag
    keystring=('Scale: Pythagorean')
    keytext.place_forget()
    keytext = Label(root, text = keystring, bg='black', fg='lime', font=('purisa',14))
    keytext.place(x=135, y=75)
def setharmonic():
    play_scale=harmonic
    global keystring
    global keytext
    play_scale = pythag
    keystring=('Scale: Harmonic')
    keytext.place_forget()
    keytext = Label(root, text = keystring, bg='black', fg='lime', font=('purisa',14))
    keytext.place(x=135, y=75)
def seteven():
    play_scale=eventemp
    global keystring
    global keytext
    play_scale = pythag
    keystring=('Scale: Even Temp')
    keytext.place_forget()
    keytext = Label(root, text = keystring, bg='black', fg='lime', font=('purisa',14))
    keytext.place(x=135, y=75)

#### Play scale

    ##Generates random interval
def generate():
    global note2
    note2 = random.randint(0,12)
    

generate()

def playnotes():
    global frequency
    winsound.Beep(frequency, 1000)
    time.sleep(.5)
    winsound.Beep(play_scale[note2], 1000)


### GUI

root = Tk()
root.wm_title("Ear Trainer")
root.geometry("310x575")
root.configure(background='white')

menu = Menu(root)
header = Label(root, text = 'Ear Trainer', bg='black', fg='lime', font=('purisa',16))
scaletext = Label(root, text = scalestring, bg='black', fg='lime', font=('purisa',14))
keytext = Label(root, text = keystring, bg='black', fg='lime', font=('purisa',14))


playnotes = Button(root, text = 'Play Notes', command=playnotes,bg='DarkCyan', height = 5, width=15, fg='white',font=('purisa',12))
newnotes = Button(root, text = 'New interval', command=generate,bg='DarkCyan', height = 5, width = 15, fg='white',font=('purisa',12))

    #scale degree buttons
unison = Button(root, text = 'Unison', command = lambda: answer(0), bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
minor2 = Button(root, text = 'Minor 2nd', command = lambda: answer(1),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
major2 = Button(root, text = 'Major 2nd', command = lambda: answer(2),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
minor3 = Button(root, text = 'Minor 3rd', command = lambda: answer(3),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
major3 = Button(root, text = 'Major 3rd', command = lambda: answer(4),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
perfect4 = Button(root, text = 'Perfect 4th', command = lambda: answer(5),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
dim5 = Button(root, text = 'Diminished 5th', command = lambda: answer(6),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
perfect5 = Button(root, text = 'Perfect 5th', command = lambda: answer(7),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
minor6 = Button(root, text = 'Minor 6th', command = lambda: answer(8),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
major6 = Button(root, text = 'Major 6th', command = lambda: answer(9),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
minor7 = Button(root, text = 'Minor 7th', command = lambda: answer(10),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
major7 = Button(root, text = 'Major 7th', command = lambda: answer(11),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)
octave = Button(root, text = 'Octave', command = lambda: answer(12),bg='DarkCyan', fg='white', font=('purisa',10),height = 1, width=12)

    #pack notes
header.pack(pady=5)
unison.pack(padx = 8, pady=5, anchor=W)
minor2.pack(padx = 8, pady=5, anchor=W)
major2.pack(pady=5, anchor=W,padx = 8)
minor3.pack(pady=5, anchor=W,padx = 8)
major3.pack(pady=5, anchor=W,padx = 8)
perfect4.pack(pady=5, anchor=W,padx = 8)
dim5.pack(pady=5, anchor=W,padx = 8)
perfect5.pack(pady=5, anchor=W,padx = 8)
minor6.pack(pady=5, anchor=W,padx = 8)
major6.pack(pady=5, anchor=W,padx = 8)
minor7.pack(pady=5, anchor=W,padx = 8)
major7.pack(pady=5, anchor=W,padx = 8)
octave.pack(pady=5, anchor=W,padx = 8)
playnotes.place(x=140, y=150)
newnotes.place(x=140,y=300)
scaletext.place(x=135, y=50)
keytext.place(x=135,y=75)

###Score

score = 0
score2 = 0

string1 = ('%d out of %d correct' % (score, score2))
string = (score2)

def resetscore():
    global score
    global score2
    global status
    score=0
    score2=0
    status.pack_forget()
    status = Label(root, text=string1, bd=1, relief=SUNKEN, anchor=S)
    status.pack(side=BOTTOM, fill=X)

### Answer

def answer(x):
    global score
    global score2
    global status
    if note2 == x:
        
        generate()
        score +=1
        score2 +=1
        
        status.pack_forget()
        string1 = ('Correct! %d out of %d correct' % (score, score2))
        status = Label(root, text=string1, bd=1, relief=SUNKEN, anchor=S)
        status.pack(side=BOTTOM, fill=X)
        
    else:
        
               
        score2 +=1
        
        status.pack_forget()
        string1 = ('Wrong! %d out of %d correct' % (score, score2))
        status = Label(root, text=string1, bd=1, relief=SUNKEN, anchor=S)
        status.pack(side=BOTTOM, fill=X)



status = Label(root, text=string1, bd=1, relief=SUNKEN, anchor=S)
status.pack(side=BOTTOM, fill=X)
        
root.config(menu=menu, background='black')

###Menu

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Reset score', command=resetscore)
subMenu.add_command(label='Quit', command=quit)

scaleMenu = Menu(menu)
menu.add_cascade(label='Pick Scale', menu=scaleMenu)
scaleMenu .add_radiobutton(label='Even Tempered', command=seteven)
scaleMenu .add_radiobutton(label='Harmonic Series', command=setharmonic)
scaleMenu .add_radiobutton(label='Pythagorean', command=setpythag)

frequencymenu = Menu(menu)
menu.add_cascade(label='Change key', menu=frequencymenu)

frequencymenu.add_radiobutton(label='C (528hz)', command= lambda: changefrequency(528))

frequencymenu.add_radiobutton(label='Db(559hz', command= lambda: changefrequency(559))
frequencymenu.add_radiobutton(label='D (583hz)', command= lambda: changefrequency(583))
frequencymenu.add_radiobutton(label='Eb (628hz)', command= lambda: changefrequency(628))
frequencymenu.add_radiobutton(label='E (665hz)', command= lambda: changefrequency(665))
frequencymenu.add_radiobutton(label='F (705hz)', command= lambda: changefrequency(705))
frequencymenu.add_radiobutton(label='Gb (747hz)', command= lambda: changefrequency(747))
frequencymenu.add_radiobutton(label='G (791hz)', command= lambda: changefrequency(791))
frequencymenu.add_radiobutton(label='Ab (838hz)', command= lambda: changefrequency(838))
frequencymenu.add_radiobutton(label='A (888hz)', command= lambda: changefrequency(888))
frequencymenu.add_radiobutton(label='Bb (941hz)', command= lambda: changefrequency(941))
frequencymenu.add_radiobutton(label='B (997hz)', command= lambda: changefrequency(997))

root.mainloop()
