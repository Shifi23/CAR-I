from opcode import stack_effect
import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
print("Communication Successfully started")

IGN = 4
SRT = 5
KSN = 7
PKL = 6
UNL = 8
LOC = 9
INL = 10
ACC = 11

board.digital[IGN].write(1)
board.digital[SRT].write(1)
board.digital[KSN].write(1)
board.digital[PKL].write(1)
board.digital[UNL].write(1)
board.digital[LOC].write(1)
board.digital[INL].write(1)
board.digital[ACC].write(1)

def StartCar():
    board.digital[KSN].write(0)
    time.sleep(1)
    board.digital[IGN].write(0)
    time.sleep(1)
    board.digital[SRT].write(0)
    time.sleep(1)
    board.digital[SRT].write(1)
    time.sleep(1)
    board.digital[PKL].write(0)
    time.sleep(1)
    print("Car Started")
    # board.digital[ACC].write(0)
    # board.digital[INL].write(0)
    


    
def unlockcar():
    board.digital[UNL].write(0)
    time.sleep(1)
    board.digital[UNL].write(1)
    time.sleep(1)
    board.digital[UNL].write(0)
    time.sleep(1)
    board.digital[UNL].write(1)
    time.sleep(1)

def acc():
    board.digital[ACC].write(1)


def inl():
    board.digital[INL].write(0)
    time.sleep(1)
    board.digital[INL].write(1)
    time.sleep(1)
    board.digital[INL].write(0)
    time.sleep(1)
    board.digital[INL].write(1)

def pkl():
    board.digital[PKL].write(0)
    time.sleep(1)
    board.digital[PKL].write(1)
    time.sleep(1)
    board.digital[PKL].write(0)
    time.sleep(1)
    board.digital[PKL].write(1)


acc()
inl()
#
