import ConfigParser
import string
import os
import sys

def main():
    cf = ConfigParser.ConfigParser()
    cf.read('db.ini')
    
    secs = cf.sections()
    print 'sections: %s' % secs 

    ops = cf.options('db')
    print 'options: %s' % ops

    its = cf.items('concurrent')
    print 'items: %s' % its

    db_host = cf.get('db','db_host')
    print 'host: %s' % db_host

    db_port = cf.getint('db','db_port')
    print 'port: %d' % db_port

    cf.set('db','db_host','192.168.1.1')
    cf.write(open('db.ini','w'))
    


if __name__ == '__main__':
    main()

