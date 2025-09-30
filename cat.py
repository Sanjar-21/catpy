import sys
# import os
class Cat:
    """ Linux cat command """
    def __init__(self):
       pass

    def cat(self, file):
        with open(file, "r") as files:
            for file in files:
                print(file, end="")

if __name__ == '__main__':
    cat = Cat()
    cat.cat(sys.argv[1])
