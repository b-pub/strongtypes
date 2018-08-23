#
# Can strong typing be implemented with decorators?
#
from strongtypes import *

#----------------
# Test single int parameter 
@prototype(int)
def takesOneInt(arg1):
    print("takesOneInt called with " + str(arg1))

try:
    takesOneInt(3)
except TypeError, exc:
    print("TypeError" + str(exc))

try:
    takesOneInt(3.0)
except TypeError, exc:
    print("Got expected TypeError: " + str(exc))

try:
    takesOneInt('three')
except TypeError, exc:
    print("Got expected TypeError: " + str(exc))


#----------------
# Test with object
class Foo(object):
    def doSomething(self):
        print("Foo.doSomething called")

@prototype(Foo)
def takesAFoo(foo):
    print("Calling foo.doSomething...")
    foo.doSomething()

aFoo = Foo()
try:
    print("First call to takesAFoo...")
    takesAFoo(aFoo)
    print("First call to takesAFoo got a Foo. Calling with a string:")
    takesAFoo('aFoo')
except TypeError, exc:
    print("Got Expected TypeError: " + str(exc))
