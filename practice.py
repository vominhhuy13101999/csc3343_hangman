import sys, pygame
from pygame.locals import *

pygame.init()
from math import pi
size = w, h = 1600, 1000
speed = [2, 2]

screen = pygame.display.set_mode(size, RESIZABLE)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
i=0
myfont = pygame.font.SysFont("Times New Roman", 35)

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
resize=1
pygame.display.set_caption("Example code for the draw module")
done = False
clock = pygame.time.Clock()
image = pygame.image.load(r'.\hangman2.jpg')

h_=h*resize
w_=w*resize
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
    
    person((0,0))
    face(1)
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
i=0
word="magnuscarlsen"
l=draw(word)
d=word_to_dic(word)
print(d)
alphabet= {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
already_set=set()
memory=[]
while not done:
    
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(3)
    eraseEvents()

    for event in pygame.event.get(): # User did something

        print(event)
        
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        if event.type==pygame.KEYDOWN:
            print(event.__dict__['unicode'])
            key=event.__dict__['unicode']
            if key not in already_set and key in d:
                fill_all(key,d,l)
                already_set.add(key)
                
            
            pygame.display.update() 
        if event.type==pygame.VIDEORESIZE:
            
            l=draw(word)

    # Clear the screen and set the screen background
    # Draws the surface object to the screen.


    
    
    
    
    pygame.display.flip()
 
pygame.quit()



