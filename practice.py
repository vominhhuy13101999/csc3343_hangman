import sys, pygame
pygame.init()
from math import pi
size = width, height = 1000, 800
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()
i=0

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
resize=2
pygame.display.set_caption("Example code for the draw module")
done = False
clock = pygame.time.Clock()
image = pygame.image.load(r'.\download.png')
h, w = image.get_height(),image.get_width()
h_=h*resize*1.5
w_=w*resize
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)
    # Draws the surface object to the screen.
    screen.blit(pygame.transform.scale(image,(w_,h_)),(200,0))
    pygame.display.flip()

  
    pygame.display.update() 
    # Draw on the screen a GREEN line from (0, 0) to (50, 30) 
    # 5 pixels wide.
    pygame.draw.line(screen, WHITE, [200, h_-102], [700,h_-102], 22)
 
    # Draw on the screen 3 BLACK lines, each 5 pixels wide.
    # The 'False' means the first and last points are not connected.
    # pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    
    # Draw on the screen a GREEN line from (0, 50) to (50, 80) 
    # Because it is an antialiased line, it is 1 pixel wide.
    # pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)

    # Draw a rectangle outline
    # pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
     
    # Draw a solid rectangle
    # pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    # Draw a rectangle with rounded corners
    # pygame.draw.rect(screen, GREEN, [115, 210, 70, 40], 10, border_radius=15)
    # pygame.draw.rect(screen, RED, [135, 260, 50, 30], 0, border_radius=10, border_top_left_radius=0,
    #                  border_bottom_right_radius=15)

    # Draw an ellipse outline, using a rectangle as the outside boundaries
    # pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2) 

    # Draw an solid ellipse, using a rectangle as the outside boundaries
    # pygame.draw.ellipse(screen, RED, [300, 10, 50, 20]) 
 
    # This draws a triangle using the polygon command
    # pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
  
    # Draw an arc as part of an ellipse. 
    # Use radians to determine what angle to draw.
    # pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
    # pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
    # pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
    # pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
    
    # Draw a circle
    pygame.draw.circle(screen, BLACK, [320, 430], 38,5,draw_bottom_left=True,
    draw_bottom_right=True,draw_top_left=True, draw_top_right=True)







    pygame.draw.line(screen, BLACK, [320, h_-210], [320,h_-102], 7)


    pygame.draw.line(screen, BLACK, [320, h_-183], [280,h_-217], 7)
    pygame.draw.line(screen, BLACK, [320, h_-102], [280,h_-67], 7)
    pygame.draw.line(screen, BLACK, [320, h_-183], [360,h_-217], 7)
    pygame.draw.line(screen, BLACK, [320, h_-102], [360,h_-67], 7)
    screen.set_at((312, 417), BLACK,)
    screen.set_at((328, 417), BLACK)

    pygame.draw.line(screen, BLACK, [310, 417], [310, 417], 13)
    pygame.draw.line(screen, BLACK, [330, 417], [330, 417], 13)

    pygame.draw.line(screen, BLACK, [320, 441], [310,431], 4)
    # pygame.draw.line(screen, BLACK, [320, 438], [310,448], 4)
    pygame.draw.line(screen, BLACK, [320, 441], [330,431], 4)
    # pygame.draw.line(screen, BLACK, [320,438], [330,448], 4)
    
    # Draw only one circle quadrant
    # pygame.draw.circle(screen, BLUE, [250, 250], 40,  draw_top_right=True)
    # pygame.draw.circle(screen, RED, [250, 250], 40,  draw_top_left=True)
    # pygame.draw.circle(screen, GREEN, [250, 250], 40, 20, draw_bottom_left=True)
    # pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True)
    start=[420,h_]
    blank=10
    for i in range(10):
        pos=start[0]+ 20*i+blank *i
        pygame.draw.line(screen, BLACK, [pos,start[1]], [pos+20,start[1]], 4)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()

# while i<300000:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]

#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()
#     i+=1

