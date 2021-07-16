



from tkinter import *
from playsound import playsound
import random

root = Tk()

root.geometry('800x600+400+100')
root.config(bg = 'dark magenta')
root.title('Typing bunny')
root.iconbitmap('C:\\Users\\sheetal\\Downloads\\Python Course with Notes\\python\\project\\assets\\rabbit.ico')
root.maxsize(700,570)
root.minsize(700,570)


score = 0
miss = 0
timeleft = 60



wordlist = ['Amazing',	'Incredible',	'Unbelievable',	'Improbable',	'Astonishing',
'Anger',	'Enrage'	'Infuriate',	'Arouse',	'Nettle',
'Angry',	'Wrathful',	'Furious',	    'Enraged',	'Indignant',
'Answer',	 'Reply',	'Respond',	    'Retort',	'Acknowledge',
'Ask',	     'Question',  'Inquire',	'Query',	'Interrogate',
'Awful',	'Dreadful',	'Terrible',	'Abominable',	'Unpleasant',
'Bad',	'Depraved',	'Rotten',	'Contaminated',	'Sinful',
'Beautiful',	'Gorgeous',	'Dazzling',	'Splendid',	'Magnificent'
'Begin',	'Start',	'Open',	'Launch',	'Initiate', 'coder',
'bunny', 'program', 'Bot']


random.shuffle(wordlist)





def timer():
    global timeleft,score,miss
    
    if(timeleft>0):
        timeleft -= 1
        timerlabel.configure(text= timeleft)
        timerlabel.after(1000,timer)
    else:
        hint.configure(text= 'Hit = {}| MISS = {}| TOTAL SCORE = {}'.format(score,miss,score-miss))



def wordenter (event):
    global score,miss
    if (timeleft == 60):
        timer()
    if (fomtlable.get() == fomtlab['text']):
      score += 1
      scoreLabelok.configure(text= score)


    else:
        miss += 1
    random.shuffle(wordlist)
    fomtlab.configure(text= wordlist[0])
    fomtlable.delete(0,END)









fomtlable = Entry(root,font =('calibri',25), fg = 'dark magenta',bd= 3, justify= 'center')
fomtlable.place(x=190,y=260)
fomtlable.focus_set()



fomtlabl = Label(root, text= 'Welcome to Typing Bunny' ,font =('Alien League',25,'bold'), fg = 'white',bg= 'dark magenta')
fomtlabl.place(x=200,y=50)

fomtlab = Label(root, text= wordlist[0] ,font =('calibri',25), fg = 'white',bg= 'dark magenta')
fomtlab.place(x=300,y=200)






scoreLabel = Label(root,text='Score:',font =(35),fg= 'white',bg = 'dark magenta')
scoreLabel.place(x=10,y = 20)

scoreLabelok = Label(root,text= score ,font =(20),fg= 'white',bg = 'dark magenta')
scoreLabelok.place(x=10,y = 50)





timelabel = Label(root, text ='Timer', font = (35), fg='white' ,bg= 'dark magenta')
timelabel.place(x=650,y=20)

timerlabel = Label(root, text = timeleft,font = (35), fg='white' ,bg= 'dark magenta')
timerlabel.place(x=650,y=50)


hint = Label(root, text ='Just type and hit enter', font = ('Alien League',20), fg='white' ,bg= 'dark magenta')
hint.place(x=220,y=350)



root.bind('<Return>', wordenter)


root.mainloop()
