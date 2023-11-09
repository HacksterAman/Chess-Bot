import pyautogui as py
import pyscreenshot as I
from PIL import Image
x=Image.open("Light.png")
y=x.crop((5,6,48,49))
y.show()
y.save("Light.png")
