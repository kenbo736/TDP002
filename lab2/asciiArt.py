######################################### frame ################################
def frame(text):
    print(len(text)*"*"+4*"*")
    print("*", text, "*")
    print(len(text)*"*"+4*"*")

frame("Hej jag heter Kenneth")

######################################### triangle #############################
def triangle(number):
    for x in range(1, number+1):
        print((2*x*"*")[:-1])

triangle(10)

######################################## flag ##################################
def flag(number):
    for i in range(1, 6):
        print(("*"*10)*number, ("*"*10)*number)
    print("")
    for x in range(1, 6):
        print(("*"*10)*number, ("*"*10)*number)


flag(2)
