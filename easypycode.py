import ctypes
from colorama import Style
from win32api import Beep as dihbeep
import time
from tkinter import Tk 
from colorama import Fore,Style
import os
import threading
import sys
MainTitle='eazyPython'
CautionIcon=0x30
InfoIcon=0x40
ErrorIcon=0x10
QuestionIcon=0x20

def SetEazyTitle(z):
 global MainTitle
 MainTitle=z
def Error(x):
    ctypes.windll.user32.MessageBoxW(0,x,MainTitle,0x10)
def Info(dih):
    ctypes.windll.user32.MessageBoxW(0,dih,MainTitle,0x40)
def Warning(dih):
    ctypes.windll.user32.MessageBoxW(0,dih,MainTitle,0x30)
def Ask(dih,nih,**l):
    if nih:
        a=ctypes.windll.user32.MessageBoxW(0,dih,MainTitle,0x20|0x4)
    else:
        a=ctypes.windll.user32.MessageBoxW(0,dih,MainTitle,0x20)
    if a==6 and "Yes" in l:
            l["Yes"]()
    elif a==7 and "No" in l:
            l["No"]()

white=Fore.WHITE
blue=Fore.BLUE
cyan=Fore.CYAN
green=Fore.GREEN
magenta=Fore.MAGENTA
yellow=Fore.YELLOW
red=Fore.RED
black=Fore.BLACK
lightwhite=Fore.LIGHTWHITE_EX
lightblue=Fore.LIGHTBLUE_EX
lightcyan=Fore.LIGHTCYAN_EX
lightgreen=Fore.LIGHTGREEN_EX
lightmagenta=Fore.LIGHTMAGENTA_EX
lightyellow=Fore.LIGHTYELLOW_EX
lightred=Fore.LIGHTRED_EX
lightblack=Fore.LIGHTBLACK_EX

def Colored(Color,Text):
 print(Color,Text,Style.RESET_ALL)

def Beep(Frequency,duration):
 """
  Frequency= Hz(int)\n
  Duration= Seconds(int)
\n\n
  ACTION = win32api.beep(Frequency,duration*1000)
 """
 dihbeep(Frequency,duration*1000)

def Countdown(timeleft):
    timeleft=int(timeleft)
    while timeleft:
        m,s=divmod(timeleft,60)
        struc='{:02d}:{:02d}'.format(m,s)
        print(struc,end='\r')
        time.sleep(1)
        timeleft-=1
    print('00:00')

def BeepCountdown(timeleft):
    timeleft=int(timeleft)
    while timeleft:
        m,s=divmod(timeleft,60)
        struc='{:02d}:{:02d}'.format(m,s)
        print(struc,end='\r')
        time.sleep(1)
        timeleft-=1
        if(1<=timeleft<=3):
            dihbeep(500,300)
    dihbeep(700,150)
    dihbeep(700,150)
    print('00:00')
def Copy(a):
    c=Tk()
    c.withdraw()
    c.clipboard_clear()
    c.clipboard_append(a)
    c.update()
    c.destroy()
def Paste():
    p=Tk()
    p.withdraw()
    clipboard_text=p.clipboard_get()
    p.destroy()
    return clipboard_text
def OpenInDefaultApp(path):
    os.startfile(os.path.abspath(path))
busy0run=False
busy0thread=None
def Busy0loop():
    global busy0run
    ss=['-','/','|','\\']
    o=0
    while busy0run:
        sys.stdout.write(ss[o%4]+'\r')
        sys.stdout.flush()
        o+=1
        time.sleep(0.5)
def Busy(act):
    global busy0run,busy0thread
    if act.upper()=="RUN":
     if busy0run:
       return
     busy0run=True
     busy0thread=threading.Thread(target=Busy0loop,daemon=True)
     busy0thread.start()
    elif act.upper()=="RESET":
     busy0run=False
     if busy0thread:
        busy0thread.join()
     print(' ',end='\r')


def ErrorText(x):
    print(Fore.RED+'Error: '+Style.RESET_ALL+Fore.LIGHTRED_EX+x+Style.RESET_ALL)

def Alert(message,icon):
     ctypes.windll.user32.MessageBoxW(0,message,MainTitle,icon)

def ReopenAsAdmin():
    def tstahhh():
            try:
               return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
    if not tstahhh():
         ctypes.windll.shell32.ShellExecuteW(
            None,'runas',sys.executable," ".join(sys.argv),
            None,1
         )
         sys.exit(0)
def FlashWindow(duration):
 a=ctypes.windll.kernel32.GetConsoleWindow()
 if a:
     ctypes.windll.user32.FlashWindow(a,True)
     time.sleep(duration)
     ctypes.windll.user32.FlashWindow(a,False)
__all__=[
 "Error",
 "Info",
 "Warning",
 "Ask",
 "Colored",
 "Beep",
 "Countdown",
 "BeepCountdown",
 "Copy",
 "Paste",
 "Busy",
 "ErrorText",
 "SetEazyTitle",
 "Alert",
 "ReopenAsAdmin",
 "FlashWindow",
 
  "CautionIcon",
  "InfoIcon",
  "ErrorIcon",
  "QuestionIcon", 

 "white","blue","cyan","green","magenta","yellow","red","black",
 "lightwhite","lightblue","lightcyan","lightgreen",
 "lightmagenta","lightyellow","lightred","lightblack"
]
