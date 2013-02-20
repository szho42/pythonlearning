import re

def main():
    # an re object
    p = re.compile('[a?]')
    # use re to match and return an result object
    p.match("")
    print p.match("abacdeajfja")
    res = p.match("abcdefa")
    
    if res:
        print res.group()
	print res.start()
	print res.end()
	print res.span()

    else:
	print "no match"
    # find all the matches and result a list
    p.findall("abcdakfjaljfkka")
    
    # use re function rather than object
    print re.match(r'from\s+', 'fromage amk')


if __name__ == "__main__":
    main()
