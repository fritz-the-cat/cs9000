import sys
import serial
#import wx

global_number = 0
global_list = []
global_string = "A"
gInputFname = "sequence.txt"

STEPSPERINCH = 181.4286 #step/inch

CONTROLARRAYSIZE = 16
POSITIONARRAYSIZE = 21
gControlArray=[]
gPositionArray=[]

gSerialOpen = 0
gSer = serial.Serial()
gSerTimeout = 3

def __init__():
    for i in range(CONTROLARRAYSIZE):
        gControlArray.append(0)
    for i in range(POSITIONARRAYSIZE):
        gPositionArray.append(0)
    gSer = serial.Serial()
    return

    
#    Ocommand()
#    Dcommand()

    """
    gSer = serial.Serial(0, 9600, timeout=gSerTimeout,parity=serial.PARITY_EVEN,bytesize=serial.EIGHTBITS)
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
    
def SerialChkOpen():
    if gSer.isOpen() :
        return
    else :
        gSer.port = 4
        gSer.baudrate = 9600
        gSer.timeout = gSerTimeout
        gSer.parity=serial.PARITY_EVEN
        gSer.bytesize=serial.EIGHTBITS
        gSer.open()
        #gSer.Serial("com6", 9600, timeout=3,parity=serial.PARITY_EVEN,bytesize=serial.EIGHTBITS)
    #ser.baudrate = 9600
    #ser.port = 6
    #print gSer.isOpen()
    #gSer.close()
    #ser.open()
    return

def Ocommand():
    sCmd = "O"
    chk = ord(sCmd)
    for i in range(CONTROLARRAYSIZE):
        c = gControlArray[i]
        ret, s = ToAsciiHex(c)
        sCmd = sCmd + s
        chk ^= ret
        #print "c: " + str(c&0xff) + "\t" + str(s)
    #print "sCmd: " + sCmd
    SendCommand(sCmd,chk)
    s=gSer.readline(0x0d)
    return s
    
def Dcommand():
    sCmd = "D"
    chk = ord(sCmd)
    for i in range(POSITIONARRAYSIZE):
        for c in [gPositionArray[i]>>16, gPositionArray[i]>>8, gPositionArray[i]]:
            ret, s = ToAsciiHex(c)
            chk ^= ret
            sCmd = sCmd + s
            #print "c: " + str(c&0xff) + "\t" + str(s)
    #print "sCmd: " + sCmd
    SendCommand(sCmd,chk)
    s=gSer.readline(0x0d)           # read back machine response
    return s
    
def Pcommand():
    sCmd = "P"
    chk = ord(sCmd)
    SendCommand(sCmd,chk)
    s=gSer.readline(0x0d)
    return s

def Vcommand():
    sCmd = "V"
    chk = ord(sCmd)
    SendCommand(sCmd,chk)
    s=gSer.readline(0x0d)
    return s
    
def SendCommand(sCmd,chk):
    SerialChkOpen()
    chk = 0xff & (~chk)
    sCmd = sCmd + chr(chk) + chr(0x0d)
    if gSer.isOpen():
        gSer.write(sCmd)
    else:
        pass
        
"""
def ShowMenu():
    for i in range(16):
        print
    ShowParray()    
    return
    """
"""    
def ShowCarray():
    for i in range(16):
        print
    return
    """
"""
def ShowParray():
    for i in range(0,POSITIONARRAYSIZE,3):
        print "P"+repr(i).ljust(2)+":"+repr(gPositionArray[i]).rjust(6),repr(gPositionArray[i+1]).rjust(6),repr(gPositionArray[i+2]).rjust(6)
    return
    """

def ClearArrays():
    for i in range(CONTROLARRAYSIZE):
        gControlArray[i] = 0
    for i in range(POSITIONARRAYSIZE):
        gPositionArray[i] = 0
    return

def ReadArraysFromFile(filename):
    if filename!="":
        gInputFname = filename
    f = open(gInputFname, 'r')
    """
    lines 0 thru 15 are control variables $50 ... $5F
    lines 16 thru 36 are position variables
    """
    for i in range(CONTROLARRAYSIZE):
        gControlArray[i] = int(f.readline())
    for i in range(POSITIONARRAYSIZE):
        gPositionArray[i] = int(f.readline())
    f.close()
    return  

def WriteArraysToFile(filename):
    if filename!="":
        gInputFname = filename
    f = open(gInputFname, 'w')
    """
    lines 0 thru 15 are control variables $50 ... $5F
    lines 16 thru 36 are position variables
    """
    for i in range(CONTROLARRAYSIZE):
        f.readline(str(gControlArray[i])+"\n")
    for i in range(POSITIONARRAYSIZE):
        f.readline(str(gPositionArray[i])+"\n")
    f.close()
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

"""
if __name__ == '__main__':
    main()
    sys.exit()
    """