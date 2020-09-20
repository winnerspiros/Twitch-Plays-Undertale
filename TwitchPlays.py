import time, subprocess, ctypes, random, string, re, sys, TwitchPlays_Connection, pyautogui, pynput
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN
from pynput.mouse import Button, Controller
SendInput = ctypes.windll.user32.SendInput
def PressKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def ReleaseKeyPynput(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.ki = pynput._util.win32.KEYBDINPUT(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x = pynput._util.win32.INPUT(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def PressAndHoldKey(hexKeyCode, seconds):
    PressKeyPynput(hexKeyCode)
    time.sleep(seconds)
    ReleaseKeyPynput(hexKeyCode)
mouse = Controller()
Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32
ESC = 0x01
ONE = 0x02
TWO = 0x03
THREE = 0x04
FOUR = 0x05
FIVE = 0x06
SIX = 0x07
SEVEN = 0x08
EIGHT = 0x09
NINE = 0x0A
ZERO = 0x0B
MINUS = 0x0C
EQUALS = 0x0D
BACKSPACE = 0x0E
SEMICOLON = 0x27
TAB = 0x0F
CAPS = 0x3A
ENTER = 0x1C
LEFT_CONTROL = 0x1D
LEFT_ALT = 0x38
LEFT_SHIFT = 0x2A
SPACE = 0x39
DELETE = 0x53
COMMA = 0x33
PERIOD = 0x34
BACKSLASH = 0x35
NUMPAD_0 = 0x52
NUMPAD_1 = 0x4F
NUMPAD_2 = 0x50
NUMPAD_3 = 0x51
NUMPAD_4 = 0x4B
NUMPAD_5 = 0x4C
NUMPAD_6 = 0x4D
NUMPAD_7 = 0x47
NUMPAD_8 = 0x48
NUMPAD_9 = 0x49
NUMPAD_PLUS = 0x4E
NUMPAD_MINUS = 0x4A
LEFT_ARROW = 0xCB
RIGHT_ARROW = 0xCD
UP_ARROW = 0xC8
DOWN_ARROW = 0xD0
LEFT_MOUSE = 0x100
RIGHT_MOUSE = 0x101
MIDDLE_MOUSE = 0x102
MOUSE3 = 0x103
MOUSE4 = 0x104
MOUSE5 = 0x105
MOUSE6 = 0x106
MOUSE7 = 0x107
MOUSE_WHEEL_UP = 0x108
MOUSE_WHEEL_DOWN = 0x109
COMA = 0x33
RIGHT_SHIFT = 0x36
t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN);
while True:
    new_messages = t.twitch_recieve_messages();
    if not new_messages:
        continue
    else:
        try:  
            for message in new_messages:
                msg = message['message'].lower()
                username = message['username'].lower()

                if msg in ['up', 'u', 'forward', 'go up']:
                    PressKeyPynput(UP_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['tap up', 'micro up', 'tap u', 'micro u']:
                    PressKeyPynput(UP_ARROW)
                    time.sleep(0.1)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['tap up left', 'micro up left', 'tap ul', 'micro ul', 'tap left up', 'micro left up', 'tap lu', 'micro lu']:
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(0.1)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['tap down left', 'micro down left', 'tap dl', 'micro dl', 'tap left down', 'micro left down', 'tap ld', 'micro ld']:
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(0.1)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['tap down right', 'micro down right', 'tap dr', 'micro dr', 'tap right down', 'micro right down', 'tap rd', 'micro rd']:
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(0.1)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['tap up right', 'micro up right', 'tap ur', 'micro ur', 'tap right up', 'micro right up', 'tap ru', 'micro ru']:
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(0.1)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['light up', 'soft up', 'mini up', 'mini u', 'soft u']:
                    PressKeyPynput(UP_ARROW)
                    time.sleep(0.3)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['light up left', 'soft up left', 'mini up left', 'mini ul', 'soft ul', 'light left up', 'soft left up', 'mini left up', 'light lu', 'soft lu', 'mini lu', 'light ul']:
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(0.3)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['light down left', 'soft down left', 'mini down left', 'mini dl', 'soft dl', 'light left down', 'soft left down', 'mini left down', 'light ld', 'soft ld', 'mini ld', 'light dl']:
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(0.3)
                    ReleaseKeyPynput(LEFT_ARROW)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['light down right', 'soft down right', 'mini down right', 'mini dr', 'soft dr', 'light right down', 'soft right down', 'mini right down', 'light rd', 'soft rd', 'mini rd', 'light dr']:
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(0.3)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['light up right', 'soft up right', 'mini up right', 'mini ur', 'soft ur', 'light right up', 'soft right up', 'mini right up', 'light ru', 'soft ru', 'mini ru', 'light ur']:
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(0.3)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['hard up', 'aggresive up', 'hard u', 'aggresive u']:
                    PressKeyPynput(UP_ARROW)
                    time.sleep(2.0)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['hard up left', 'aggresive up left', 'hard ul', 'aggresive ul', 'hard left up', 'aggresive left up', 'hard lu', 'aggresive lu']:
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(2.0)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['hard down left', 'aggresive down left', 'hard dl', 'aggresive dl', 'hard left down', 'aggresive left down', 'hard ld', 'aggresive ld']:
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(2.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['hard down right', 'aggresive down right', 'hard dr', 'aggresive dr', 'hard right down', 'aggresive right down', 'hard rd', 'aggresive rd']:
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(2.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['hard up right', 'aggresive up right', 'hard ur', 'aggresive ur', 'hard right up', 'aggresive right up', 'hard ru', 'aggresive ru']:
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(2.0)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['tap left', 'micro left', 'tap l', 'micro l']:
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(0.1)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['left', 'turn left', 'l', 'go left']:
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['light left', 'soft left', 'mini left', 'light l', 'soft l' 'mini l']:
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(0.3)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['hard left', 'aggresive left', 'hard l', 'aggresive l']:
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(2.0)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['tap right', 'micro right', 'tap r', 'micro r']:
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(0.1)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['right', 'r', 'go right', 'turn right']:
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['light right', 'soft right', 'mini right', 'light r', 'soft r', 'mini r']:
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(0.3)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['hard right', 'aggresive right', 'hard r', 'aggresive r']:
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(2.0)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['tap down', 'micro down', 'tap d', 'micro d', 'tap back', 'micro back']:
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(0.1)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['down', 'd', 'go down', 'back']:
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['light down', 'soft down', 'mini down', 'light down', 'light d', 'mini d', 'soft d', 'mini back', 'soft back', 'light back']:
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(0.3)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['hard down', 'aggresive down', 'hard d', 'aggresive d', 'hard back', 'aggresive back']:
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(2.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['ul', 'up left', 'forward left']: 
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['lu', 'left up', 'left forward']: 
                    PressKeyPynput(LEFT_ARROW)
                    PressKeyPynput(UP_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(LEFT_ARROW)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['ur', 'up right', 'forward right']: 
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['ru', 'right up', 'right forward']: 
                    PressKeyPynput(RIGHT_ARROW)
                    PressKeyPynput(UP_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(RIGHT_ARROW)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['dl', 'down left']: 
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['ld', 'left down']: 
                    PressKeyPynput(LEFT_ARROW)
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(LEFT_ARROW)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['dr', 'down right']: 
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['rd', 'right down']: 
                    PressKeyPynput(RIGHT_ARROW)
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(1.0)
                    ReleaseKeyPynput(RIGHT_ARROW)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['hu', 'hold up', 'hold forward']:
                    PressKeyPynput(UP_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['hd', 'hold down', 'hold back']:
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['hl', 'hold left']:
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['hr', 'hold right']:
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['hul', 'hold up left', 'hold forward left']: 
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['hlu', 'hold left up', 'hold left forward']: 
                    PressKeyPynput(LEFT_ARROW)
                    PressKeyPynput(UP_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(LEFT_ARROW)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['hur', 'hold up right', 'hold forward right']: 
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['hru', 'hold right up', 'hold right forward']: 
                    PressKeyPynput(RIGHT_ARROW)
                    PressKeyPynput(UP_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(RIGHT_ARROW)
                    ReleaseKeyPynput(UP_ARROW)
                if msg in ['hdl', 'hold down left', 'hold back left']: 
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(LEFT_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                if msg in ['hld', 'hold left down', 'hold left back']: 
                    PressKeyPynput(LEFT_ARROW)
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(LEFT_ARROW)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['hdr', 'hold down right', 'hold back right']: 
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(3.0)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['!stop', 'stop', 'release', 'end', 'release key', 'release keys']:
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(LEFT_ARROW)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                    ReleaseKeyPynput(C)
                    ReleaseKeyPynput(LEFT_SHIFT)
                    ReleaseKeyPynput(Z)
                if msg in ['shift']: 
                    PressKeyPynput(LEFT_SHIFT)
                    time.sleep(0.1)
                    ReleaseKeyPynput(LEFT_SHIFT)
                if msg in ['menu', 'items', 'c']:
                    PressKeyPynput(C)
                    time.sleep(0.1)
                    ReleaseKeyPynput(C)
                if msg in ['z', 'punch', 'attack', 'talk', 'enter', 'select']: 
                    PressAndHoldKey(Z, 0.1)
                if msg in ['zz', 'z z']:
                    PressAndHoldKey(Z, 0.1)
                    time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1)
                if msg in ['zzz', 'z z z']:
                    zz=0
                    while zz<=2:
                        zz+=1
                        PressAndHoldKey(Z, 0.1)
                        time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1)
                if msg in ['zzzz', 'z z z z']:
                    zz=0
                    while zz<=3:
                        zz+=1
                        PressAndHoldKey(Z, 0.1)
                        time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1)
                if msg in ['zzzzz', 'z z z z z']:
                    zz=0
                    while zz<=4:
                        zz+=1
                        PressAndHoldKey(Z, 0.1)
                        time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1)
                if msg in ['zzzzzz', 'z z z z z z']:
                    zz=0
                    while zz<=5:
                        zz+=1
                        PressAndHoldKey(Z, 0.1)
                        time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1)
                if msg in ['zzzzzzz', 'z z z z z z z']:
                    zz=0
                    while zz<=6:
                        zz+=1
                        PressAndHoldKey(Z, 0.1)
                        time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1)
                if msg in ['zzzzzzzz', 'z z z z z z z z']:
                    zz=0
                    while zz<=7:
                        zz+=1
                        PressAndHoldKey(Z, 0.1)
                        time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1) 
                if msg in ['zzzzzzzzz', 'z z z z z z z z z']:
                    zz=0
                    while zz<=8:
                        zz+=1
                        PressAndHoldKey(Z, 0.1)
                        time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1)
                if msg in ['zzzzzzzzzz', 'z z z z z z z z z z']:
                    zz=0
                    while zz<=9:
                        zz+=1
                        PressAndHoldKey(Z, 0.1)
                        time.sleep(0.3)
                    PressAndHoldKey(Z, 0.1)
                if msg in ['hold up down', 'hud', 'hdu', 'hold down up', 'hold ud', 'hold du']:
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(DOWN_ARROW)
                    time.sleep(5.0)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(DOWN_ARROW)
                if msg in ['hold up down right', 'hudr', 'hdur', 'hold down up right', 'hold udr', 'hold dur', 'hold right up down', 'hold right down up', 'hrdu', 'hrud']:
                    PressKeyPynput(UP_ARROW)
                    PressKeyPynput(DOWN_ARROW)
                    PressKeyPynput(RIGHT_ARROW)
                    time.sleep(5.0)
                    ReleaseKeyPynput(UP_ARROW)
                    ReleaseKeyPynput(DOWN_ARROW)
                    ReleaseKeyPynput(RIGHT_ARROW)
                if msg in ['x', 'b', 'back']: 
                    PressAndHoldKey(X, 0.1)
                if msg.startswith("type "): 
                    try:
                        typeMsg = msg[5:]
                        pydirectinput.typewrite(typeMsg)
                    except:
                        print("Typing this particular message didn't work: " + msg)
                if msg.startswith('up for '): 
                    try:
                        timee = msg[7:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            PressAndHoldKey(UP_ARROW,timee)
                    except:
                        print('er')
                if msg.startswith('left for '): 
                    try:
                        timee = msg[9:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            PressAndHoldKey(LEFT_ARROW,timee)
                    except:
                        print('er')
                if msg.startswith('right for '): 
                    try:
                        timee = msg[10:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            PressAndHoldKey(RIGHT_ARROW,timee)
                    except:
                        print('er')
                if msg.startswith('down for '): 
                    try:
                        timee = msg[9:]
                        timee = float(timee)
                        if timee<=10 and timee>=0:
                            PressAndHoldKey(DOWN_ARROW,timee)
                    except:
                        print('er')
        except:
            print('Encountered an exception while reading chat.')