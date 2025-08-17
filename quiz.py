import pyautogui, pgzrun

questions=[]
questioncount=0
questionindex=0

WIDTH,HEIGHT=900,700
TITLE=("Quiz Game")

marqueebox=Rect(0,0,WIDTH,100)
questionbox=Rect(0,0,700,150)
timerbox=Rect(0,0,150,150)
answerbox1=Rect(0,0,340,150)
answerbox2=Rect(0,0,340,150)
answerbox3=Rect(0,0,340,150)
answerbox4=Rect(0,0,340,150)
skipbox=Rect(0,0,150,322.5)

answerboxes=[answerbox1,answerbox2,answerbox3,answerbox4]
questionbox.move_ip(16,120)
timerbox.move_ip(732,120)
answerbox1.move_ip(16,300)
answerbox2.move_ip(372,300)
answerbox3.move_ip(16,470)
answerbox4.move_ip(372,470)
skipbox.move_ip(732,300)

def draw():
    screen.fill("white")
    screen.draw.filled_rect(marqueebox,"white")
    for i in answerboxes:
        screen.draw.filled_rect(i,"lightblue")
    screen.draw.filled_rect(skipbox,"blue")
    screen.draw.filled_rect(questionbox,"darkblue")
    screen.draw.filled_rect(timerbox,"violet")
    screen.draw.textbox(question[0],questionbox,color="white",shadow=(0.25,0.25),scolor="black")
    for i,v in enumerate(answerboxes):
        screen.draw.textbox(question[i+1],v,color="white")



def readfile():
    global questioncount, questions
    qfile=open("quiz.txt","r")
    for i in qfile:
        #print(i)
        questions.append(i)
        questioncount += 1
        #print("")
    #print(questions)
    qfile.close()

def read_next_question():
    global questionindex
    questionindex += 1
    question=questions.pop(0).split(",")
    print(question)
    return question

readfile()

question=read_next_question()

pgzrun.go()