"""
# EasyPycode
#### EasyPycode is a lightweight, Windows focused Python utility module intended to simplify common tasks in console based applications. It provides a small, consistent interface for improving user interaction, system integration, and workflow control without introducing heavy dependencies or graphical frameworks.
[github](https://github.com/tromoSM/EasyPycode)
"""
import ctypes
from colorama import Style
from win32api import Beep as dihbeep
import time
from tkinter import Tk 
from colorama import Fore,Style,init,Back
import os
import threading
import sys
from windows_toasts import AudioSource, Toast, ToastAudio,WindowsToaster
from urllib import request
from PIL import Image
import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
import webbrowser
import subprocess
import shutil
import webview
from datetime import datetime
import tkinter
import requests
import PIL
MainTitle='EasyPycode' #eztitle fallback for wintoast all alert types

CautionIcon=0x30
InfoIcon=0x40
ErrorIcon=0x10
QuestionIcon=0x20

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

BGwhite=Back.WHITE
BGblue=Back.BLUE
BGcyan=Back.CYAN
BGgreen=Back.GREEN
BGmagenta=Back.MAGENTA
BGyellow=Back.YELLOW
BGred=Back.RED
BGblack=Back.BLACK
BGlightwhite=Back.LIGHTWHITE_EX
BGlightblue=Back.LIGHTBLUE_EX
BGlightcyan=Back.LIGHTCYAN_EX
BGlightgreen=Back.LIGHTGREEN_EX
BGlightmagenta=Back.LIGHTMAGENTA_EX
BGlightyellow=Back.LIGHTYELLOW_EX
BGlightred=Back.LIGHTRED_EX
BGlightblack=Back.LIGHTBLACK_EX

def SetEazyTitle(z):
 """Sets the global title for dialogs and windows created by this module"""
 global MainTitle
 MainTitle=z
def Error(x):
    """Displays an error dialog"""
    ctypes.windll.user32.MessageBoxW(0,x,MainTitle,0x10)
def Info(dih):
    """Displays an info dialog"""
    ctypes.windll.user32.MessageBoxW(0,dih,MainTitle,0x40)
def Warning(dih):
    """Displays a warning dialog"""
    ctypes.windll.user32.MessageBoxW(0,dih,MainTitle,0x30)
def Ask(dih,nih,**l):
    """Displays a question dialog. 
    ez.Ask(<-Message:str->,<-whether the dialog should have yes/no buttons:bool->,yes=<-function if yes is clicked:func->,no=<-function if no is clicked:func->)
    Example : Ask("do you want to continue?",True,yes=yesfunc,no=nofunc)
    """
    if nih:
        a=ctypes.windll.user32.MessageBoxW(0,dih,MainTitle,0x20|0x4)
    else:
        a=ctypes.windll.user32.MessageBoxW(0,dih,MainTitle,0x20)
    if a==6 and "yes" in l:
            l["yes"]()
    elif a==7 and "No" in l:
            l["No"]()

def Colored(Color,Text):
 """Prints a colored text or colored background with the chosen color.
 Example : ez.Colored(lightred,"im red")"""
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
    """Displays a countdown timer for a specific time in seconds
    Example: ez.Countdown(5)"""
    timeleft=int(timeleft)
    while timeleft:
        m,s=divmod(timeleft,60)
        struc='{:02d}:{:02d}'.format(m,s)
        print(struc,end='\r')
        time.sleep(1)
        timeleft-=1
    print('00:00')

def BeepCountdown(timeleft):
    """Displays a countdown timer with a beep sound at the end for a specific time in seconds
    Example: ez.BeepCountdown(5)"""
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
    """Copy a string into the users clipboard
    Example: ez.Copy("example text")
    """
    c=Tk()
    c.withdraw()
    c.clipboard_clear()
    c.clipboard_append(a)
    c.update()
    c.destroy()
def Paste():
    """Return the current copied text in the users clipboard"""
    p=Tk()
    p.withdraw()
    clipboard_text=p.clipboard_get()
    p.destroy()
    return clipboard_text
def OpenInDefaultApp(path):
    """Opens a file or a path in the default app"""
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
    """Displays a spinner in between when the ez.Busy("RUN") was called and ez.Busy("RESET") was called."""
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
    """Prints a formatted error message in the console"""
    print(Fore.RED+'Error: '+Style.RESET_ALL+Fore.LIGHTRED_EX+x+Style.RESET_ALL)

def Alert(message,icon):
     """Displays a message dialog with the message and the chosen icon
     Example: ez.Alert("message",ez.InfoIcon)
     """
     ctypes.windll.user32.MessageBoxW(0,message,MainTitle,icon)

def ReopenAsAdmin():
    """Reopen the current process with admin access"""
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
 """Flashing the current window for a specific duration(seconds)"""
 a=ctypes.windll.kernel32.GetConsoleWindow()
 if a:
     ctypes.windll.user32.FlashWindow(a,True)
     time.sleep(duration)
     ctypes.windll.user32.FlashWindow(a,False)
def SendNotification(text,description):
 """Sends a notification with the Title and the description
 Example : ez.SendNotification("example title","example description")
 \n\nIMPORTANT : ez.SendNotification() will only work in windows 10 or later.
 """
 burnttoast = WindowsToaster(MainTitle)
 TotЯ = Toast()
 TotЯ.text_fields = [text,description]
 TotЯ.audio=ToastAudio(AudioSource.Default, looping=False)
 burnttoast.show_toast(TotЯ)

def CheckNetwork():
 """Returns True if the user is connected to a network returns false if not"""
 try:
    request.urlopen("http://www.msftconnecttest.com/connecttest.txt", timeout=2)
    return True
 except request.URLError as err: 
    return False
def CreateQR(content,FilePathWithName):
    """
    Creates a QR code and saves it to the path given
    Example : ez.CreateQR("hello world","folder1/filename")
    \n\nDo not include the file extension(.png/.jpg) in the FilePathWithName
    ex: ez.CreateQR("example qr content","media/images/qrcode") | output: currentDir/media/images/qrcode.png
    """
    qrcode.make(content).save(os.path.abspath(FilePathWithName+".png"))
    
def CreateBarcode(number,FilePathWithName):
    """
    Creates a Barcode and saves it to the path given
    Example : ez.CreateBarcode(241851545431)
    \n\n- Do not include the file extension(.png/.jpg) in the FilePathWithName
    ex: ez.CreateBarcode(241851545431,"media/images/barcode") | output: currentDir/media/images/barcode.png
    - The barcode number must include 12 digits
    """
    EAN13(str(number),writer=ImageWriter()).save(os.path.abspath(FilePathWithName))
def PrintCenter(text):
    """Prints the text given centered in the console
    this function will raise an OSError if stdout isnt a terminal. run in a "try" block as a safe fallback
    """
    c,r=os.get_terminal_size()
    print(text.center(c))
def TypePrint(text):
    """Print the text given with a typing animation"""
    for dih in text:
        print(dih,end="",flush=True)
        time.sleep(0.2)
    print() 
def OpenUrl(url):
  """Opens the url given in the default browser
  Example: ez.OpenUrl("https://google.com/")
  """
  webbrowser.open(url)
def OpenInWebview(title,url):
 """
 Opens the url given in a webview window with the given title
 Example: ez.OpenInWebview("example title",'https://google.com/')
 \n\nNote : webview is installed on many windows systems.
 Some older systems might not have it installed. if its not installed
 please run this command(cmd/bash) to install webview,
 winget install Microsoft.EdgeWebView2Runtime
 """
 try:
     import webview
 except ImportError:
     raise RuntimeError('ImportError : pywebview is required. pip install pywebview')
 webview.create_window(title,url)
 webview.start()
def GetUsername():
  """Returns the current username"""
  return os.getlogin()
def LockWorkStation():
 """Locks the current workstation"""
 ctypes.windll.user32.LockWorkStation()
def Pause():
    """Prints 'Press enter to continue...' and will not continue the following code until enter is pressed."""
    input("Press enter to continue...")
settings_home="ms-settings:"
settings_about='ms-settings:about'
settings_system='ms-settings:system'
settings_display='ms-settings:display'
settings_multitasking='ms-settings:multitasking'
settings_clipboard='ms-settings:clipboard'
settings_remoteDesktop='ms-settings:remote-desktop'
settings_personalization="ms-settings:personalization"
settings_network="ms-settings:network"
settings_network_wifi="ms-settings:network-wifi"
settings_apps='ms-settings:appsfeatures'
settings_privacy='ms-settings:privacy'
settings_defender="ms-settings:windowsdefender"
settings_security='ms-settings:windowssecurity'
settings_update='ms-settings:windowsupdate'
def NavigateSettings(x):
   """
   Opens setting with the given page
   Example: ez.NavigateSettings(ez.settings_network_wifi) """
   subprocess.run(['cmd',"/c","start",x])
def ShowAvailableNetworks():
   """Opens the 'show available networks' dialog """
   subprocess.run(['cmd',"/c","start",'ms-availablenetworks:'])
def MoveSelfToStartup():
   """
   Copy the current __file__ to windows shell:startup (current user)
   """
   shutil.copy(__file__,os.path.expanduser("~")+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")

day='d'
month='m'
hour='h'
microsecond='w'
weekday='a'
second='s'
timeWithMicrosecond='f'
timestamp='tt'
def GetDateAndTime(x):
 """Returns the current day/month/hour/microsecond/weekday/second/time microsecond/timestamp based on the argument given.
 Example ez.GetDateAndTime(ez.weekday) | returns "friday"
 """
 a=datetime.now()
 if(x=="d"):
    return a.day
 elif(x=="m"):
    return a.month
 elif(x=='h'):
    return a.hour
 elif(x=="w"):
    return a.microsecond
 elif(x=="a"):
    b=a.weekday()
    if(b==0):
       return "monday"
    elif(b==1):
       return "tuesday"
    elif(b==2):
       return "wednesday"
    elif(b==3):
       return "thursday"
    elif(b==4):
       return "friday"
    elif(b==5):
       return "saturday"
    elif(b==6):
       return "sunday"
 elif(x=="s"):
    return a.second
 elif(x=='f'):
    return a.time()
 elif(x=="tt"):
    return a.timestamp()


Gigabytes="gb"
Bytes='b'
Kilobytes='kb'
Bits='B'
Terabytes='T'
def ConvertToMB(data,current):
   """Converts and returns the data and the current data-measurement given into MegaBytes.
   Example: ez.ConvertToMB(123542,ez.Bytes)
   \n\nIMPORTANT: this is using 1024(binary) to convert data.
   """
   if(current=="b"):
      return data/(1024*1024)
   elif(current=='kb'):
      return data/1024
   elif(current=='gb'):
      return data*1024
   elif(current=='B'):
      return data/(1024*1024*8)
   elif(current=='T'):
      return data*(1024*1024)
def GetUserDir():
   """Return the current user's dir 
   Example ez.GetUserDir() | returns : "C:\\Users\\TromoSM"
   """
   return os.path.expanduser("~")
def SetConsoleTitle(z):
 ctypes.windll.kernel32.SetConsoleTitleW(z)

def GetProcessID():
   return os.getpid()
def GetParentProcessID():
   return os.getppid()
def TerminateProcess(x):
    if(type(x)==int):
       x=str(x)
       Colored(lightblue,"INFO : Turned ProcessID from int to str. Use str next time.")
    try:
       os.system("TASKKILL /F /PID "+x)
    except:
       Error('Failed to terminate process with pid : '+x)
       pass

def ReadFileAsText(path):
 """Return the read the content inside the given file path as text"""
 with open(os.path.abspath(path),"r")as dih:
    return dih.read()
def ReadFileAsBinary(path):
 """Return the read the content inside the given file path as Binary (rb)"""
 with open(os.path.abspath(path),"rb")as dih:
    return dih.read()
def WriteFileAsText(path,data):
 """Write the given data to the given file.
 example | ez.WriteFileAsText(temp.txt,"hello world ahh")
 """
 with open(os.path.abspath(path),"w")as dih:
   dih.write(data)
def WriteFileAsBinary(path,data):
 """Write the given data to the given file as binary.
 example | ez.WriteFileAsBinary(example.png,b"hello world ahh")
 """
 with open(os.path.abspath(path),"wb")as dih:
   dih.write(data)

def GetDisplayResolution():
    """Returns the current display resolution as an array
    Example : ez.GetDisplayResolution() will return [1366, 768]
    """
    sybau=tkinter.Tk()
    temp0arr0res=[]
    temp0arr0res.append(sybau.winfo_screenwidth ())
    temp0arr0res.append(sybau.winfo_screenheight())
    sybau.after(0,sybau.destroy)  
    return temp0arr0res

def BrightText(dih):
   """Prints the given text as bright text (ESC[1m)
   Example : ez.BrightText("example")
   """
   print(Style.BRIGHT+str(dih)+Style.RESET_ALL)
   
def Download(url,path):
        """Downloads the given file(url) to the given path.
        Example : ez.Download("https://www.example.com/download/file.txt","./example_path/")
        """
        imimname=url.split('/')[-1]
        imimpath=os.path.abspath(path)
        if os.path.isdir(imimpath):
           imimpath=os.path.join(imimpath,imimname)
        ctypes.windll.user32.MessageBoxW(0,f"Downloading setup\r\nFile will be saved to {imimpath}",MainTitle,0x40)
        r=requests.get(url,stream=True)
        with open(imimpath,'wb')as dih:
            for i in r.iter_content(65536):
                dih.write(i)
        ctypes.windll.user32.MessageBoxW(0,f"Download complete\r\nSaved to {imimpath}",MainTitle,0x40)
        return str(imimpath)

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
 "SendNotification",
 'CheckNetwork',
 "CreateQR",
 "CreateBarcode",
 "TypePrint",
 "OpenUrl",
  "OpenInWebview",
  "GetUsername",
  "LockWorkStation",
  "Pause",
  "NavigateSettings",
  "ShowAvailableNetworks",
  "MoveSelfToStartup",
  "GetDateAndTime",
  "ConvertToMB",
  "GetUserDir",
  "SetConsoleTitle",
  "GetProcessID",
  "GetParentProcessID",
  "TerminateProcess",
  "ReadFileAsText",
  "ReadFileAsBinary",
  "WriteFileAsText",
  "WriteFileAsBinary",
  "GetDisplayResolution",
  "BrightText",
  "Download",

 "Gigabytes",
 "Bytes",
 "Kilobytes",
 "Bits",
 "Terabytes",
  
"settings_home",
"settings_about",
"settings_system",
"settings_display",
"settings_multitasking",
"settings_clipboard",
"settings_remoteDesktop:str",
"settings_personalization:str",
"settings_network:str",
"settings_network_wifi:str",
"settings_apps:str",
"settings_privacy:str",
"settings_defender:str",
"settings_security:str",
"settings_update:str",
  
  "CautionIcon",
  "InfoIcon",
  "ErrorIcon",
  "QuestionIcon", 

 "white","blue","cyan","green","magenta","yellow","red","black",
 "lightwhite","lightblue","lightcyan","lightgreen",
 "lightmagenta","lightyellow","lightred","lightblack",
"BGwhite=Back.WHITE",
"BGblue=Back.BLUE",
"BGcyan=Back.CYAN",
"BGgreen=Back.GREEN",
"BGmagenta=Back.MAGENTA",
"BGyellow=Back.YELLOW",
"BGred=Back.RED",
"BGblack=Back.BLACK",
"BGlightwhite=Back.LIGHTWHITE_EX",
"BGlightblue=Back.LIGHTBLUE_EX",
"BGlightcyan=Back.LIGHTCYAN_EX",
"BGlightgreen=Back.LIGHTGREEN_EX",
"BGlightmagenta=Back.LIGHTMAGENTA_EX",
"BGlightyellow=Back.LIGHTYELLOW_EX",
"BGlightred=Back.LIGHTRED_EX",
"BGlightblack=Back.LIGHTBLACK_EX"
]
