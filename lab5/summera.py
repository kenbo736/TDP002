############################### a #############################################
def solver(operation, n):
    result = 1
    for i in range(1, n):
        result = operation(i, result)
    return result


#print(solver((lambda x, i: i + x), 513)-1)
#print(solver((lambda x, y: x * y), 513))

############################### b ##############################################
db = [
{"name": "Jakob", "position": "assistant"},
{"name": "Åke", "position": "assistant"},
{"name": "Ola", "position": "examiner"},
{"name": "Henrik", "position": "assistant"}
]

def dbsearch(database, position, valueOfposition):
    return [d for d in database if d[position] == valueOfposition]

#print(dbsearch(db, "position", "examiner"))
################################ c ############################################
haystack = "can you find the needle in this haystack?".split()

def contains(word, theList):
    if(len(list(filter(lambda x : x == word, theList))) > 0):
        return True
    return False
    #inte använda while, använda filter, map
print(contains("can", haystack))
print(contains("needle", haystack))
print(contains("haystack", haystack))
################################ d ############################################
import os

def kommando_tolken():
    run = True
    lista = os.listdir(os.getcwd())
    path = os.getcwd()
    cdPath = path.split("/")
    slash = "/"
    while run:
        command = input("command> ")
        if command == "cd .." or "cd":
            if command == "cd ..":
                cdPath.pop(-1)
                if slash in cdPath:
                    for check in range(0, len(cdPath)):
                        cdPath[check] = cdPath[check][:-1]
                for i in range(0, len(cdPath)):
                    cdPath[i] = cdPath[i] + slash
                cdPath[-1] = cdPath[-1][:-1]
                path = "".join(cdPath)
                print(path)


        if command == "quit":
            run = False
        if command == "pwd":
            print(path)
        if command == "ls":
            print(" ".join(os.listdir(path)))
        if command == "cat" + " " + command[4:]:
            for i in range(0, len(lista)):
                if command[4:] == lista[i]:
                    for line in open(lista[i]):
                        print(line)
#kommando_tolken()

################################ e ############################################
def stars(n): return '*' * n
def mirror(x): return x
def generate_list(function, value):
    lista = []
    for x in range(1, value + 1):
        lista.append(function(x))
    print(lista)
    return lista

#generate_list(stars, 5)
################################ f ############################################
def add(n, m) : return n + m

def partial(function, value1):
     def new_function(value2):
         return function(value1, value2)
     return new_function

#add_five = partial(add, 5)
#add_five calls on the inner function
#add_five(3)

#add_five = partial(add)
################################## g ##########################################
def multiply_five(n):
    return n * 5

def add_ten(x):
    return x + 10

def compose(fa, fb):
    def fres(x):
        return fa(fb(x))
    return fres

composition = compose(multiply_five, add_ten)
#print(composition(3))

################################# h ###########################################
def make_filter_map(filter_f, map_f):
    def new_function(lista):
        return [map_f(l) for l in lista if filter_f(l)]
    return new_function

                            #filter_f                  #map_f
process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)
#print(process(range(10)))
