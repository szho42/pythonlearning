#!/bin/bash/python
# coding=utf-8

# Python will default to ASCII as standard encoding if no other
# encoding hints are given.
# To define a source code encoding, a magic comment must
# be placed into the source files either as first or second
# line in the file, such as:

#    # coding=<encoding name>
#   or (using formats recognized by popular editors)

#    #!/usr/bin/python
#    # -*- coding: <encoding name> -*-
#    or
#    #!/#usr/bin/python
#    # vim: set fileencoding=<encoding name> :

#sample code
def main():
    s = "中国"

    ss = u"中国"

    print s
    type(s)
    len(s)

    print ss
    type(ss)
    len(ss)

    print '-' * 40

    print repr(s)

    print '-' * 40

    ss1 = s.decode('utf-8')
    print ss1
    len(ss1)
    type(ss1)

    print '-' * 40

    ss2 = s.decode('utf-8').encode('gbk')

    print ss2
    print type(ss2)
    print len(ss2)
    print '-' * 40

    ss3 = ss.encode('gbk')
    print ss3
    print type(ss3)
    print len(ss3)

if __name__ == "__main__":
    main()


