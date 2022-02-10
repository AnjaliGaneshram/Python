import sys
import os
'''
#Os Module
#cwd

print(os.getcwd())

#mkdir

a = os.getcwd()

path = a+"\\Feb-8"

os.mkdir(path)

#listdir - list the directories in the cwd

print(os.listdir("."))

#chdir - change the directory - For path we need to use \\ or /

os.chdir(path)
print(os.getcwd())

#getlogin - Login name of the OS

print(os.getlogin())

#rmdir() - remove the directory
os.chdir("..")
print(os.getcwd())
os.rmdir(path)

#getenv() - print the value from Enviornment Variable and Path is one of the variable in EV.

print(os.getenv("Path"))



'''
#os.open, os.O_RDONLY, os.read, os.close

fd = os.open(".\Temp.txt",os.O_RDONLY)

print(os.read(fd,25))

os.close(fd)












