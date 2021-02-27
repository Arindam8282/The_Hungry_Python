import pygame
import os
import time
import random
pygame.init()
co=0
border=(0,51,51)
border1=(102,102,0)
white = (255, 255, 255)
black = (0, 0, 0)
#button colors
red=(204,0,0)
lightred=(255,102,102)
green=(0,153,0)
lightgreen=(0,204,0)
yellow=(253,253,1)
lightyellow=(255,255,134)
blue=(0,153,153)
lightblue=(0,204,204)
#display colors
displaycolors=[(102,0,0),(102,51,0),(51,102,0),(0,102,102),(96,96,96),(0,204,102)]
snakecolors=[(255,182,0),(0,255,255),(255,0,255),(255,20,229),(224,224,224),(255,255,51),(255,178,102)]
dis_width = 800
dis_height = 600
side=20
dis = pygame.display.set_mode((dis_width, dis_height))
#icon=pygame.image.load("scared.png")
#pygame.display.set_icon(icon)
pygame.display.set_caption('The Hungry Python')
bg=pygame.image.load("pic1.png")
helppic=pygame.image.load("cursor.png")
clock = pygame.time.Clock()
#step jumping
snake_block = 20
#snake jump
font_style = pygame.font.SysFont("bahnschrift", 25)
game_over=pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("arial", 17)
    
def randcolor(color,length):
    return color[random.randint(0,length-1)]
def randfoodclr():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [380,0]) 
def our_snake(snake_block, snake_list,snkclr):
    for x in snake_list:
        pygame.draw.rect(dis,snkclr, [x[0], x[1], snake_block, snake_block])
        pygame.draw.rect(dis,randfoodclr(),[x[0]+9,x[1]+13,3,3])
        pygame.draw.rect(dis,randfoodclr(),[x[0]+6,x[1]+9,3,3])
        pygame.draw.rect(dis,randfoodclr(),[x[0]+10,x[1]+15,3,3])
        pygame.draw.rect(dis,randfoodclr(),[x[0]+13,x[1]+15,3,3])
        pygame.draw.rect(dis,randfoodclr(),[x[0]+4,x[1]+15,3,3])
    pygame.draw.rect(dis,snkclr, [x[0], x[1], snake_block, snake_block])
    pygame.draw.rect(dis,black,[x[0]+5,x[1]+5,4,4])
    pygame.draw.rect(dis,black,[x[0]+15,x[1]+5,4,4])    
 
def message(msg, color,w,h):
    mesg = game_over.render(msg, True,color)
    dis.blit(mesg,[w,h])
 
def foodloc():
    width=round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    height=round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
    if((width>20 and width<780) and (height>20 and height<580)):return width,height
    else:return foodloc()
def borders():
    for i in range(0,dis_width-(side-1),side):pygame.draw.rect(dis,border,(i,0,side,side));pygame.draw.rect(dis,border,(i,dis_height-side,side,side))
    for i in range(0,dis_height-(side-1),side):pygame.draw.rect(dis,border,(dis_width-side,i,side,side));pygame.draw.rect(dis,border,(0,i,side,side))
    for j in range(0,21,20):
        for i in range(0,dis_width-1,1):pygame.draw.rect(dis,border1,(i,j,1,1))
    for j in range(0,580,50):
        for i in range(0,20,1):pygame.draw.rect(dis,border1,(i,j,1,1))
        for i in range(780,800,1):pygame.draw.rect(dis,border1,(i,j,1,1))
    for j in range(580,601,19):
        for i in range(0,dis_width-1,1):pygame.draw.rect(dis,border1,(i,j,1,1))
    for j in range(0,20):
        for i in range(20,780,39):pygame.draw.rect(dis,border1,(i,j,1,1))
    for j in range(580,600):
        for i in range(20,780,39):pygame.draw.rect(dis,border1,(i,j,1,1))
    for i in range(0,dis_height-1,1):pygame.draw.rect(dis,border1,(0,i,1,1));pygame.draw.rect(dis,border1,(19,i,1,1))
    for i in range(0,dis_height-1,1):pygame.draw.rect(dis,border1,(780,i,1,1));pygame.draw.rect(dis,border1,(799,i,1,1))
def buttons(text,posw,posh,color1,color2,w,h):
    value=font_style.render(text,True,white)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if posw+100>mouse[0]>posw and posh+50>mouse[1]>posh:
        pygame.draw.rect(dis,color2,[posw,posh,100,50])
        dis.blit(value,[posw+w,posh+h])
        if(click[0]==1):return True
        else:return False
    else:pygame.draw.rect(dis,color1,[posw,posh,100,50]);dis.blit(value,[posw+w,posh+h]);return False
def gameover(l,h):
    message("Game over", lightred,360,300)
    if h!='':h=l-1 if l>int(h) else h
    else:h=l-1
    f=open("score.txt","w")
    f.write(str(h))
    f.close()
    message("highscore - "+str(h),lightyellow,360,320)
    Your_score(l- 1)
    if(buttons("back",300,400,red,lightred,30,15)):TheHungryPython()
    if(buttons("retry",420,400,green,lightgreen,30,15)):play(h)
    pygame.display.update()

def play(highscore):
    snake_speed=5
    score_check=5
    discolor=randcolor(displaycolors,6)
    game_over = False
    game_close = False
    snakecolor=snakecolors[random.randint(0,6)]
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    foodx,foody=foodloc()
 
    while not game_over:
 
        while game_close == True:
            gameover(Length_of_snake,highscore)
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= (dis_width-side) or x1 < 20 or y1 >= (dis_height-side) or y1 < 20:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(discolor)
        borders()
        pygame.draw.rect(dis, randfoodclr(), [foodx, foody,snake_block,snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List,snakecolor)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx,foody=foodloc()
            Length_of_snake += 1
        if Length_of_snake >score_check:snake_speed+=2;score_check+=5
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()

def TheHungryPython():
    os.system("exit")
    f=open("score.txt","r")
    highscore=f.read()
    f.close()
    f=h=0
    while f==0:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                f=1
        dis.fill(white)
        dis.blit(bg,(20,0))
        if(buttons("play",100,200,green,lightgreen,30,15)):play(highscore)
        if(buttons("exit",600,200,red,lightred,30,15)):pygame.quit()
        if(buttons("highscore",100,300,yellow,lightyellow,10,15)):import score;score.score()
        if(buttons("help",600,300,blue,lightblue,30,15)):import helpg;helpg.helpg()
        pygame.display.update()
        clock.tick(10)
        pygame.display.flip()
 

