#imports
import subprocess
from colorama import init,Fore, Back, Style
init(convert=True)
#vars
ver = "Literal First Release, prob has millions of bugs"
ping = 0
tempping = 0
searches = 0
base = 400
delay = 0
#funcs
def setupPing():
    print (Fore.BLUE, end='')
    print(" [setup]",end='')
    print(Fore.CYAN, end='')
    tempping = input( ''' What is your latency when connecting to api.mojang.com?
         You can also type "auto" for ping detection! ''')
            #See if they want auto ping detection or manual
    if (tempping == "auto"):
        #ping the server and read output
        print (Fore.RESET)
        p = subprocess.Popen("ping api.mojang.com", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        print()
        print (Fore.BLUE + " [info]" + Fore.CYAN + " Your avg ping was: " + formatOut(out) + "ms! This value will be used as your ping.")
        return formatOut(out)
    else:
        print()
        print (Fore.BLUE + " [info]" + Fore.CYAN + " You entered " + str(tempping) + " as your ping in ms, This value will be used as your ping.")
        return tempping
def formatOut(stf):
    format1 = str(stf).split("Average = ",1)[1]
    formatted = format1.split("m",1)[0]
    return formatted
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
    if (int(searches) >= 100):
        searchdiv = int(searches) / 10
        possibledelay = base + int(ping) + searchdiv
        return possibledelay
    else:
        possibledelay = base + int(ping)
        return possibledelay
def out():
    print()
    print (Fore.BLUE + " [DELAY]" + Fore.CYAN + " Your approximate delay to use is: " + Fore.WHITE + str(delay) + Fore.CYAN + " ms. This is an estimate, and you should lower or higher it depending on request times." )
#cool ascii text thing/creds
print(Fore.LIGHTBLUE_EX + '''
       _      _
      | |    | |
    __| | ___| | __ _ _   _
   / _` |/ _ \ |/ _` | | | |
  | (_| |  __/ | (_| | |_| |
   \__,_|\___|_|\__,_|\__, |
                       __/ |
                      |___/
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
