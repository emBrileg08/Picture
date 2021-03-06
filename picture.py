"""
picture.py
Author: emBrileg08
Credit: www.colorhexa.com for the color hexadecimals

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects. Done
2. Ten different Sprite objects. 7/10
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects. Done
5. One (or more) EllipseAsset objects. Done
6. One (or more) PolygonAsset objects.Done

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

black= Color(0x000000, 1.0)
peach= Color(0xffe0bd, 1.0)
brown= Color(0x654321, 1.0)
red= Color(0xff0000, 1.0)
mouthred= Color(0xff0000,0.25)
thinline = LineStyle(1, black)
mouthline= LineStyle (4, red)

face=EllipseAsset(136, 160, thinline, peach)
pupil=CircleAsset(10, thinline, brown)
mouth=CircleAsset(20,mouthline,mouthred)
eyebrow=RectangleAsset(30,2,thinline,brown)
nose=PolygonAsset([(0,0),(25,25),(-25,25),(0,0)],thinline,peach)
nosebridge=PolygonAsset([(0,0),(0,45)],thinline,black)
hatbrim=RectangleAsset(250,25,thinline,brown)
hat=PolygonAsset([(0,0),(60,-60),(120,-60),(180,0),(0,0)],thinline,brown)

Sprite(face, (160,160))
Sprite(pupil, (220,260))
Sprite(pupil, (350, 260))
Sprite(mouth, (280, 400))
Sprite(eyebrow, (220,230))
Sprite (eyebrow, (340,230))
Sprite(nose,(272,310))
Sprite(nosebridge,(273,290))
Sprite(nosebridge,(323,290))
Sprite(hatbrim, (170,150))
Sprite(hat, (205,90))


# add your code here /\  /\  /\


myapp = App()
myapp.run()
