import cv2
import pyautogui as py
import pyscreenshot as I
import time as T
from PIL import Image,ImageDraw
import keyboard as key
'''
bx='abcdefgh'
by='87654321'
wx='hgfedcba'
wy='12345678'
dictb={}
dictw={}
X=[789, 838, 887, 936, 985, 1034, 1083, 1132]
Y=[387, 436, 485, 534, 583, 632, 681, 730]

# Range
for x in range(789,1133,49):
    X+=[x]
for y in range(387,731,49):
    Y+=[y]
print(X,Y)

for i in range(8):
    dictb[bx[i]]=X[i]
    dictw[wx[i]]=X[i]
for j in range(8):
    dictb[by[j]]=Y[j] 
    dictw[wy[j]]=Y[j]
print(dictb,dictw)

box=Image.open('box.png')
crop=Image.open('crop.png')
for x in range(5,379,49):
    for y in range(5,379,49):
        box.paste(crop,(x,y))
sbox.save('grid.png')

    for x in range(941,981):
        for y in range(539,579):
            print(pix[x,y])

img=Image.open('screen.png')
grid=Image.open('Grid.png')
img.paste(grid,(0,0),grid)
pix=img.load()
def endPos():
    for a in range(5,379,49):
        for x in range(a,40):
            for b in range(5,379,49):
                for y in range(b,40):
                    if 173<pix[x,y][0]<179:
                        print(x,y)
                        
endPos()
'''
img=Image.open('new.png')
pix=img.load()
for x in range(8,385):
    for y in range(8,385):
        p=pix[x,y]
        if p[0]==176:
            print(p,':',x,y)
