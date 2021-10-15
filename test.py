'''
# this is called function aliasing and changing the functionality
def hello(func):
    def wrapper():
        print("hello")
        func()
        print("world")
    return wrapper

def xd():
    print("Kichan Park")

mama = hello(xd)
mama()
'''




#this is using decorator of the code above

def hello(func):
    def wrapper():
        print("hello")
        func()
        print("world")
    return wrapper

@hello
def xd():
    print("Kichan Park")





