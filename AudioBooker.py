import eyed3
import os, re, sys, shutil

if (len(sys.argv) < 2):
    print('Need Help?\nAudioBooker.py <Path> <AudioBookName> <Author> ')
    sys.exit()
else:
    
    tPath = sys.argv[1]
    #tPath = '..\\..\\..\\MP3Files\\'
print('Root Path:\t' + tPath)



def SetMeta(file,trackTitle,trackNum):
    audiofile = eyed3.load(file)
    audiofile.tag.album = sys.argv[2]
    audiofile.tag.artist = sys.argv[3]
    audiofile.tag.title = trackTitle
    audiofile.tag.album_artist = sys.argv[3]
    audiofile.tag.track_num = trackNum

    audiofile.tag.save()

def PrepNewDir():
    newDir = sys.argv[1] + '\\_AudioBooker'
    if (os.path.isdir(newDir)):
        shutil.rmtree(newDir)


    os.mkdir(newDir)
    return newDir

def Renamer(tPath):
    discNum = 0
    newDir = PrepNewDir()
    for root, dirs, files in os.walk(tPath):
        trackNum = 0
        '''
        print(root)
        print(dirs)
        print(files)
        '''
        if '_AudioBooker' in root:
            continue

        elif (len(files) > 0) and (len(dirs) == 0) :
            discNum +=1


            for file in files:
                if '.mp3' in file:
                    trackNum += 1
                    oldName = file
                    strDiscNum = ('000' + str(discNum))[-2:]
                    strTrackNum = ('000' + str(trackNum))[-2:]
                    newName = str(sys.argv[2]) + '_D' + strDiscNum + 'T' +  strTrackNum + '_' + re.sub(r'\.mp3','',file) + '.mp3'
                    #re.sub(r'\.mp3', '_D' + strDiscNum + 'T' +  strTrackNum ,file)
                    shutil.copyfile(root + '\\' + oldName,newDir + '\\' + newName)
                    #os.rename(root + '\\' + oldName,newDir + '\\' + newName)
                    print('Renamed ' + oldName + ' as ' + newName)
                    # SetMeta(,artist,album,trackTitle,trackNum,album_artist = '')
                    SetMeta(newDir + '\\' + newName,'Track' + strTrackNum,trackNum)


Renamer(tPath)

