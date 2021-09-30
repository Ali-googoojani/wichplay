from pygame import mixer
import keyboard,os,platform,pyfiglet

#global vars

keys=[]
allnames=[]
maindict={}

#set keys and song here

def get_list_of_sounds_split():

    try:
        with open('config/ListOfSound.txt','r') as File:

           fileContent=File.read().split('\n')

           for i in range(0,len(fileContent)):
                if(".mp3" in fileContent[i] or ".ogg" in fileContent[i] or ".wav" in fileContent[i]):
                    allnames.append(fileContent[i])
                else:
                   keys.append(fileContent[i].upper()) 
                
        for dic in range(0,len(keys)):
            try:
                maindict[keys[dic]]=allnames[dic]
            except:
                print("")
        print(pyfiglet.figlet_format("wichplay\n"),"your config:",maindict,"\n Control Keys{'P':'PAUSE','C':'Contniue','0':'OFF'}")

    except FileNotFoundError:
        print('not found {0}'.format(filename))
        
#play sound function here
        
def play_sound():
    mixer.init()
    while True:
        
        try:
           
            
            if(keyboard.read_key().upper()=='P'):
                mixer.music.pause()
            elif(keyboard.read_key().upper()=='C'):
                mixer.music.unpause()
            elif(keyboard.read_key().upper() in keys):
                mixer.music.load('Sounds/'+allnames[keys.index(keyboard.read_key().upper())])
                mixer.music.play()

            elif(keyboard.read_key().upper()=="0"):
                if(platform.system().upper()=='WINDOWS'):
                    os.system('cls')
                    break
                elif(platform.system().upper()=='LINUX'):
                    os.system('clear')
                    break
            else:
                mixer.music.unpause()
        except ValueError:
            print("")
if(__name__=="__main__"):   
    get_list_of_sounds_split()
    play_sound()
