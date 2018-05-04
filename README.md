# UnityTools
Tools for Making it easier to get games created with Unity for PSVita games to run on HENKAKU..

Python3.5

Arguments:
    -i Input DIR  
    -o output DIR  
    -f Fix the "Unsafe homebrew" bug (that prevents the game from launching if unsafe homebrew is enabled)  
    -u Remove the "trial version" watermark caused by development build in the bottom right corner  
    -r Remove unused files from your build  
    -p Pack to "PC HOSTED" builds to .VPK  
    -d Remove input directory after packing into .vpk  
    

Also, after building a "PC HOSTED" application with UNITY. you can just drag n drop the folder onto the application
and it will run: `-f -u -r -p -d` on it.
