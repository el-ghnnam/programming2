#


from os import system
system("cls")


class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, traceback):  #* this parameter are for exceptions.    
        self.file.close()
        
with Open_File("/test.txt", 'w') as f:  #* f is an object of Open_File class.
    f.write('my name is ahmed and my age are 19')

print(f.closed)
    
    