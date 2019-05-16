import os

class Folder():
    def file_rename(self, source, destination):
        os.rename(source, destination)

    def getOrCreate(self, path):
        try:  
            os.mkdir(path)
        except OSError:  
            pass 
        return path


        