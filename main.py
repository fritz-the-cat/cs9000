import sys
import serial
import wx

global_number = 0
global_list = []
global_string = "A"
gInputFname = "sequence.txt"

CONTROLARRAYSIZE = 16
POSITIONARRAYSIZE = 21
gControlArray=[]
gPositionArray=[]

gSerialOpen = 0
gSer = serial.Serial()

def main():

    app = wx.App()
    
    frame = wx.Frame(None,-1,'simple.py')
    frame.Show()
    
    app.MainLoop()
    
    #gControlArray = []
    for i in range(CONTROLARRAYSIZE):
        gControlArray.append(0)
    for i in range(POSITIONARRAYSIZE):
        gPositionArray.append(0)
    ShowMenu()
    ReadArraysFromFile()    
   
    ShowMenu()
    
    Ocommand()
    
    Dcommand()

    """
    #ser = serial.Serial()
    gSer = serial.Serial(0, 9600, timeout=3,parity=serial.PARITY_EVEN,bytesize=serial.SEVENBITS)
    #ser.baudrate = 9600
    #ser.port = 0
    print gSer.portstr
    stro = ""
    for i in range(p_list):
        stro += p_list[i][0] + p_list[i][1]
    gSer.write("D" + stro + chr(chk&0xff) + "\r")
    line = gSer.readline()   # read a '\n' terminated line
    """
    
    """    
    '0'== one cycle completed
    '1'== no wire left
    '5'== $45.5 set EMERGENCYSTOP BUTTON pressed
    '6'== CYCLESTOP BUTTON pressed
    '0'== $16.1 set
    '2'== JACK 
    '7'== PIPESENSOR
    '4'== CUTSENSOR
    'F4'==ram test $0040 to $00f0 error
    'F5'==ram test $0100 to $01ff error
    'F9'==parity or checksum error
    """
    #print "return: " + line
    
    
    gSer = serial.Serial(0, 9600, timeout=3,parity=serial.PARITY_EVEN,bytesize=serial.EIGHTBITS)
    print gSer

    print gSer.isOpen()
    
    gSer.close()
    #ser.open()
    return

def Ocommand():
    sCmd = "O"
    chk = ord(sCmd)
    #v_list = []
    
    for i in range(CONTROLARRAYSIZE):
        c = gControlArray[i]
        ret, s = ToAsciiHex(c)
        sCmd = sCmd + s
        chk ^= ret
        print "c: " + str(c&0xff) + "\t" + str(s)
    print "sCmd: " + sCmd
    SendCommand(sCmd,chk)
    
def Dcommand():
    sCmd = "D"
    chk = ord(sCmd)
    #p_list = []
    for i in range(POSITIONARRAYSIZE):
        for c in [gPositionArray[i]>>16, gPositionArray[i]>>8, gPositionArray[i]]:
            ret, s = ToAsciiHex(c)
            chk ^= ret
            sCmd = sCmd + s
            print "c: " + str(c&0xff) + "\t" + str(s)
    print "sCmd: " + sCmd
    SendCommand(sCmd,chk)
    
def Pcommand():
    sCmd = "P"
    chk = ord(sCmd)
    SendCommand(sCmd,chk)

def Vcommand():
    sCmd = "V"
    chk = ord(sCmd)
    SendCommand(sCmd,chk)
    
def SendCommand(sCmd,chk):
    chk = 0xff & (~chk)
    sCmd = sCmd + chr(chk) + chr(0x0d)
    if gSer.isOpen():
        pass
        gSer.write(sCmd)
    else:
        pass
        
def ShowMenu():
    for i in range(16):
        print
    ShowParray()    
    return

def ShowCarray():
    for i in range(16):
        print
        
    return

def ShowParray():
    for i in range(0,POSITIONARRAYSIZE,3):
        print "P"+repr(i).ljust(2)+":"+repr(gPositionArray[i]).rjust(6),repr(gPositionArray[i+1]).rjust(6),repr(gPositionArray[i+2]).rjust(6)
        
    return

def ClearArrays():
    for i in range(CONTROLARRAYSIZE):
        gControlArray[i] = 0
    for i in range(POSITIONARRAYSIZE):
        gPositionArray[i] = 0
    return

def ReadArraysFromFile():
    #gInputFname = raw_input("Enter filename (sequence.txt):")
    f = open(gInputFname, 'r')
    """
    lines 0 thru 15 are control variables $50 ... $5F
    lines 16 thru 36 are position variables
    """
    for i in range(CONTROLARRAYSIZE):
        gControlArray[i] = int(f.readline())
    for i in range(POSITIONARRAYSIZE):
        gPositionArray[i] = int(f.readline())
    return  

#returns int chk, string s
def ToAsciiHex(c):
    c = c & 0xff
    i = c>>4
    if(i>9):
        i += 7
    i += 0x30
    chk = i
    s = str(chr(i))
    i = c & 0x0f
    if(i>9):
        i += 7
    i += 0x30
    chk ^= i
    s += str(chr(i))
    return chk, s

"""
'D'  X1H X1L X2H X2L X3H X3L ... X53H X53L X54H X54L CHK $0D
     X1H X1L  like '4A' for 4Ah
     copy 54 bytes from input buffer to $60 thru $95
     
'O'  X1H X1L X2H X2L X3H X3L ... X15H X15L X16H X16L CHK $0D
     X1H X1L  like '4A' for 4Ah
     copy 16 bytes from input buffer to $50 thru $5F
     $50 $51 $52 $53 are doubled before copying
     """

if __name__ == '__main__':
    main()
    sys.exit()