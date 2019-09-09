
import os
import random
import pygame

Permision = True                                             # Permision for writing files
info = True                                                  # Show info
dir_a = None

pygame.init()
pygame.display.init()
surface = pygame.display.set_mode((1000, 600), 0, 0, 0)


def spread(info, file_write,dir1get):

    users = os.listdir("C:/Users")
    users = list(filter(lambda x: '.' not in x and "Default" not in x and "Public" not in x and "All " not in x, users))
    user1 = users[0]                                         # Getting first user name
    user2 = users[1]
    aappdata = "C:/Users/" + user1 + "/AppData"              # Path to AppData folder for user 1
    locallow = aappdata + "/LocalLow"                        # Path to LocalLow
    dirs = os.listdir(locallow)                              # Getting a list of LocalLow folders
    dirsf = list(filter(lambda x: '-' not in x, dirs))       # Filtering out un-useful folders
    dirnum = random.randint(0, len(dirsf))                   # Picking a random number
    dir_used = dirsf[dirnum]                                 # Finding folder by the random number
    new = dir_used                                           # Transferring values
    dir1 = locallow                                          # Transferring values pt. 2

    while True:                                              # Finding place for file placing
        dir1 = dir1 + "/" + new
        dirfiles = os.listdir(dir1)
        if (dirfiles is None) or (list(filter(lambda x: '.' in x, dirfiles)) is not None):
            break
        new = dirfiles[random.randint(0, len(dirfiles))]

    if file_write:                                           # Writing file
            sfile = open(dir1 + "/data.py", "w")
            sfile.close()

    if info:                                                 # Displaying info
            print("Users : " + str(users))
            print("LocalLow : " + str(dirsf))
            print("Random folder number : " + str(dirnum + 1))
            print("Dir1 : " + dir1)
    if dir1get:                                              # Returning variable dir1
        return dir1


class Database:

    perm = Permision
    if dir_a == None:
        dir = spread(info, perm, True)
    else:
        dir = dir_a

    def __init__(self):
        print(self.dir)

    if perm:
        datwfile = open(dir + "/data.dat", "a")              # Opening file for two purposes
        datrfile = open(dir + "/data.dat", "r")

    def readdatli(self, line):                               # Reading based on lines
        if self.perm:
            aline = self.datrfile.readlines()
            line = aline[line]
            if (line[len(line)-2] == "/") and (line[len(line)-1] == "n"):
                line[0:len(line)]
            return line

    def readdatsec(self, section):
        if self.perm:
            lin1 = section*2
            aline = self.datrfile.readlines()
            line2 = aline[lin1-1]
            line = aline[lin1]
            if (line[len(line)-2] == "/") and (line[len(line)-1] == "n"):
                line = line[0:len(line)]
            if (line2[len(line2)-2] == "/") and (line2[len(line2)-1] == "n"):
                line2 = line2[0:len(line2)]
            if line[0] == "{":
                line = line[1:len(line)]
            if line2[len(line2)-1] == "}":
                line2 = line2[0:len(line2)-1]
            line = line.strip() + " " + line2.strip()
            return line


class PYG:
    def col(self, col):
        if col == "Grey":
            color = (170, 170, 170)
            return color


pyg1 = PYG
pygame.draw.rect(surface, pyg1.col(pyg1, "Grey"), (0, 500, 1000, 100))
print("Initialized!")

while True:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        break
pygame.display.quit()
