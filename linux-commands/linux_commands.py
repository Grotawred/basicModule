import os
import shutil


def ls(directory='.', flags=''):
    if flags:
        command = f"dir /B {directory}"

        if('l' in flags):
            command = f"dir /Q {directory}"
        if('a' in flags):
            command += " /A"
        result = os.popen(command).read()
        return result.split("\n")
    else:
        return os.listdir(directory)


def pwd():

    return os.getcwd()



def mkdir(directory_name):

    os.makedirs(directory_name)



def rm(name):

    if os.path.isfile(name):
        os.remove(name)
    elif os.path.isdir(name):
        os.removedirs(name)
    

def cat(filename):

    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')


def cp(source, destination):
    
    if os.path.isfile(source):
        shutil.copy(source, destination)
    elif os.path.isdir(source):
        shutil.copytree(source, destination)


def mv(source, destination):

    shutil.move(source, destination)