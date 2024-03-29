'''
    py script - Creates file within directory on being  provided by an absolute path
    py libraries -
        1. os - Used to work with file directories and operating system
        2. os.path - Used to work with absolute paths
        3. re - Used to validate strings
    classes-
            IsFileException- Class to handle creating file inside file exception
            CreateFile - Class to create file
    '''
import os
import os.path
class IsFileException(Exception):
    def __str__(self):
        return ("Cannot create file inside a file")

class CreateFile(IsFileException):
    def __init__(self):
        pass

    #Method to get penultimate path i.e the destination location for file creation
    #error handing(creation of file inside a file)
    def getDestinationPath(self,path):
        destPath=""
        tempPath = path.split("\\")
        for dir in tempPath:
            if dir != tempPath[-1]:
                destPath = destPath +"\\"+ str(dir)
        return destPath

    #Method to create file in the specified absolute path
    def createFile(self,path):
        try:
            checkPath=self.getDestinationPath(path)
            if(checkPath.find(".")!=-1):
                    raise IsFileException
            if(os.path.exists(path)):
                raise FileExistsError
            f=open(path,"w+")
            f.close()
            return ((path, "TRUE"))
        except IsFileException as error:
            return(error)
        except (FileExistsError):
            print("Unable to create file")
            return ((("NO such file created", "FAlSE")))


# obj= CreateFile()
# print(obj.createFile("C:\\Users\\pc\\PycharmProjects\\myDir\\new.txt"))