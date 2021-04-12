#imports
import os
import subprocess
from colorama import init,Fore, Back, Style
import asyncio
import urllib.parse
import time
from time import perf_counter
init(convert=True)
#vars
ver = "Beta, Lots of commits going on!"
ping = 0
pings = []
tempping = 0
searches = 0
base = 300
delay = 0
gotQ = ""
dropTime = 0
reqTime = 0
#funcs
def setupPing():
    print (Fore.BLUE, end='')
    print(" [setup]",end='')
    print(Fore.CYAN, end='')
    tempping = input( ''' What is your latency when connecting to the Minecraft API?
         You can also type "auto" for ping detection! ''')
            #See if they want auto ping detection or manual
    if (tempping == "auto"):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        print()
        print (Fore.BLUE + " [info]" + Fore.CYAN + " Ping detected was " + Fore.WHITE + str(sum(pings)/5) + Fore.CYAN + " ms, This value will be used as your ping.")
        return sum(pings)/5
    else:
        print()
        print (Fore.BLUE + " [info]" + Fore.CYAN + " You entered " + str(tempping) + " as your ping in ms, This value will be used as your ping.")
        return tempping
def setupSearches():
    print()
    print (Fore.BLUE, end='')
    print(" [setup]",end='')
    print(Fore.CYAN, end='')
    sm = 0
    sm = input(" How many searches/month does the target name have? ")
    return sm
def calc():
    print()
    print(Fore.BLUE + " [calculator]" + Fore.CYAN + " Calculating delay using ping: " + Fore.WHITE + str(ping) + Fore.CYAN + ", and searches: " + Fore.WHITE + str(searches) + Fore.CYAN)
    if (int(searches) >= 1000):
        print()
        print (Fore.BLUE + " [info]" + Fore.CYAN + " Since the amount of searches for the name is over 1000, we will account for server lag by adding some extra ms to your delay.")
        searchdiv = int(searches) / 50
        possibledelay = base + int(ping) + searchdiv
        return possibledelay
    else:
        possibledelay = base + int(ping)
        return possibledelay
def out():
    print()
    print (Fore.BLUE + " [DELAY]" + Fore.CYAN + " Your approximate delay to use is: " + Fore.WHITE + str(delay) + Fore.CYAN + " ms. This is an estimate, and you should lower or higher it depending on request times." )
    print()
    print (Fore.BLUE, end='')
    print(" [DELAY ADJUST]",end='')
    print(Fore.CYAN, end='')
    gotQ = input(" Did you get the name? (Y/N) (Caps): ")
    if (gotQ == "Y"):
        print (Fore.BLUE + " [DELAY ADJUST]" + Fore.CYAN + " Good job! Closing in 3 seconds.")
        time.sleep(3)
        exit()
    if (gotQ == "N"):
        print (Fore.BLUE, end='')
        print(" [DELAY ADJUST]",end='')
        print(Fore.CYAN, end='')
        dropTime = input(" Sorry to hear that. What time did the name drop? (Seconds/60) (ex. 23): ")
        print (Fore.BLUE, end='')
        print(" [DELAY ADJUST]",end='')
        print(Fore.CYAN, end='')
        reqTime = input(" And what time was your last request at? (Seconds.XXXX/60) (ex. 22.9874): ")
        if (int(dropTime) > float(reqTime)):
            changeDel =  (int(dropTime) - float(reqTime)) * 100
            print (Fore.BLUE + " [DELAY ADJUST]" + Fore.CYAN + " You were too early. Try: " + Fore.WHITE + str(delay + changeDel) + Fore.CYAN + " ms instead.")
            input(" Press any key to continue...")
        if (int(dropTime) < float(reqTime)):
            changeDel =  (float(reqTime) - int(dropTime)) * 100
            print (Fore.BLUE + " [DELAY ADJUST]" + Fore.CYAN + " You were too late. Try: " + Fore.WHITE + str(delay - changeDel) + Fore.CYAN + " ms instead.")
            input(" Press any key to continue...")
        else:
            exit()
    else:
     print (Fore.RED + " [ERROR]" + Fore.CYAN + " ENTER Y OR N!")
     time.sleep(3)
     exit()
#THIS PING CHECK CODE IS FROM kingscratss#3407 on discord!!
async def check(url: str):
    async def x():
        uri = urllib.parse.urlparse(url)
        reader, writer = await asyncio.open_connection(uri.hostname, 443, ssl=True)
        writer.write(f"GET {uri.path or '/'} HTTP/1.1\r\nHost:{uri.hostname}\r\n\r\n".encode())
        start = perf_counter()
        await writer.drain()

        await reader.read(1)
        end = perf_counter()
        return round((end - start) * 1000)
    for _ in range(5):
        pings.append(await x())
        await asyncio.sleep(0.01)
async def main():
    await check("https://api.minecraftservices.com/minecraft")

#cool ascii text thing/creds
os.system("cls")
print(Fore.LIGHTBLUE_EX + '''
  ██████╗ ███████╗██╗      █████╗ ██╗   ██╗
  ██╔══██╗██╔════╝██║     ██╔══██╗╚██╗ ██╔╝
  ██║  ██║█████╗  ██║     ███████║ ╚████╔╝
  ██║  ██║██╔══╝  ██║     ██╔══██║  ╚██╔╝
  ██████╔╝███████╗███████╗██║  ██║   ██║
  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝
''')
print(Fore.LIGHTBLUE_EX + "  By Mythological, Version: " + ver)
print()
print()
#assign vars
ping = setupPing()
searches = setupSearches()
#computate and print
delay = calc()
out()
