#!/bin/bash/env python

import cPickle as pickle

def main():
    obj = {"a":1,
	   "b":2,
	   "c":3}

    #dump an object to a file
    pickle.dump(obj,open("tmp.txt",'w'))

    #load an object from a file
    obj2 = pickle.load(open("tmp.txt","r"))

    print obj2

if __name__ == "__main__":
    main()
