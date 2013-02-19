import cPickle as pickle
import random
import os
import time

def main():
    obj = {"1":"a",
	   "2":"b",
	   "3":"c"}

    #the True parameter tells pickle to compress the obj when dump
    pickle.dump(obj,open("tmp1.txt","wb"),True)

    obj2 = pickle.load(open("tmp1.txt","rb"))

    print obj2

if __name__ =="__main__":
    main()
