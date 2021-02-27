import pygame
import main
pygame.init()
#button colors
red=(255,0,0)
lightred=(255,102,102)
green=(0,153,0)
lightgreen=(0,204,0)
yellow=(253,253,1)
lightyellow=(255,255,134)
blue=(0,153,153)
lightblue=(0,204,204)
#dis colors
border=(21,107,18)
white=(255,255,255)
dis_width=800
dis_height=600
dis=pygame.display.set_mode((dis_width,dis_height))
font_style = pygame.font.SysFont("bahnschrift", 25)
#pygame.display.set_caption("HIGHSCORE")
f=0
side=20
   
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

   
       
def score():
    f=open("score.txt","r")
    h=f.read()
    f.close() 
    f=0
    while f==0:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                f=1
        dis.fill(white)
        value=font_style.render("HIGHSCORE",True,red)
        dis.blit(value,[350,20])
        value=font_style.render(h,True,red)
        dis.blit(value,[380,35])
        if(buttons("back",350,550,red,lightred,30,15)):print();main.TheHungryPython()          
        pygame.display.update()
    

