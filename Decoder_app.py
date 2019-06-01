import os
import pyunpack

class decoder():
    def rar():
        directory = input('directory: ')
    
        FileOrDirectory = input('File or whole directory? f/d: ') 
        if FileOrDirectory == 'd' or FileOrDirectory == 'D':
            for file in os.listdir(os.fsencode(directory)):
                filename = os.fsdecode(file)
                if filename.endswith(".rar"):
                    pyunpack.Archive(directory + '\\' + filename).extractall(directory)

        elif FileOrDirectory == 'f' or FileOrDirectory == 'F':
            filename = input('filename')
            try:
                pyunpack.Archive(directory + '\\' + filename).extractall(directory)
            except:
                print('error: file probably not .rar')
        else:
            return('error: not proper response')
        print('decoding complete')




