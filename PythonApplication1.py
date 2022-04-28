from bangtal import *
from bangtal import scene

SCENE1 = Scene('VIEW1','images\cam01\cam01.png') #ºä1
SCENE2 = Scene('VIEW2','images\cam02\cam02.png') #ºä2
SCENE3 = Scene('VIEW3','images\cam03\cam03.png') #ºä3
SCENE4 = Scene('VIEW4','images\cam04\cam04.png') #ºä4
SCENE5 = Scene('HIDDEN SPACE','images\cam02\SC5.png') #QR°ø°£
SCENE6 = Scene('PINBOX_BACKSIDE','images\cam03\PINBOX_BACKWARD.png') #ÇÉ¹Ú½º µÞ°ø°£
SCENE7 = Scene('PINBOX','images\cam03\ZOOM1000.png') #ÇÉ¹Ú½º
SCENE8 = Scene('COLOR_PASSWORD','images\cam01\COLOR_PW.png') #ÄÃ·¯ÆÐ½º¿öµå
SCENE9 = Scene('LIGHT','images\cam02\LIGHT.png') #Á¶¸íµÚ


### È­»ìÇ¥
LEFT_ARROW1 = Object('images\LEFT.png')
LEFT_ARROW1.locate(SCENE1,0,0)
LEFT_ARROW1.show()

LEFT_ARROW2 = Object('images\LEFT.png')
LEFT_ARROW2.locate(SCENE2,0,0)
LEFT_ARROW2.show()

LEFT_ARROW3 = Object('images\LEFT.png')
LEFT_ARROW3.locate(SCENE3,0,0)
LEFT_ARROW3.show()

LEFT_ARROW4 = Object('images\LEFT.png')
LEFT_ARROW4.locate(SCENE4,0,0)
LEFT_ARROW4.show()

RIGHT_ARROW1 = Object('images\RIGHT.png')
RIGHT_ARROW1.locate(SCENE1,900,0)
RIGHT_ARROW1.show()

RIGHT_ARROW2 = Object('images\RIGHT.png')
RIGHT_ARROW2.locate(SCENE2,900,0)
RIGHT_ARROW2.show()

RIGHT_ARROW3 = Object('images\RIGHT.png')
RIGHT_ARROW3.locate(SCENE3,900,0)
RIGHT_ARROW3.show()

RIGHT_ARROW4 = Object('images\RIGHT.png')
RIGHT_ARROW4.locate(SCENE4,900,0)
RIGHT_ARROW4.show()

DOWN_ARROW1 = Object('images\DOWN.png')
DOWN_ARROW1.locate(SCENE5,0,0)
DOWN_ARROW1.show()

DOWN_ARROW2 = Object('images\DOWN.png')
DOWN_ARROW2.locate(SCENE6,0,0)
DOWN_ARROW2.show()

DOWN_ARROW3 = Object('images\DOWN.png')
DOWN_ARROW3.locate(SCENE7,0,0)
DOWN_ARROW3.show()

DOWN_ARROW4 = Object('images\DOWN.png')
DOWN_ARROW4.locate(SCENE8,0,0)
DOWN_ARROW4.show()

DOWN_ARROW5 = Object('images\DOWN.png')
DOWN_ARROW5.locate(SCENE9,0,0)
DOWN_ARROW5.show()

##################### ¿ÀºêÁ¦

#NULL-03
YELLOWBOX = Object('images\YELLOWBOX.png')
YELLOWBOX.locate(SCENE1, 120, 230)
YELLOWBOX.show()

#¹®Â¦
DOOR = Object('images\cam01\door_closed.png')
DOOR.locate(SCENE1, 420, 130)
DOOR.show()
DOOR.DOOR_CLOSED = True

#¿­¼è
KEY = Object('images\cam01\KEYOUT.png')
KEYTEM = Object('images\item\key.png')
KEY.locate(SCENE8, 424, 146)

#ºü·ç
TOOL = Object('images\cam02\TOOL.png')
TOOLZOOM = Object('images\item\TOOL_ZOOM.png')
TOOL.locate(SCENE2, 360, 110)
TOOL.show()

#ºä2 ÇÉ
PIN_WIN = Object('images\cam02\PIN_ON.png')
PIN_WIN.locate(SCENE2, 750, 220)
PIN_WIN.APPEAR = True
PIN_WIN.show()

#NULL-01
REDBOX = Object('images\REDBOX.png')
REDBOX.locate(SCENE2, 690, 240)
REDBOX.show()

#³ª¹«Â¦
BLOCK = Object('images\cam02\BLOCKED.png')
BLOCK.locate(SCENE2, 620, 210)
BLOCK.setScale(0.8)
BLOCK.show()
BLOCK.BLOCK_LOCKED = True

#½ºÆÄ¸£Å¸¾×ÀÚ
FRAMEON = Object('images\cam01\FRAME_ON.png')
FRAMEON.locate(SCENE1, 100, 190)
FRAMEON.show()
FRAMEON.FRAME_LOCKED = True

#ÇÉ¹Ú½º
PINBOX1000 = Object('images\cam03\PINBOX1000.png')
PINBOX1100 = Object('images\cam03\PINBOX1100.png')
PINBOX1110 = Object('images\cam03\PINBOX1110.png')
PINBOX1111 = Object('images\cam03\PINBOX1111.png')

ZOOMAABB = Object('images\cam03\ZOOM1.png')
ZOOMAABB.locate(SCENE7, 0,0)
ZOOMABAB = Object('images\cam03\ZOOM2.png')
ZOOMABAB.locate(SCENE7, 0,0)
ZOOMABBA = Object('images\cam03\ZOOM3.png')
ZOOMABBA.locate(SCENE7, 0,0)


PINBOX1000.locate(SCENE3, 490, 100)
PINBOX1000.show()

PINBOXPORTAL = True


#NULL-02
BLUEBOX = Object('images\BLUEBOX.png')
BLUEBOX.locate(SCENE3, 420, 110)
BLUEBOX.show()


#QR ¾Õ ÇÉ
PIN_001 = Object('images\cam02\PIN001.png')
PINTEM1 = Object('images\item\PIN1.png')
PIN_001.locate(SCENE5, 460, 100)
PIN_001.show()

#¹Ú½º µÚ ÇÉ
PIN_002 = Object('images\cam03\PIN_BEHIND.png')
PINTEM2 = Object('images\item\PIN2.png')
PIN_002.locate(SCENE6, 347, 158)
PIN_002.show()

#»ýÀÏ¹Ú½º ÇÉ
PIN_003 = Object('images\cam04\BDPIN.png')
PIN_003.locate(SCENE4, 475, 143)
PINTEM3 = Object('images\item\PIN3.png')

#»ýÀÏ¹Ú½º
BIRTHBOX = Object('images\GREENBOX.png')
BIRTHBOX.locate(SCENE4, 405, 90)
BIRTHBOX.show()

#NULL-04
ORANGEBOX = Object('images\ORANGEBOX.png')
ORANGEBOX.locate(SCENE8, 330, 140)
ORANGEBOX.show()

#»ö±òÂÊÁö
NOTE = Object('images\cam02\QUIZNOTE.png')
NOTE.locate(SCENE9, 460, 180)
NOTETEM = Object('images\item\QUIZNOTE.png')
NOTE.show()

#NULL-05
CYANBOX = Object('images\CYANBOX.png')
CYANBOX.locate(SCENE2, 450, 210)
CYANBOX.show()

#nullboxes
BOX1 = Object('images\BOX1.png')
BOX1.locate(SCENE7, 330, 240)
BOX1.show()
BOX2 = Object('images\BOX2.png')
BOX2.locate(SCENE7, 510, 240)
BOX2.show()
BOX3 = Object('images\BOX3.png')
BOX3.locate(SCENE7, 690, 240)
BOX3.show()

PINVALUE = 0

##### ¾ÆÀÌÅÛ»ç¿ë
def ESCAPE(x, y, action): #Å»Ãâ
    if DOOR.DOOR_CLOSED:
        if KEYTEM.inHand():
            DOOR.setImage('images\cam01\door_opend.png')
            DOOR.DOOR_CLOSED = False
            showAudioPlayer('audio\OPENDOOR.wav')
        else:
            showMessage('THE DOOR IS LOCKED')
            showAudioPlayer('audio\ERROR.wav')
    else:
        endGame()
DOOR.onMouseAction = ESCAPE

def UNBLOCK(x, y, action): #¾À2 ¹æº®ÇØÁ¦
    if BLOCK.BLOCK_LOCKED:
        if TOOLZOOM.inHand():
            BLOCK.setImage('images\cam02\KWAH.png')
            BLOCK.locate(SCENE2, 600, 80)
            showMessage('KWAH-ZIK, tool and boards broken.')
            TOOLZOOM.drop()
            TOOLZOOM.hide()
            BLOCK.BLOCK_LOCKED = False
            showAudioPlayer('audio\01.wav')
        else:
            showMessage('boards are blocking something')
            showAudioPlayer('audio\ERROR.wav')
    else:
        SCENE5.enter()
BLOCK.onMouseAction = UNBLOCK

def PIN_USE1(x, y, action):
    global PINVALUE
    if PINTEM1.inHand():
            ZOOMAABB.show()
            SCENE3.enter()
            showMessage("USE YELLOW PIN")
            PINTEM1.drop()
            PINTEM1.hide()
            BOX1.hide()
            PINVALUE = PINVALUE+1
            showAudioPlayer('audio\PINON.wav')
            print(PINVALUE)
            if PINVALUE == 3:
                FRAMEON.locate(SCENE1, 250, 190)
                showMessage("SOMETHING CHANGED")
                showAudioPlayer('audio\FRAME_ON.wav')
            else:
                FRAMEON.locate(SCENE1, 100, 190)
    else:
        showMessage('NEED YELLOW')
        showAudioPlayer('audio\ERROR.wav')
BOX1.onMouseAction = PIN_USE1

def PIN_USE2(x, y, action):
    global PINVALUE
    if PINTEM2.inHand():
            ZOOMABAB.show()
            SCENE3.enter()
            showMessage("USE RED PIN")
            PINTEM2.drop()
            PINTEM2.hide()
            BOX2.hide()
            PINVALUE = PINVALUE+1
            showAudioPlayer('audio\PINON.wav')
            print(PINVALUE)
            if PINVALUE == 3:
                FRAMEON.locate(SCENE1, 250, 190)
                showMessage("SOMETHING CHANGED")
                showAudioPlayer('audio\FRAME_ON.wav')
            else:
                FRAMEON.locate(SCENE1, 100, 190)
    else:
        showMessage('NEED RED PIN')
        showAudioPlayer('audio\ERROR.wav')

BOX2.onMouseAction = PIN_USE2

def PIN_USE3(x, y, action):
    global PINVALUE
    if PINTEM3.inHand():
            ZOOMABBA.show()
            SCENE3.enter()
            showMessage("USE GREEN PIN")
            PINTEM3.drop()
            PINTEM3.hide()
            BOX3.hide()
            PINVALUE = PINVALUE+1
            showAudioPlayer('audio\PINON.wav')
            print(PINVALUE)
            if PINVALUE == 3:
                FRAMEON.locate(SCENE1, 250, 190)
                showMessage("SOMETHING CHANGED")
                showAudioPlayer('audio\FRAME_ON.wav')
            else:
                FRAMEON.locate(SCENE1, 100, 190)
    else:
        showMessage('NEED GREEN PIN')
        showAudioPlayer('audio\ERROR.wav')
BOX3.onMouseAction = PIN_USE3


#Æ÷Å»
def SC5_ENTER(x, y, action):
    SCENE5.enter()
REDBOX.onMouseAction = SC5_ENTER
def SC6_ENTER(x, y, action):
    SCENE6.enter()
BLUEBOX.onMouseAction = SC6_ENTER
def SC7_ENTER(x, y, action):
        SCENE7.enter()
PINBOX1000.onMouseAction = SC7_ENTER
def SC8_ENTER(x, y, action):
    SCENE8.enter()
YELLOWBOX.onMouseAction = SC8_ENTER
def SC9_ENTER(x, y, action):
    SCENE9.enter()
CYANBOX.onMouseAction = SC9_ENTER




###### ¾ÆÀÌÅÛ È¹µæ
def KEY_OBTAIN(x, y, action): # ¿­¼è½Àµæ
    KEY.setImage=('images\item\key.png')
    showAudioPlayer('audio\OBTAIN.wav')
    KEYTEM.pick()
    KEY.hide()
KEY.onMouseAction = KEY_OBTAIN
def TOOL_OBTAIN(x, y, action): # ºü·ç½Àµæ
    TOOL.setImage=('images\item\TOOL_ZOOM.png')
    showAudioPlayer('audio\OBTAIN.wav')
    TOOLZOOM.pick()
    TOOL.hide()
TOOL.onMouseAction = TOOL_OBTAIN
def PIN001_OBTAIN(x, y, action): # PIN001 ½Àµæ
    showAudioPlayer('audio\OBTAIN.wav')
    PIN_001.setImage=('images\item\PIN2.png')
    PINTEM1.pick()
    PIN_WIN.locate(SCENE5,900,900)
    PIN_001.hide()
PIN_001.onMouseAction = PIN001_OBTAIN
def PIN002_OBTAIN(x, y, action): # PIN002 ½Àµæ
    showAudioPlayer('audio\OBTAIN.wav')
    PIN_002.setImage=('images\item\PIN1.png')
    PINTEM2.pick()
    PIN_002.hide()
PIN_002.onMouseAction = PIN002_OBTAIN
def PIN003_OBTAIN(x, y, action): # PIN003 ½Àµæ
    showAudioPlayer('audio\OBTAIN.wav')
    PIN_003.setImage=('images\item\PIN3.png')
    PINTEM3.pick()
    PIN_003.hide()
PIN_003.onMouseAction = PIN003_OBTAIN
def NOTE_OBTAIN(x, y, action): # QUIZNOTE ½Àµæ
    showAudioPlayer('audio\OBTAIN.wav')
    NOTE.setImage=('images\item\QUIZNOTE.png')
    NOTETEM.pick()
    NOTE.hide()
NOTE.onMouseAction = NOTE_OBTAIN




############## È­¸éÀÌµ¿
def VIEW_LEFT1(x, y, action):
    SCENE2.enter()
    showAudioPlayer('audio\MOVE.wav')
LEFT_ARROW1.onMouseAction = VIEW_LEFT1
def VIEW_LEFT2(x, y, action):
    SCENE3.enter()
    showAudioPlayer('audio\MOVE.wav')
LEFT_ARROW2.onMouseAction = VIEW_LEFT2
def VIEW_LEFT3(x, y, action):
    SCENE4.enter()
    showAudioPlayer('audio\MOVE.wav')
LEFT_ARROW3.onMouseAction = VIEW_LEFT3
def VIEW_LEFT4(x, y, action):
    SCENE1.enter()
    showAudioPlayer('audio\MOVE.wav')
LEFT_ARROW4.onMouseAction = VIEW_LEFT4
def VIEW_RIGHT1(x, y, action):
    SCENE4.enter()
    showAudioPlayer('audio\MOVE.wav')
RIGHT_ARROW1.onMouseAction = VIEW_RIGHT1
def VIEW_RIGHT2(x, y, action):
    SCENE3.enter()
    showAudioPlayer('audio\MOVE.wav')
RIGHT_ARROW4.onMouseAction = VIEW_RIGHT2
def VIEW_RIGHT3(x, y, action):
    SCENE2.enter()
    showAudioPlayer('audio\MOVE.wav')
RIGHT_ARROW3.onMouseAction = VIEW_RIGHT3
def VIEW_RIGHT4(x, y, action):
    SCENE1.enter()
    showAudioPlayer('audio\MOVE.wav')
RIGHT_ARROW2.onMouseAction = VIEW_RIGHT4

#µÚ·Î°¡±â
def VIEW_BACK1(x, y, action):
    SCENE2.enter()
    showAudioPlayer('audio\MOVE.wav')
DOWN_ARROW1.onMouseAction = VIEW_BACK1
def VIEW_BACK2(x, y, action):
    showAudioPlayer('audio\MOVE.wav')
    SCENE3.enter()
DOWN_ARROW2.onMouseAction = VIEW_BACK2
def VIEW_BACK3(x, y, action):
    showAudioPlayer('audio\MOVE.wav')
    SCENE3.enter()
DOWN_ARROW3.onMouseAction = VIEW_BACK3
def VIEW_BACK4(x, y, action):
    showAudioPlayer('audio\MOVE.wav')
    SCENE1.enter()
DOWN_ARROW4.onMouseAction = VIEW_BACK4
def VIEW_BACK5(x, y, action):
    showAudioPlayer('audio\MOVE.wav')
    SCENE2.enter()
DOWN_ARROW5.onMouseAction = VIEW_BACK5



########## ÆÐ½º¿öµå
def BIRTHDAY(x,y,action):
    showKeypad('1107', BIRTHBOX)
BIRTHBOX.onMouseAction = BIRTHDAY
def BD_PADON():
    showMessage("CORRECT")
    PIN_003.show()
    BIRTHBOX.setScale(0.01)
    BIRTHBOX.locate(SCENE4,900,900)
BIRTHBOX.onKeypad = BD_PADON
def COLORPAD(x,y,action):
    showMessage("RED...YELLOW...BLUE...GREEN?")
    showKeypad('5734', ORANGEBOX)
ORANGEBOX.onMouseAction = COLORPAD
def COLORPAD_CORRECT():
    showMessage("CORRECT")
    ORANGEBOX.hide()
    ORANGEBOX.setScale(0.01)
    ORANGEBOX.locate(SCENE8,900,900)
    KEY.show()
ORANGEBOX.onKeypad = COLORPAD_CORRECT


startGame(SCENE1)
