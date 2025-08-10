import pyautogui, pgzrun

WIDTH,HEIGHT=900,700
TITLE=("Quiz Game")

marqueebox=Rect(0,0,WIDTH,100)
questionbox=Rect(0,0,700,150)
timerbox=Rect(0,0,150,150)
answerbox1=Rect(0,0,320,150)
answerbox2=Rect(0,0,320,150)
answerbox3=Rect(0,0,320,150)
answerbox4=Rect(0,0,320,150)
skipbox=Rect(0,0,150,300)

answerboxes=[answerbox1,answerbox2,answerbox3,answerbox4]
questionbox.move_ip(16,120)
timerbox.move_ip(732,120)
answerbox1.move_ip(16,300)
answerbox2.move_ip(352,300)
answerbox3.move_ip(16,470)
answerbox4.move_ip(352,470)
skipbox.move_ip(732,300)

def draw():
    screen.fill("blue")
    screen.draw.filled_rect(marqueebox,"red")
    for i in answerboxes:
        screen.draw.filled_rect(i,"yellow")

pgzrun.go()