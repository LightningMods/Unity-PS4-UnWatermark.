''' 
       __          __    _                       _____                   _ _ 
       \ \        / /   | |                     / ____|                 | | |
        \ \  /\  / /__  | |     _____   _____  | (___   ___  _ __  _   _| | |
         \ \/  \/ / _ \ | |    / _ \ \ / / _ \  \___ \ / _ \| '_ \| | | | | |
          \  /\  /  __/ | |___| (_) \ V /  __/  ____) | (_) | | | | |_| |_|_|
           \/  \/ \___| |______\___/ \_/ \___| |_____/ \___/|_| |_|\__, (_|_)
                                                                    __/ |    
                                                                   |___/     
'''
 
import shutil
import sys
import os
import zipfile


def zip(src, dst):
    zf = zipfile.ZipFile("%s" % (dst), "w", zipfile.ZIP_DEFLATED,allowZip64 = True)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print('Writing %s To '+dst) % filename
            zf.write(absname, arcname)
            if args.__contains__("-d"):
                print("Removing %s") % filename
                os.remove(absname)
    zf.close()
	
print("________                __      _________       _____  __                                                            ")
print("\______ \ _____ _______|  | __ /   _____/ _____/ ____\/  |___  _  _______ _______   ____      ___  ______.__.________")
print(" |      |  \\__  \\_  __ \  |/ / \_____  \ /  _ \   __\\   __\ \/ \ / /\__  \\_  __ \_/ __ \     \  \/  <   |  |\___  /")
print(" |    `   \/ __ \|  | \/    <  /        (  <_> )  |   |  |  \     /  / __ \|  | \/\  ___/      >    < \___  | /   /") 
print("/_______  |____  /__|  |__|_ \/_______  /\____/|__|   |__|   \/\_/  |____  /__|    \___  > /\ /__/\_ \/ ____|/____/")
print("        \/     \/           \/        \/                                 \/            \/  \/       \/\/          \/") 
print(" __      __         __                  _____                __     __________")                                         
print("/  \    /  \_____ _/  |_  ___________  /     \ _____ _______|  | __ \______   | ____   _____   _______  __ ___________") 
print("\   \/\/   /\__  \\   __\/ __ \_  __ \/  \ /  \\__  \\_  __ \  |/ /  |       _// __ \ /     \ /  _ \  \/ // __ \_  __ |")
print(" \        /  / __ \|  | \  ___/|  | \/    Y    \/ __ \|  | \/    <   |    |   \  ___/|  Y Y  (  <_> )   /\  ___/|  | \/")
print("  \__/\  /  (____  /__|  \___  >__|  \____|__  (____  /__|  |__|_ \  |____|_  /\___  >__|_|  /\____/ \_/  \___  >__|")   
print("       \/        \/          \/              \/     \/           \/         \/     \/      \/                 \/")       
print("")
print("")
print("")
print("-i Input Path")
print("-o Output Path")
print("-j Delete TEMP Folder")
print("-p Pack to Package (Currently Unavilable)")
print("-u Remove \"Trial Version\" Watermark")
print("\nExample: UnWaterMark.py -i input -o output -j -p -u -p")

args = sys.argv[1:]

if len(args) == 1 and os.path.exists(args[0]):
    args = ["-i",args[0],"-o",args[0],"-u","-j","-p"]

if args.__contains__("-i"):
    global inputFolder
    inputFolder = args[args.index("-i") + 1]
else:
    print("No input folder!")
    sys.exit(123)

if args.__contains__("-o"):
    global outputFolder
    outputFolder = args[args.index("-o") + 1]
else:
    print("No output folder! using "+inputFolder+"-output")
    outputFolder = inputFolder+"-output"

print("BEGIN PROCESSING")
print("Looking for SELFs in "+inputFolder)


a = 0

list = os.listdir(inputFolder)
while a != len(list):
    if list[a].lower().endswith(".self") or list[a].lower() == "eboot.bin":
        print("SELF Found: "+list[a])
        global selfFile
        selfFile = list[a]
        a = len(list)
        break
        file.close()
    a += 1
try:
    selfFile
except:
    print("No SELF found! (Incorrect input dir?)")
    sys.exit(643)

if args.__contains__("-u"):
    print("Removing \"Trial Version\" Watermark. . .")
    try:
        with open(inputFolder+selfFile,"rb") as file:
            readData = file.read()
            offset = readData.index(b"\x74\x72\x69\x61\x6C\x2E\x70\x6E\x67")
            file.close()
        if not readData.__contains__(b"invaild"):
            with open(inputFolder+selfFile,"r+b") as file:
                file.seek(offset)
                file.write(b"invaild")
    except:
        print("Failed to open SELF: "+selfFile)
        sys.exit(344)
    print("Watermark Removed.")
	
if args.__contains__("-p"):
        print("Unavilable")
pass

if args.__contains__("-j"):
    print("Deleting TEMP")
    try:
        shutil.rmtree(inputFolder+"\\Temp")
    except:
        pass

    print("Removing configuration.ps4path")
    try:
        os.remove(inputFolder+"\\configuration.ps4path")
    except:
        pass

    print("Finding and Removing Bin files")

    try:
        list = os.listdir(inputFolder)
        a = 0
        while a != len(list):
            if list[a].lower().endswith("bin"):
                print("Removing "+list[a])
                os.remove(inputFolder+"\\"+list[a])
            a += 1
    except:
        pass
    print("Removed unused files . . .")
