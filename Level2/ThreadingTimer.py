from threading import Timer

timeout = 5
t = Timer(timeout, print, ["Times up"])
t.start()

answer = input("Hi!")
t.cancel()






