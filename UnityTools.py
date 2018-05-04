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
                print("Remove %s") % filename
                os.remove(absname)
    zf.close()

print("SilicaAndPina's PSV Unity Tools:")
print("-i Input Path")
print("-o Output Path")
print("-f Fix Unsafe Homebrew Bug")
print("-u Remove \"Trial Mode\" Watermark")
print("-r Remove unused files")
print("-p Pack to VPK")
print("-d Remove input folder after packing to vpk.")
print("\nExample: UnityTools -i input -o output -f -u -r -p")

args = sys.argv[1:]


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
try:
    list = os.listdir(inputFolder)
    while a != len(list):
        if list[a].lower().endswith(".self") or list[a].lower().endswith(".bin"):
            with open(inputFolder+list[a],"rb") as file:
                if file.read(3) == "SCE":
                    print("SELF Found: "+list[a])
                    global selfFile
                    selfFile = list[a]
                    a = len(list)
                    break
                file.close()
        a += 1
    selfFile
except:
    print("No SELF found! (Incorrect input dir?)")
    sys.exit(643)

if args.__contains__("-f"):
    print("Fixing Unsafe Homebrew bug. . .")
    try:
        with open(inputFolder+selfFile,"r+b") as file:
            file.seek(0x80)
            file.write(b"\x00\x00\x00\x00\x00\x00\x00\x00")
            file.close()
    except:
        print("Failed to open SELF: "+selfFile)
        sys.exit(344)
    print("Fixed!")

if args.__contains__("-u"):
    print("Removing \"Trial Mode\" Watermark. . .")
    try:
        readData = open(inputFolder+selfFile,"rb").read()
        readData = readData.replace(b"\x55\x6E\x69\x74\x79\x57\x61\x74\x65\x72\x4D\x61\x72\x6B\x2D\x74\x72\x69\x61\x6C\x2E\x70\x6E\x67",b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        open(inputFolder+selfFile,"wb").write(readData)
    except:
        print("Failed to open SELF: "+selfFile)
        sys.exit(344)
    print("Watermark Removed.")

if args.__contains__("-r"):
    print("Removing unused files. . .")
    print("Removing SymbolFiles/")
    try:
        shutil.rmtree(inputFolder+"SymbolFiles")
    except:
        pass

    print("Removing Configuration.psp2path")
    try:
        os.remove(inputFolder+"configuration.psp2path")
    except:
        pass

    print("Removing ScriptLayoutHashes.txt")
    try:
        os.remove(inputFolder+"ScriptLayoutHashes.txt")
    except:
        pass

    print("Finding and Removing .bat files. . .")

    try:
        list = os.listdir(inputFolder)
        a = 0
        while a != len(list):
            if list[a].lower().endswith("bat"):
                print("Removing "+list[a])
                os.remove(inputFolder+list[a])
            a += 1
    except:
        pass
    print("Removed unused files . . .")

if args.__contains__("-p"):
        print("Packing to .VPK. . .")
        print("Renaming " +selfFile+" To eboot.bin")
        os.rename(inputFolder+selfFile,inputFolder+"eboot.bin")
        print("Zipping "+inputFolder)
        try:
            os.makedirs(outputFolder)
        except:
            pass
        zip(inputFolder,outputFolder+"/"+selfFile+".vpk")
        if args.__contains__("-d"):
            try:
                print("Removing "+inputFolder)
                shutil.rmtree(inputFolder)
            except:
                pass




