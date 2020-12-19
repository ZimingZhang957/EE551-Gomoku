import pygame
from pygame.locals import *
import sys
import traceback
import copy

pygame.init()
pygame.mixer.init()

#color
background=(222,184,135)
checkerboard=(80,80,80)
button=(80,80,80)
tips=[(0,0,0),(255,255,255),(255,215,0)]
tips_i=1


#Draw chessboard
def Draw_a_chessboard(screen):  
    #Fill color
    screen.fill(background)
    #Draw the chessboard
    for i in range(21):
        pygame.draw.line(screen, checkerboard, (40*i+3, 3), (40*i+3, 803)) 
        pygame.draw.line(screen, checkerboard, (3, 40*i+3), (803, 40*i+3))
    #Draw the line
    pygame.draw.line(screen, checkerboard, (3, 3), (803, 3),5)   
    pygame.draw.line(screen, checkerboard, (3, 3), (3, 803),5)   
    pygame.draw.line(screen, checkerboard, (803, 3), (803, 803),5)   
    pygame.draw.line(screen, checkerboard, (3, 803), (803, 803),5) 
     
    
    #draw "Withdraw" "Restart" "Quit" button
    s_font=pygame.font.Font('FFF.ttf',40)
    text1=s_font.render("Withdraw",True,button)
    text2=s_font.render("Restart",True,button)
    text3=s_font.render("Quit",True,button)
    screen.blit(text1,(920,370))
    screen.blit(text2,(920,520))
    screen.blit(text3,(920,670))

#Draw chess stones
def Draw_a_chessman(x,y,screen,color):    
    if color==1:        
        Black_chess=pygame.image.load("Black_chess.png").convert_alpha()
        screen.blit(Black_chess,(40*x+3-15,40*y+3-15))
    if color==2:
        White_chess=pygame.image.load("White_chess.png").convert_alpha()
        screen.blit(White_chess,(40*x+3-15,40*y+3-15))

#Draw the chessboard with stones
def Draw_a_chessboard_with_chessman(map,screen):  
    screen.fill(background)
    Draw_a_chessboard(screen)
    for i in range(24):
        for j in range(24):
            Draw_a_chessman(i+1,j+1,screen,map[i][j])



#Define the list of stored chessboards
map=[]
for i in range(24):
    map.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#Clear list
def clear():
    global map
    for i in range(24):
        for j in range(24):
            map[i][j]=0

#Judging game victory
def win(i, j):
    k = map[i][j]
    p=[]
    for a in range(20):
        p.append(0)
    for i3 in range(i-4,i+5):
        for j3 in range(j-4,j+5):
            if (map[i3][j3] == k and i3 - i == j3 - j and i3 <= i and j3 <= j):
                p[0]+=1
            if (map[i3][j3] == k and j3 == j and i3 <= i and j3 <= j):
                p[1]+=1
            if (map[i3][j3] == k and i3 == i and i3 <= i and j3 <= j):
                p[2]+=1
            if (map[i3][j3] == k and i3 - i == j3 - j and i3 >= i and j3 >= j):
                p[3]+=1
            if (map[i3][j3] == k and j3 == j and i3 >= i and j3 >= j):
                p[4]+=1
            if (map[i3][j3] == k and i3 == i and i3 >= i and j3 >= j):
                p[5]+=1
            if (map[i3][j3] == k and i - i3 == j3 - j and i3 <= i and j3 >= j):
                p[6]+=1
            if (map[i3][j3] == k and i3 - i == j - j3 and i3 >= i and j3 <= j):
                p[7]+=1
            if (map[i3][j3] == k and j - j3 == i - i3 and i3 <= i + 1  and  i3 >= i - 3  and  j3 <= j + 1  and  j3 >= j - 3):
                p[8]+=1
            if (map[i3][j3] == k and j == j3 and i3 <= i + 1  and  i3 >= i - 3  and  j3 <= j + 1  and  j3 >= j - 3):
                p[9]+=1
            if (map[i3][j3] == k and i == i3 and i3 <= i + 1  and  i3 >= i - 3  and  j3 <= j + 1  and  j3 >= j - 3):
                p[10]+=1
            if (map[i3][j3] == k and j - j3 == i - i3 and i3 >= i - 1  and  i3 <= i + 3  and  j3 >= j - 1  and  j3 <= j + 3):
                p[11]+=1
            if (map[i3][j3] == k and j == j3 and i3 >= i - 1  and  i3 <= i + 3  and  j3 >= j - 1  and  j3 <= j + 3):
                p[12]+=1
            if (map[i3][j3] == k and i == i3 and i3 >= i - 1  and  i3 <= i + 3  and  j3 >= j - 1  and  j3 <= j + 3):
                p[13]+=1
            if (map[i3][j3] == k and i - i3 == j3 - j and i3 <= i + 1  and  i3 >= i - 3  and  j3 >= j - 1  and  j3 <= j + 3):
                p[14]+=1
            if (map[i3][j3] == k and i3 - i == j - j3 and i3 >= i - 1  and  i3 <= i + 3  and  j3 <= j + 1  and  j3 >= j - 3):
                p[15]+=1
            if (map[i3][j3] == k and j - j3 == i - i3 and i3 <= i + 2  and  i3 >= i - 2  and  j3 <= j + 2  and  j3 >= j - 2):
                p[16]+=1
            if (map[i3][j3] == k and j == j3 and i3 <= i + 2  and  i3 >= i - 2  and  j3 <= j + 2  and  j3 >= j - 2):
                p[17]+=1
            if (map[i3][j3] == k and i == i3 and i3 <= i + 2  and  i3 >= i - 2  and  j3 <= j + 2  and  j3 >= j - 2):
                p[18]+=1
            if (map[i3][j3] == k and i - i3 == j3 - j and i3 <= i + 2  and  i3 >= i - 2  and  j3 <= j + 2  and  j3 >= j - 2):
                p[19]+=1
    for b in range(20):
        if p[b]==5:
            return True
    return False

#Draw the tips
def text(s,screen,x):
    #cover
    pygame.draw.rect(screen,background,[850,100,1200,100])

    s_font=pygame.font.Font('FFF.ttf',x)
    s_text=s_font.render(s,True,tips[tips_i])
    screen.blit(s_text,(880,100))
    pygame.display.flip()


t=True
#Determine if the game is in progress
running=True

#main
def main():

    global t,map,running,maps,r,h
    clear()
    map2=copy.deepcopy(map)
    maps=[map2]

    
    #Define window
    screen = pygame.display.set_mode([1200,806])
    pygame.display.set_caption("Gomoku")
    
    #Draw the chessboard, tips and buttons in the window
    Draw_a_chessboard(screen)
    pygame.display.flip()
    clock=pygame.time.Clock()
    while True:
        
        if running:
            if t:
                color=1
                global tips_i
                tips_i=0
                text('Black Stone',screen,50)
            else:
                color=2
                tips_i=1
                text('White Stone',screen,50)
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Instruction
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y=event.pos[0],event.pos[1]
                    for i in range(19):
                        for j in range(19):
                            #Click on the board
                            if i*40+3+20<x<i*40+3+60 and j*40+3+20<y<j*40+3+60 and not map[i][j] and running:
                                Draw_a_chessman(i+1,j+1,screen,color)
                                #Record the position of the stones
                                map[i][j]=color

                                map3=copy.deepcopy(map)
                                maps.append(map3)

                                #Determine whether 5 stones in a row
                                if win(i,j):
                                    if t:
                                        tips_i=2
                                        text('Black Win!',screen,50)
                                    else:
                                        tips_i=2
                                        text('White Win!',screen,50)
                                    #Prevent adding stones
                                    running=False
                                pygame.display.flip()
                                t=not t
                    #Click "Restart"
                    if 900<x<1100 and 500<y<600:
                        running=True
                        main()
                    
                    #Click "Quit"
                    elif 900<x<1000 and 650<y<750:
                        pygame.quit()
                        sys.exit()
 
                    #Click "Withdraw"
                    elif 900<x<1200 and 350<y<450 and len(maps)!=1:
                        del maps[len(maps)-1] 
                        map=copy.deepcopy(maps[len(maps)-1])
                        t=not t
                        Draw_a_chessboard_with_chessman(map,screen)
                        #Prevent consecutive withdraws
                        x,y=0,0
        clock.tick(60)
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
