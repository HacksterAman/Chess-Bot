import pyautogui as py
py.FAILSAFE=False
import time as T
import keyboard as key
from stockfish import Stockfish
from PIL import Image,ImageGrab
S=Stockfish(r'C:\Users\amams\OneDrive\Desktop\Chess\stockfish_13_win_x64_bmi2\stockfish_13_win_x64_bmi2.exe')
Bx={0: 'a', 49: 'b', 98: 'c', 147: 'd', 196: 'e', 245: 'f', 294: 'g', 343: 'h'}
By={0: '8', 49: '7', 98: '6', 147: '5', 1196: '4', 245: '3', 294: '2', 343: '1'}
Wx={0: 'h', 49: 'g', 98: 'f', 147: 'e', 196: 'd', 245: 'c', 294: 'b', 343: 'a'}
Wy={0: '1', 49: '2', 98: '3', 147: '4', 196: '5', 245: '6', 294: '7', 343: '8'}
dictB={'a': 789, 'b': 838, 'c': 887, 'd': 936, 'e': 985, 'f': 1034, 'g': 1083, 'h': 1132, '8': 387, '7': 436, '6': 485, '5': 534, '4': 583, '3': 632, '2': 681, '1': 730}
dictW={'h': 789, 'g': 838, 'f': 887, 'e': 936, 'd': 985, 'c': 1034, 'b': 1083, 'a': 1132, '1': 387, '2': 436, '3': 485, '4': 534, '5': 583, '6': 632, '7': 681, '8': 730}
moves=[]
dictx={}
dicty={}
dictC={}

def match(template):
    loc=py.locateCenterOnScreen(template,confidence=0.5)
    return loc

def end():
    img=ImageGrab.grab(bbox=(764,362,1156,754))
    grid=Image.open('Grid.png')
    img.paste(grid,(0,0),grid)
    pix=img.load()
    for x in range(0,392):
        for y in range(0,392):
            p=pix[x,y]
            if 176<p[0]<179 and 135<p[1]<139:
                return position(x,y,False)
                        
def position(x,y,s=True):
    if s:
        x-=764
        y-=362
    for i in dictx:
        if x>i and x<i+49:
            Xpos=dictx[i]
            break
    for j in dicty:
        if y>j and y<j+49:
            Ypos=dicty[j]
            break
    pos=Xpos+Ypos
    return pos
   
def clicker():
    global moves
    move=S.get_best_move_time(1000)
    print('Computer:'+move)
    moves+=[move]
    S.set_position(moves)
    Loc=[]
    for i in move:
        Loc+=[dictC[i]]
    py.click(x=Loc[0],y=Loc[1])
    T.sleep(0.1)
    py.click(x=Loc[2],y=Loc[3])

def getMove():
    global moves
    while True:
        if key.is_pressed('0'):
            startMatch=match('Light.png')
            while startMatch==None:
                startMatch=match('Light.png')
            x,y=startMatch
            startPos=position(x,y)
            endPos=end()
            move=startPos+endPos
            print('You:'+move)
            moves+=[move]
            S.set_position(moves)
            clicker()

white='white.png'
black='black.png'
moves=[]
while True:
    if match(white)!=None and match(black)!=None:
        print('New Game')
        matchW=match(white)[1]
        matchB=match(black)[1]
        if matchW<558 and matchB>558:
            dictx=Wx
            dicty=Wy
            dictC=dictW
            print("White\n  |\n  |\nBlack")
            getMove()
            break
        elif matchW>558 and matchB<558:
            dictx=Bx
            dicty=By
            dictC=dictB
            print("Black\n  |\n  |\nWhite")
            clicker()
            getMove()
            break  
