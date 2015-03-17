import sys
import threading

def main():

    for x in range(0, 10):
        thr = threading.Thread(group=None, target=foo, name=None, args=[(x)])
        thr.start() # will run "foo"
        thr.is_alive() # will return whether foo is running currently
        thr.join() # will wait till "foo" is donedef foo():

def foo(y):
    for x in range (y, 10):
        print(str(y) + "From Thread: " + str(y))
    print("This thread is done!")


if __name__ == '__main__':
    main()
