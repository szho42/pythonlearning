from base import Base1
from base import Base2

class Child(Base1, Base2):
    __classMem = 123
    
    def __init__(self):
	Base1.__init__(self)
	Base2.__init__(self)
	self.objMem = 456
	print "Child class created."
	self.__x=["a","b","c"]

    @staticmethod
    def test():
	print "this is a static method"

    def __getitem__(self,key):
	return self.__x[key]

    def __setitem__(self,key,vlaue):
	self.__x[key] = value

    def __add__(self,other):
	return self.objMem + other.objMem

    def __eq__(self,other):
	return self.objMem == other.objMem

    def meth(self):
	print "this is an old method"

    """def __getattr__(self,name):
	print "__getattr__", name
	return None
    """
    def __setattr__(self,name,value):
	self.__dict__[name] = value

def meth(self):
    print "this is a new method"

if __name__ == "__main__":
    child = Child()
    child.test()
    print "class member: %s" % Child._Child__classMem
    print "object member: %s" % child.objMem
    Child.test()
    print "%s" % child[0]
    child2 = Child()
    print "__add__ function override result: " + str(child + child2)
    print "child = child2? :" + str(child == child2)

    # dymanically change class members
    child.meth()
    Child.meth = meth
    child.meth()

    # get the attr 
    child.objMem
