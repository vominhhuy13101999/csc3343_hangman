import sys, pygame
from pygame.locals import *
import pandas as pd
import random
import main 
pygame.init()   
from math import pi
size = w, h = 1600, 1000
speed = [2, 2]

screen = pygame.display.set_mode(size, RESIZABLE)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
i=0
text=pd.read_csv("text.txt",header=None).to_numpy().T.tolist()[0]
myfont = pygame.font.SysFont("Times New Roman", 35)

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
PINK=(248, 152, 128)
RED =   (255,   0,   0)
resize=1
pygame.display.set_caption("Example code for the draw module")
done = False
clock = pygame.time.Clock()
image = pygame.image.load(r'hangman2.jpg')
h_=h*resize
w_=w*resize
alphabet= {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

def face(win=1):
    x,y=499, 350

    pygame.draw.line(screen, BLACK, [x-10, y-17], [x-10, y-17], 13)
    pygame.draw.line(screen, BLACK, [x+10, y-17], [x+10, y-17], 13)
    if win:
        pygame.draw.line(screen, BLACK, [x, y+17], [x-7,y+4], 4)
        pygame.draw.line(screen, BLACK, [x, y+17], [x+7,y+4], 4)
    else:
        pygame.draw.line(screen, BLACK, [x, y+17], [x-7,y+30], 4)
        pygame.draw.line(screen, BLACK, [x,y+17], [x+7,y+30], 4)
    # screen.set_at((328, 417), BLACK)

    
def person(position,part=10):
    # Draw a circle
    x,y=499, 350
    if part>=1:
        pygame.draw.circle(screen, BLACK, [499, 350], 50,7,draw_bottom_left=True,
        draw_bottom_right=True,draw_top_left=True, draw_top_right=True)
    if part>=2:
        pygame.draw.line(screen, BLACK, [x, y+175], [x,y+50], 7) 
    if part>=3:

        pygame.draw.line(screen, BLACK, [x, y+175], [x-40,y+227], 7)
    if part>=4:

        pygame.draw.line(screen, BLACK, [x, y+83], [x-40,y+107], 7)
    if part>=5:

        pygame.draw.line(screen, BLACK, [x, y+175], [x+40,y+227], 7)
    if part>=6:

        pygame.draw.line(screen, BLACK, [x, y+83], [x+40,y+107], 7)
    
        screen.set_at((312, 417), BLACK,)

    
    pass
def add(a,n=1):
        b=a
        for _ in range(n):
            b=chr(ord(b)+1)
        return b
def subtract(a,n=1):
    b=a
    for _ in range(n):
        b=chr(ord(b)-1)
    return b
def fill(word,pos):
    label = myfont.render(word, 1, BLACK)
    # put the label object on the screen at point x=100, y=100
    screen.blit(label, (pos[0]+4, pos[1]-40))
    pygame.display.update()
def alpha():
    s= "A   B   C   D   E   F   G   H   I   J  "  
    s1="N   O   P   Q   R   S   T   U   V   W   X   Y   Z "
    label = myfont.render(s, 1, BLACK)

    # put the label object on the screen at point x=100, y=100
    screen.blit(label, (820, 700))
    label = myfont.render(s1, 1, BLACK)
    screen.blit(label, (740, 760))
def blank(n):
    start=[820,550]
    blank=20
    l=[]
    for i in range(n):
        pos=start[0]+ 20*i+blank *i
        l.append((pos,start[1]))
        pygame.draw.line(screen, BLACK, [pos,start[1]], [pos+30,start[1]], 4)
    return l
def eraseEvents():
    pygame.event.set_blocked(pygame.ACTIVEEVENT)
    # pygame.event.set_blocked(pygame.KEYDOWN)
    # pygame.event.set_blocked(pygame.KEYUP)
    pygame.event.set_blocked(pygame.MOUSEMOTION)
def draw(word):
    n=len(word)
    screen.fill(WHITE)
    screen.blit(pygame.transform.scale(image,(1600,1000)),(0,0))
    
    
    
    alpha()
    l=blank(n)
    pygame.display.flip()
    pygame.display.update() 
    return l
def word_to_dic(word):
    d={}
    for i in range(len(word)):
        if word[i] in d:
            d[word[i]].append(i)
        else:
            d[word[i]]=[i]
    return d
def fill_all(char,dic,l):
    for i in dic[char]: 
        fill(char,l[i])
def game_status(s,dic):
    for i in dic:
        if i in s:
            continue
        else:
            return 0
    return 1
def begin():
    screen.fill(WHITE)
    pygame.draw.rect(screen,PINK,pygame.Rect(500, 300, 400, 600))
    instruction_1()
    pygame.display.flip()
    pygame.display.update() 
def end_screen(status):
    pygame.draw.rect(screen,BLUE,pygame.Rect(500, 300, 600, 300))
    
    if status:
        s= "You win! "  
        face(1)
    else:
        s= "You Lose! "
        face(0)
    s1="Press enter to continue"
    s2="Press Esc to got to home screen"

    label = pygame.font.SysFont("Times New Roman", 100).render(s, 1, BLACK)
    screen.blit(label, (720, 310))
    label = myfont.render(s1, 1, BLACK)
    screen.blit(label, (720, 420))
    label = myfont.render(s2, 1, BLACK)
    screen.blit(label, (720, 460))
    pygame.display.flip()
    pygame.display.update()    
def end(status):
    end_screen(status)
    while not False:
        
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(3)
        eraseEvents()
        
        for event in pygame.event.get(): # User did something

            print(event)
            
            if event.type == pygame.QUIT: # If user clicked close
                sys.exit() # Flag that we are done so we exit this loop
            if event.type==pygame.KEYDOWN:
                print(event.__dict__['unicode'])
                key=event.__dict__['unicode']
                if key=="\x1b":
                    return 0
                elif key=="\r":
                    return 1
            if event.type==pygame.VIDEORESIZE:
                end_screen(status)
                pygame.display.flip()
def instruction_1():
    s_0="H A N G M A N"
    label = pygame.font.SysFont("Times New Roman", 100).render(s_0, 1, GREEN)
    screen.blit(label, (350, 100))

    s= "Begin"  
    s1="Instruction"
    s2="Search"
    label = myfont.render(s, 1, BLUE)
    pygame.draw.rect(screen,GREEN,pygame.Rect(580, 400, 180, 50))

    # put the label object on the screen at point x=100, y=100
    screen.blit(label, (600, 400))
    label = myfont.render(s1, 1, BLUE)
    pygame.draw.rect(screen,GREEN,pygame.Rect(580, 550, 180, 50))

    screen.blit(label, (600, 550))
    label = myfont.render(s2, 1, BLUE)
    pygame.draw.rect(screen,GREEN,pygame.Rect(580, 700, 180, 50))

    screen.blit(label, (600, 700))
    pygame.display.flip()
    pygame.display.update()
def instruction_2():
    s="Word  will  be  choosing  random  from  the dictionary"
    s1="you can choose your own bag of word in Search"
    s2="if you  get  wrong  character  new  body part  will  be reveal"
    s3="hit  esc  to  close  any  window,  hit  space  bar  to  choose  word"

    s4="hit  begin  when  you  ready"
    label = myfont.render(s, 1, BLUE)
    pygame.draw.rect(screen,GREEN,pygame.Rect(260, 500, 1100, 250))

    # put the label object on the screen at point x=100, y=100
    screen.blit(label, (300, 520))
    label = myfont.render(s1, 1, BLUE)

    screen.blit(label, (300, 560))
    label = myfont.render(s2, 1, BLUE)

    screen.blit(label, (300, 600))
    label = myfont.render(s3, 1, BLUE)

    screen.blit(label, (300, 640))
    label = myfont.render(s4, 1, BLUE)

    screen.blit(label, (300, 680))
    pygame.display.flip()
    pygame.display.update()
def instruction_3(word="",l=[],bag=set()):
    begin()
    pygame.draw.rect(screen,GREEN,pygame.Rect(34, 390, 300, 40))
    

    label = myfont.render(word, 1, BLUE)
    screen.blit(label, (34, 390))
    pygame.draw.rect(screen,RED,pygame.Rect(34, 430, 300, 300))
    
    x,y=34, 430
    # put the label object on the screen at point x=100, y=100
    for i in range(len(l)):
        
        label = myfont.render(l[i], 1, BLACK)
        screen.blit(label, (x, y+40*(i)))

    pygame.draw.rect(screen,GREEN,pygame.Rect(1066, 390, 300, 340))
    x,y=1066, 390
    i=0
    for j in bag:
        
        label = myfont.render(j, 1, BLACK)
        screen.blit(label, (x, y+40*(i)))
        i+=1
    pygame.display.flip()
    pygame.display.update()
def search_screen():
    pygame.draw.rect(screen,BLUE,pygame.Rect(400, 390, 600, 340))
    x,y=420, 410
    l=["PARALLEL SEARCH (PRESS 1)","BINARY SEARCH (PRESS 2)","AVL SEARCH (PRESS 3)","BF SEARCH (PRESS 4)",]
    for i in range(len(l)):
        
        label = myfont.render(l[i], 1, PINK)
        screen.blit(label, (x, y+80*(i)))
    pygame.display.flip()
    pygame.display.update()
def game(bag):
    i=0
    bag=list(bag)
    if bag:
        word=random.choice(bag)
    else:
        word=random.choice(text)
    print(word)
    l=draw(word)
    d=word_to_dic(word)
    print(d)
    already_set=set()
    part=0
    done=False
    while not done:
        
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(3)
        eraseEvents()
        
        for event in pygame.event.get(): # User did something

            print(event)
            
            if event.type == pygame.QUIT: # If user clicked close
                sys. exit() # Flag that we are done so we exit this loop
            if event.type==pygame.KEYDOWN:
                print(event.__dict__['unicode'])
                key=event.__dict__['unicode']
                if key=='\x1b':
                    begin()
                if key not in alphabet:
                    continue
                if key not in already_set and key in d:
                    fill_all(key,d,l)
                    already_set.add(key)
                elif    key not in already_set and not key in d:
                    part+=1
                    person((0,0),part)
                    already_set.add(key)

                else:
                    pass
                pygame.display.update() 

            if event.type==pygame.VIDEORESIZE:
                
                l=draw(word)
                for i in already_set:
                    if i in d:
                        fill_all(i,d,l)
                person((0,0),part)

        if part>6:
            if game_status(already_set,d):
                face(1)
                print("win")
                return end(1)
                # done=True
            else:
                print("lost")
                # done=True
                a=end(0)
                return a
        else:
            if game_status(already_set,d):
                face(1)
                print("win")
                a=end(1)
                return a

                # done=True


            
        # Clear the screen and set the screen background
        # Draws the surface object to the screen.

        
        
        
        
        pygame.display.flip()  
begin()
bag=set()
while not done:
    clock.tick(3)
    eraseEvents()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
                sys.exit() 
        print(event)
        if event.type==pygame.VIDEORESIZE:
            begin()



        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos=event.__dict__['pos']
            if pos[0]>580 and pos[1]>400 and pos[0]<580+180 and pos[1]<400+50:
                print("one work")
                # done=True
                i=1
                while i:
                    i=game(bag)
                begin()
                continue
        
            if pos[0]>580 and pos[1]>550 and pos[0]<580+180 and pos[1]<550+50:
                instruction_2()
                print("2 work")

                # pygame.display.flip()
                sth=False
                while not sth:
                    clock.tick(3)
                    eraseEvents()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: # If user clicked close
                            sys.exit() 
                        if event.type==pygame.KEYDOWN:
                            key=event.__dict__['unicode']
                            if key=='\x1b':
                                begin()
                                pygame.display.flip()
                                sth=True
        
            if pos[0]>580 and pos[1]>700 and pos[0]<580+180 and pos[1]<700+50:
                
                print("3 work")
                search_screen()
                # pygame.display.flip()
                sth=False
                num=0
                while not sth:
                    clock.tick(3)
                    eraseEvents()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: # If user clicked close
                            sys.exit() 
                        
                        if event.type==pygame.KEYDOWN:
                            key=event.__dict__['unicode']
                            if key=='\x1b':
                                begin()
                                pygame.display.flip()
                                sth=True
                            try:
                                key=int(key)
                            except:
                                continue
                            if key in {1,2,3,4}:
                                num=key
                                sth=True
                if num ==0:
                    continue
                print(num)
                w=""
                l=[]
                bag=set()
                instruction_3()
                sth=False
                while not sth:
                    # print("inhere")
                    clock.tick(3)
                    eraseEvents()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: # If user clicked close
                            sys.exit() 
                        if event.type==pygame.KEYDOWN:
                            key=event.__dict__['unicode']
                            if key=='\x1b':
                                begin()
                                pygame.display.flip()
                                sth=True
                            elif key in alphabet:
                                w+=key
                                
                                l=main.relative_search(w,num)
                                l=main.arrange(w,l)
                                
                                instruction_3(w,l,bag)
                                
                            elif key =="\x08":
                                w=w[:-1]
                                l=main.relative_search(w,num)
                                l=main.arrange(w,l)

                                instruction_3(w,l,bag)
                                

                            elif key ==" ":
                                if key in bag:
                                    pass
                                else:
                                    bag.add(l[0])

                                    instruction_3(w,l,bag)

                                    

                            
            


    pygame.display.flip()

 
# pygame.quit()



