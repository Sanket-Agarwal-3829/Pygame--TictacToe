import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((600,600))


a = np.array([["_","_","_"],["_","_","_"],["_","_","_"]], dtype = 'str')

def player1 (b , x ,y):
    
    x= (x//200) 
    y=(y//200) 
    b[x,y]="o"
    return b

def player2 (c,x,y):
    
    x= (x//200) 
    y=(y//200) 
    c[x,y]="x"
    return c

#icon and heading 
pygame.display.set_caption('TicTacToe')
icon  = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

turn  = 0
i =0
j=0
font = pygame.font.Font('freesansbold.ttf', 100)
over = pygame.font.Font('freesansbold.ttf', 100)

mx = 64
my= 64
# x
ximg = []
xx=[]
xy=[]
xchange = 0
nofx = 20
for i in range (nofx ):
    ximg.append(pygame.image.load('close.png'))
    xx.append(800)
    xy.append(800)



#o
oimg = []
ox= []
oy=[]
ochange = 0
nofo = 20
for i in range (nofo):
    oimg.append(pygame.image.load('o.png'))
    ox.append(800)
    oy.append(800)




#square
squareinmg = pygame.image.load('square.png')
sx=0
sy=0
sxchange=0
sychange=0

def check (d):
    x=0
    i=0
    j=0
   
    while (i<3):
        if d[i,0] == d[i,2] == d[i,1]== "x" or d[i,0] == d[i,2] == d[i,1]==  "o":
            x=1
            break
        else :
            i= i+1
   
    while (j<3):
        if d[0,j] == d[1,j] == d[2,j]== "x" or d[0,j] == d[1,j] == d[2,j]== "o":
            x=1
            break
        else :
            j+=1
   
    i=0
    j=0
    if d[i,j] == d[(i+1),(j+1)] == d[(i+2),(j+2)]== "x" or d[i,j] == d[(i+1),(j+1)] == d[(i+2),(j+2)]== "o":
        x=1
    if d[i,(j+2)] == d[(i+1),(j+1)] == d[(i+1),(j)]== "x" or  d[i,(j+2)] == d[(i+1),(j+1)] == d[(i+1),(j)]==  "o":
        x=1
    
    return x




def square(x,y):
    screen.blit(squareinmg, (x,y))
def squareright (x):
    x+=200
    return x
def squareup (y):
    y -= 200
    return y
def squaredown (y):
    y+=200
    return y
def squareleft (x):
    x-= 200
    return x
def gameovertxt(a):
    if a%2==0 and a<9:
        p1 = over.render("x wins", True, (255,0,0))
        screen.blit(p1,(150,200))
    elif a%2 !=0 and a<9:
        p2 = over.render("o wins", True, (255,0,0))
        screen.blit(p2,(150,200))
    else:
         overtxt = over.render("draw",True,(255,0,0))
         screen.blit(overtxt, (150 ,200))

def cross (x,y,i):
     
  screen.blit(ximg[i], (x,y))
    
 
def zero (x,y,i):
    screen.blit(oimg[i] ,(x,y))
print(turn)

running = True
while running:
     screen.fill((255,255,255))
     pygame.draw.line(screen, (0,0,0),(400,0),(400,600))
     pygame.draw.line(screen, (0,0,0),(200,0),(200,600))
     pygame.draw.line(screen, (0,0,0),(0,400),(600,400))
     pygame.draw.line(screen, (0,0,0),(0,200),(600,200))
     

     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT and sx <400:
                    sx= squareright(sx)
                    mx = sx + 64
                    
             if event.key == pygame.K_LEFT and sx >0:
                    sx= squareleft(sx)
                    mx = sx + 64
                    
             if event.key == pygame.K_UP and sy >0:
                    sy= squareup(sy)
                    my = sy + 64
             if event.key == pygame.K_DOWN and sy <400:
                    sy= squaredown(sy)
                    my = sy + 64
             if event.key == pygame.K_SPACE and turn <9:
                
                    if turn % 2 ==0:
                        ox[turn] = mx
                        oy[turn] = my 
                        a = player1(a,sx,sy)
                    else:
                        xx[turn] = mx
                        xy[turn] = my
                        a = player2(a,sx,sy)
                    turn +=1
                    

             
     square(sx, sy)      
     
     for i in range(9):
         cross(xx[i], xy[i],i)
         zero(ox[i],oy[i], i)


     d= check(a) 
     if d ==1 or turn > 8:
         gameovertxt(turn)
        

                
                    
                    
               
        
                                                  
                              
                
            
    
     print(turn)
     
     
  
     pygame.display.update()

print(turn)