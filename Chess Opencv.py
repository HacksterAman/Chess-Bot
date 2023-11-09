import cv2
import numpy as np
import pyautogui as py
from PIL import ImageGrab as S
import time as T
from PIL import Image as I
method = cv2.TM_SQDIFF_NORMED
board='board.png'
white='white.png'
black='black.png'
startD='Dark.png'
startL='Light.png'
Bx={0: 'a', 49: 'b', 98: 'c', 147: 'd', 196: 'e', 245: 'f', 294: 'g', 343: 'h'}
By={0: '8', 49: '7', 98: '6', 147: '5', 196: '4', 245: '3', 294: '2', 343: '1'}
Wx={0: 'h', 49: 'g', 98: 'f', 147: 'e', 196: 'd', 245: 'c', 294: 'b', 343: 'a'}
Wy={0: '1', 49: '2', 98: '3', 147: '4', 196: '5', 245: '6', 294: '7', 343: '8'}
Bfound=False

def match(template):
    loc=py.locateCenterOnScreen(template,grayscale=False,confidence=0.8)
    return loc

def position(x,y):
    for i in dictx:
        if x>i and x<i+49:
            X=i
            Xpos=dictx[i]
            break
    for j in dicty:
        if y>j and y<j+49:
            Y=j
            Ypos=dicty[j]
            break
    pos=Xpos+Ypos
    loc=(X,Y)
    return (pos,loc)

def start():
    global Bfound,startPos
    Bfound=True
    startDloc=match(startD)
    startLloc=match(startL)
    oldPos=(0,0)
    while 1:
        if startDloc!=None:
            x,y=startDloc
            x=x-764
            y=y-362
            newPos=position(x,y)
            if newPos!=oldPos:
                oldPos=newPos
                startPos,startLoc=newPos
                end(startLoc)
        elif startLloc!=None:
            x,y=startLloc
            x=x-764
            y=y-362
            newPos=position(x,y)
            if newPos!=oldPos:
                oldPos=newPos
                startPos,startLoc=newPos
                end(startLoc)


def end(startLoc):
    i,j=startLoc
    try:
        for a in range(3,347,49):
            for x in range(a,44):
                for b in range(3,347,49):
                    if a==i and b==j:
                        continue
                    for y in range(b,44):
                        if py.pixelMatchesColor(x,y,(177,137,78))==True:
                            endpos=position(x,y)[0]
                            print(endpos)
                            raise BreakIt
    except BreakIt:
        pass
                
            
    
while Bfound==False:
    if match(white)!=None and match(black)!=None:
        matchW=match(white)[1]
        matchB=match(black)[1]
        if matchW<558 and matchB>558:
            dictx=Wx
            dicty=Wy
            print("White\n  |\n  |\nBlack")
            start()
        elif matchW>558 and matchB<558:
            dictx=Bx
            dicty=By
            print("Black\n  |\n  |\nWhite")
            start()   
    
