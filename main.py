import os

def changer(folder,file):
    baseDir = os.getcwd()
    print("[+] Moving {} to {}".format(os.path.join(baseDir,file),os.path.join(baseDir,folder,file)))
    if os.path.exists(os.path.join(baseDir,folder)):
        pass
        
    else:
        os.mkdir(folder)

    os.replace(os.path.join(baseDir,file),os.path.join(baseDir,folder,file))

for file in os.listdir(os.getcwd()):
    file = file.lower()
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".aivf")  or file.endswith(".gif") or file.endswith(".apng") or file.endswith(".jfif") or file.endswith(".pjpeg") or file.endswith(".pjp") or file.endswith(".svg") or file.endswith(".webp") or file.endswith(".ico") or file.endswith(".bmp") or file.endswith(".tif"):
        changer("Images",file)
    
    if file.endswith(".mkv") or file.endswith(".mp4") or file.endswith(".webm") or file.endswith(".mov") or file.endswith(".wmv") or file.endswith(".flv") or file.endswith(".mpeg") or file.endswith(".avchd") or file.endswith(".avi"):
        changer("Videos",file)

    if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".m4a") or file.endswith(".flac") or file.endswith(".wma") or file.endswith(".aac"):
        changer("Audio",file)

    if file.endswith(".pdf") or file.endswith(".txt"):
        changer("Documents",file)