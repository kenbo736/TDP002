def create_shopping_list():
    lista = ["Kurslitteratur", "Anteckningsblock", "Penna"]
    return lista

def shopping_list(slist):
    for i in range(0, len(slist)):
        print(i+1, slist[i])

def shopping_add(slist):
    laggTill = input("Vad vill du lägga till? ")
    lista = slist.append(laggTill)
    return lista

def shopping_remove(slist):
    taBort = int(input("Vad vill du ta bort? "))-1
    lista = slist.remove(slist[taBort])
    return lista

def shopping_edit(slist):
    edit = int(input("Vad vill du ändra på? "))-1
    newEdit = input("Vad vill du ska stå istället för " + slist[edit] + "? ")
    lista = slist.insert(edit, newEdit),
    lista2 = slist.remove(slist[edit+1])

    return lista, lista2

slist = create_shopping_list()
shopping_list(slist)
shopping_add(slist)
shopping_list(slist)
shopping_remove(slist)
shopping_list(slist)
shopping_edit(slist)
shopping_list(slist)
