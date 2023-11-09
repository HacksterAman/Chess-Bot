import pyautogui as py
import pyscreenshot as I
import time as T
from PIL import Image
py.FAILSAFE = False

white=(202, 209, 208)
black=(63, 61, 64)
start=(186, 161, 130)
end=(164, 142, 104)
z=[0, 49, 98, 147, 196, 245, 294, 343]
B={'a': 760, 'b': 809, 'c': 858, 'd': 907, 'e': 956, 'f': 1005, 'g': 1054, 'h': 1103, '8': 360, '7': 409, '6': 458, '5': 507, '4': 556, '3': 605, '2': 654, '1': 703}
Bx={0: 'a', 49: 'b', 98: 'c', 147: 'd', 196: 'e', 245: 'f', 294: 'g', 343: 'h'}
By={0: '8', 49: '7', 98: '6', 147: '5', 196: '4', 245: '3', 294: '2', 343: '1'}
W={'h': 760, 'g': 809, 'f': 858, 'e': 907, 'd': 956, 'c': 1005, 'b': 1054, 'a': 1103, '1': 360, '2': 409, '3': 458, '4': 507, '5': 556, '6': 605, '7': 654, '8': 703}
Wx={0: 'h', 49: 'g', 98: 'f', 147: 'e', 196: 'd', 245: 'c', 294: 'b', 343: 'a'}
Wy={0: '1', 49: '2', 98: '3', 147: '4', 196: '5', 245: '6', 294: '7', 343: '8'}
found=False
dictkey={}
dictx={}
dicty={}
startpos=""
startcord=()
endpos=""
move=""
def start(x,y):
    img=I.grab(bbox=(764,362,1156,754))
    for a in z:
        for b in z:
            if x>=a+764 and x<=a+813 and y>=b+362 and y<=a+411 and startpos!=dictx[a]+dicty[b]:
                startcord=(a,b)
                startpos=dictx[a]+dicty[b]
                for c in z:
                    for d in z:
                        if startcord!=(c,d):
                            crop=img.crop((c+5,d+5,c+44,d+44))
                            for i in range(40):
                                for j in range(40):
                                    pix=crop.getpixel((i,j))
                                    if pix[0]==176 or pix[0]==177 and endpos!=dictx[c]+dicty[d]:
                                        endpos=dictx[a]+dicty[b]
                                        newpos()
                                        break
                                else:
                                    continue
                                break
                            break
                    else:
                        continue
                    break
                break
        else:
            continue
        break  
        
def newpos():
    move=startpos+endpos
    print(move)
    
ok=input()       
            
while 1:
    if py.locateCenterOnScreen("Light.png")!=None:
        a,b=py.locateCenterOnScreen("Light.png")
        start(a,b)
    elif py.locateCenterOnScreen("Dark.png")!=None:
        a,b=py.locateCenterOnScreen("Dark.png")
        start(a,b)
        

            
   
           
    
       
            
                
                
        
        
    
    
            
 
        
