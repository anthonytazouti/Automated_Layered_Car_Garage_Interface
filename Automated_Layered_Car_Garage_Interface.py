import time

#This is a definition that makes puts a box around the "boxAround" string, this is more of a styling add on.
def boxAround(thePrintableText):
    length = len(thePrintableText)
    print("*" * (length + 4))
    print("* " + thePrintableText + " *")
    print("*" * (length + 4))
boxAround("Type DONE when you are finished entering all your cars.")



levelCount = -1
listwhatCar = []
while True:
    levelCount = levelCount + 1
    whatCar = input(f"What car is on level {levelCount+1}?\n")
    if whatCar == "done":
        break
    listwhatCar.append(whatCar)
print("Here is a list of all of your cars:")
print(listwhatCar)
print(" ")



while True:
        whatCar = int(input("What level would you like delivered?\n"))
        whatCar = int(whatCar)
        whatCar = whatCar - 1
        numValue = listwhatCar[whatCar]
        for i in range(whatCar + 1, 0, -1):
            print("Descending in ", (i),"!")
            time.sleep(1)
        print("")
        print("*"*37)
        print(f"Your", numValue.upper(), "has descended from level", whatCar + 1,"!")
        print("*" * 37)
        break
